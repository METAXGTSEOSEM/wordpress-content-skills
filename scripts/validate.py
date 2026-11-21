import argparse
import csv
import json
import re
import sys
import xml.etree.ElementTree as element_tree
from pathlib import Path
from urllib.parse import unquote, urlsplit


def inside(path, boundary):
    return path.resolve().is_relative_to(boundary.resolve())


def scalar(text, key):
    match = re.search(r"^" + re.escape(key) + r":\s*[\"']?([a-z0-9.-]+)", text, re.M)
    return match.group(1) if match else None


def csv_header(path):
    try:
        with path.open(newline="", encoding="utf-8") as handle:
            return next(csv.reader(handle), None)
    except OSError:
        return None


def validate_examples(root):
    errors = []
    required = {
        "project-management-tool-article": [
            "README.md", "brief.md", "sources.csv", "claims.csv", "draft-v1.md",
            "review.md", "final.md", "wordpress-fields.md", "cluster-map.csv",
            "keyword-plan.csv", "image-plan.csv", "seo-geo-delivery.md",
        ],
        "audience-rewrite": ["README.md", "before.md", "after.md", "review.md"],
    }
    for folder_name, files in required.items():
        folder = root / "examples" / folder_name
        for filename in files:
            if not (folder / filename).is_file():
                errors.append(f"examples/{folder_name}: missing {filename}")
    template_folder = root / "skills/independent-site-article/assets"
    example_folder = root / "examples/project-management-tool-article"
    for filename in ["sources.csv", "claims.csv", "cluster-map.csv", "keyword-plan.csv", "image-plan.csv"]:
        expected = csv_header(template_folder / filename)
        actual = csv_header(example_folder / filename)
        if expected and actual != expected:
            errors.append(f"examples/project-management-tool-article/{filename}: headers do not match the template.")
    return errors


def validate_role_docs(root):
    errors = []
    roles_path = root / "skills/independent-site-article/references/roles.md"
    readme_path = root / "README.md"
    architecture_path = root / "docs/architecture.md"
    if not roles_path.is_file() or not readme_path.is_file():
        return ["Cannot validate role documentation: missing roles.md or README.md."]
    roles = re.findall(r"^## (.+)$", roles_path.read_text(encoding="utf-8"), re.M)
    readme = readme_path.read_text(encoding="utf-8")
    table = re.search(
        r"\| Role \| Responsibility \|\n\|[^\n]*\|\n((?:\|[^\n]*\|\n?)+)",
        readme,
    )
    if not table:
        return ["README role table was not found."]
    table_text = table.group(1).lower()
    for role in roles:
        candidates = [role]
        if role.startswith("Independent "):
            candidates.append(role.removeprefix("Independent "))
        if not any(candidate.lower() in table_text for candidate in candidates):
            errors.append(f"README role table is missing: {role}")
    count_words = {7: "seven", 8: "eight", 9: "nine", 10: "ten"}
    expected_count = count_words.get(len(roles))
    if expected_count and architecture_path.is_file():
        architecture = architecture_path.read_text(encoding="utf-8")
        if f"describes {expected_count} responsibilities" not in architecture:
            errors.append(
                f"docs/architecture.md must describe {expected_count} responsibilities "
                f"to match roles.md."
            )
    return errors


def validate(root):
    errors = []
    catalog_file = root / "catalog.json"
    try:
        catalog = json.loads(catalog_file.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        return [f"Cannot read catalog.json: {error}"]
    if catalog.get("documentation_language") != "en":
        errors.append("Documentation language must be en.")
    if catalog.get("default_output_language") != "en":
        errors.append("Default output language must be en.")
    if not re.fullmatch(r"\d+\.\d+\.\d+", str(catalog.get("version", ""))):
        errors.append("Library version must use major.minor.patch.")
    modules = catalog.get("modules")
    if not isinstance(modules, list) or not modules:
        return errors + ["Catalog modules must be a nonempty list."]
    known_ids = set()
    available_entries = set()
    for module in modules:
        if not isinstance(module, dict):
            errors.append("Each catalog module must be an object.")
            continue
        module_id = module.get("id", "")
        if not isinstance(module_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", module_id):
            errors.append(f"Invalid module ID: {module_id}")
            continue
        if module_id in known_ids:
            errors.append(f"Duplicate module ID: {module_id}")
        known_ids.add(module_id)
        status = module.get("status")
        if status == "planned":
            if module.get("path") is not None or module.get("version") is not None:
                errors.append(f"{module_id}: planned modules cannot have an installed path or version.")
            continue
        if status != "available":
            errors.append(f"{module_id}: unsupported status {status}")
            continue
        expected_path = "skills/" + module_id
        if module.get("path") != expected_path:
            errors.append(f"{module_id}: path must be {expected_path}")
            continue
        folder = root / expected_path
        entry = folder / "SKILL.md"
        available_entries.add(entry.resolve())
        if not inside(entry, root / "skills") or not entry.is_file():
            errors.append(f"{module_id}: missing or out-of-bounds SKILL.md")
            continue
        text = entry.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\n(.*?)\n---(?:\n|$)", text, re.S)
        if not frontmatter:
            errors.append(f"{module_id}: missing frontmatter")
            continue
        header = frontmatter.group(1)
        if scalar(header, "name") != module_id:
            errors.append(f"{module_id}: frontmatter name does not match its ID.")
        version = re.search(r"^\s+version:\s*[\"']?(\d+\.\d+\.\d+)", header, re.M)
        if not version or version.group(1) != module.get("version"):
            errors.append(f"{module_id}: catalog and Skill versions differ.")
        if not re.search(r"^description:\s*\S", header, re.M):
            errors.append(f"{module_id}: missing description")
        interface = folder / "agents/openai.yaml"
        if not interface.is_file():
            errors.append(f"{module_id}: missing agents/openai.yaml")
        elif "$" + module_id not in interface.read_text(encoding="utf-8"):
            errors.append(f"{module_id}: default prompt must name the Skill.")
    discovered = {path.resolve() for path in (root / "skills").rglob("SKILL.md")}
    if discovered != available_entries:
        errors.append("Available catalog modules do not match discoverable SKILL.md files.")
    if "project-maintenance" in known_ids:
        errors.append("Repository upkeep must not be an installable content module.")
    for path in (root / ".github/workflows").glob("*.yml"):
        if path.name.startswith("._"):
            continue
        if re.search(r"^\s+schedule:", path.read_text(encoding="utf-8"), re.M):
            errors.append(f"{path.name}: periodic maintenance schedules are not enabled.")
    readme = root / "README.md"
    if not readme.is_file():
        errors.append("Missing root README.md.")
    else:
        readme_text = readme.read_text(encoding="utf-8")
        if "**Current release:** `" + catalog.get("version", "") + "`" not in readme_text:
            errors.append("README release does not match catalog.json.")
        if "**Available modules:** `" + str(len(available_entries)) + "`" not in readme_text:
            errors.append("README available-module count does not match the catalog.")
    errors.extend(validate_examples(root))
    errors.extend(validate_role_docs(root))
    for path in root.rglob("*"):
        relative = path.relative_to(root)
        if any(part in {".git", "__pycache__", "articles", "verification-private", ".maintenance"} or part.startswith("._") for part in relative.parts):
            continue
        if re.search(r"[\u3400-\u9fff]", str(relative)):
            errors.append(f"{relative}: filename must be English.")
        if path.is_symlink():
            errors.append(f"{relative}: symlinks are not supported in packages.")
        if not path.is_file():
            continue
        if path.suffix not in {".md", ".json", ".yaml", ".yml", ".csv", ".py", ".svg"}:
            continue
        text = path.read_text(encoding="utf-8")
        if re.search(r"[\u3400-\u9fff]", text):
            errors.append(f"{relative}: non-English CJK text found.")
        if path.suffix == ".md":
            if text.count("```") % 2:
                errors.append(f"{relative}: unmatched fenced block")
            targets = re.findall(r"\]\(([^)\s]+)\)|\bsrc=\"([^\"]+)\"", text)
            for markdown_target, image_target in targets:
                target = markdown_target or image_target
                parsed = urlsplit(target)
                if parsed.scheme or parsed.netloc or not parsed.path:
                    continue
                resolved = path.parent / unquote(parsed.path)
                if not inside(resolved, root) or not resolved.exists():
                    errors.append(f"{relative}: broken local link {target}")
                for module_entry in available_entries:
                    boundary = module_entry.parent
                    if inside(path, boundary) and not inside(resolved, boundary):
                        errors.append(f"{relative}: link escapes its installable Skill: {target}")
        if path.suffix == ".csv":
            rows = list(csv.reader(text.splitlines()))
            if not rows or len(rows[0]) != len(set(rows[0])):
                errors.append(f"{relative}: invalid or duplicate CSV headers")
        if path.suffix == ".svg":
            try:
                document = element_tree.fromstring(text)
                if "viewBox" not in document.attrib:
                    errors.append(f"{relative}: SVG needs a viewBox.")
                for node in document.iter():
                    if node.tag.rsplit("}", 1)[-1] in {"script", "foreignObject"}:
                        errors.append(f"{relative}: executable or embedded HTML is not allowed.")
                    for key, value in node.attrib.items():
                        if key.lower().startswith("on") or "http" in value or "@import" in value:
                            errors.append(f"{relative}: external resources or event handlers are not allowed.")
            except element_tree.ParseError as error:
                errors.append(f"{relative}: invalid SVG: {error}")
    return errors


def main():
    parser = argparse.ArgumentParser(description="Validate the SOP library without network access.")
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    arguments = parser.parse_args()
    errors = validate(arguments.root.resolve())
    for error in errors:
        print("ERROR: " + error, file=sys.stderr)
    if errors:
        return 1
    print("Catalog, packages, local links, English text, CSV, and SVG checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
