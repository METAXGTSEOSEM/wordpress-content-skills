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


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9]+(?:['’-][A-Za-z0-9]+)*", text))


def validate_examples(root):
    errors = []
    required = {
        "project-management-tool-article": [
            "README.md", "brief.md", "sources.csv", "claims.csv", "draft-v1.md",
            "review.md", "final.md", "final-review.md", "wordpress-fields.md",
            "cluster-map.csv", "keyword-plan.csv", "image-plan.csv",
            "seo-geo-delivery.md",
        ],
        "audience-rewrite": ["README.md", "before.md", "after.md", "review.md"],
        "cluster-architecture-small-site": [
            "README.md", "architecture-brief.md", "site-inventory.csv",
            "cluster-map.csv", "link-plan.csv", "architecture-report.md",
        ],
    }
    for folder_name, files in required.items():
        folder = root / "examples" / folder_name
        for filename in files:
            if not (folder / filename).is_file():
                errors.append(f"examples/{folder_name}: missing {filename}")
    template_folder = root / "skills/independent-site-article/assets"
    example_folder = root / "examples/project-management-tool-article"
    ledger_header = [
        "date", "article_id", "url", "content_type", "reader", "title_pattern",
        "opening_move", "first_three_h2", "proof_type", "cta", "signature_detail",
        "similar_to", "review_note",
    ]
    if csv_header(template_folder / "article-style-ledger.csv") != ledger_header:
        errors.append("skills/independent-site-article/assets/article-style-ledger.csv: invalid headers.")
    brief_template = template_folder / "brief.md"
    if brief_template.is_file() and "## Recent-article differentiation" not in brief_template.read_text(encoding="utf-8"):
        errors.append("skills/independent-site-article/assets/brief.md: missing recent-article differentiation section.")
    for filename in ["sources.csv", "claims.csv", "cluster-map.csv", "keyword-plan.csv", "image-plan.csv"]:
        expected = csv_header(template_folder / filename)
        actual = csv_header(example_folder / filename)
        if expected and actual != expected:
            errors.append(f"examples/project-management-tool-article/{filename}: headers do not match the template.")
    cluster_template = root / "skills/cluster-architecture/assets"
    cluster_example = root / "examples/cluster-architecture-small-site"
    for filename in ["site-inventory.csv", "cluster-map.csv", "link-plan.csv"]:
        expected = csv_header(cluster_template / filename)
        actual = csv_header(cluster_example / filename)
        if expected and actual != expected:
            errors.append(f"examples/cluster-architecture-small-site/{filename}: headers do not match the template.")
    final = example_folder / "final.md"
    delivery = example_folder / "seo-geo-delivery.md"
    final_review = example_folder / "final-review.md"
    image_plan = example_folder / "image-plan.csv"
    if final.is_file() and delivery.is_file():
        final_text = final.read_text(encoding="utf-8")
        delivery_text = delivery.read_text(encoding="utf-8")
        range_match = re.search(
            r"Recommended content-length range:\s*([\d,]+)\s*[–-]\s*([\d,]+)\s*words",
            delivery_text,
        )
        if not range_match:
            errors.append("examples/project-management-tool-article/seo-geo-delivery.md: missing a parseable length range.")
        else:
            low = int(range_match.group(1).replace(",", ""))
            high = int(range_match.group(2).replace(",", ""))
            actual = word_count(final_text)
            if not low <= actual <= high:
                errors.append(
                    "examples/project-management-tool-article/final.md: "
                    f"{actual} words is outside the recommended {low}-{high} range."
                )
        if re.search(r"Visible FAQ", delivery_text, re.I) and not re.search(
            r"^## Frequently asked questions\s*$", final_text, re.M | re.I
        ):
            errors.append("examples/project-management-tool-article/final.md: visible FAQ is missing.")
        for field in ["Range set after outline and before draft", "Actual length", "Variance and reason"]:
            if field not in delivery_text:
                errors.append(
                    "examples/project-management-tool-article/seo-geo-delivery.md: "
                    f"missing {field}."
                )
        if re.search(r"Table or specification block", delivery_text, re.I) and not re.search(
            r"^\|[^\n]+\|\n\|[\s:|-]+\|", final_text, re.M
        ):
            errors.append("examples/project-management-tool-article/final.md: visible table is missing.")
        if image_plan.is_file():
            with image_plan.open(newline="", encoding="utf-8") as handle:
                for row in csv.DictReader(handle):
                    image_id = row.get("image_id", "").strip()
                    if image_id and image_id not in final_text:
                        errors.append(
                            "examples/project-management-tool-article/final.md: "
                            f"missing image marker {image_id}."
                        )
    if final_review.is_file():
        review_text = final_review.read_text(encoding="utf-8")
        if not re.search(r"Editorial decision:\s*`?(PASS|REWORK|BLOCKED)`?", review_text):
            errors.append("examples/project-management-tool-article/final-review.md: missing editorial decision.")
    if cluster_example.is_dir():
        errors.extend(validate_cluster_example(cluster_example))
    return errors


def validate_cluster_example(folder):
    errors = []
    inventory_path = folder / "site-inventory.csv"
    cluster_path = folder / "cluster-map.csv"
    link_path = folder / "link-plan.csv"
    report_path = folder / "architecture-report.md"
    try:
        with inventory_path.open(newline="", encoding="utf-8") as handle:
            inventory = list(csv.DictReader(handle))
        with cluster_path.open(newline="", encoding="utf-8") as handle:
            clusters = list(csv.DictReader(handle))
        with link_path.open(newline="", encoding="utf-8") as handle:
            links = list(csv.DictReader(handle))
    except OSError as error:
        return [f"examples/cluster-architecture-small-site: cannot read CSV: {error}"]
    inventory_urls = {row.get("url", "").strip() for row in inventory}
    if not inventory_urls:
        errors.append("examples/cluster-architecture-small-site/site-inventory.csv: no URLs.")
    allowed_inventory = {
        "status": {"existing", "draft", "proposed", "redirected", "noindex", "retired", "unknown"},
        "page_role": {"pillar", "cluster", "product-category", "product", "comparison", "case-study", "faq-glossary", "utility", "unknown"},
        "business_value": {"high", "medium", "low", "unknown"},
        "conversion_role": {"inquiry", "purchase", "lead-support", "retention", "none", "unknown"},
        "evidence_status": {"available", "partial", "missing", "unknown"},
        "orphan_status": {"not-orphan", "orphan", "unknown"},
    }
    for row in inventory:
        for field, allowed in allowed_inventory.items():
            if row.get(field) not in allowed:
                errors.append(f"inventory has an unknown {field}: {row.get(field)}")
    for row in clusters:
        if row.get("url", "").strip() not in inventory_urls:
            errors.append(f"cluster map URL is missing from inventory: {row.get('url')}")
        if row.get("page_role") not in {"pillar", "cluster", "product-category", "product", "comparison", "case-study", "faq-glossary", "utility", "unknown"}:
            errors.append(f"cluster map has an unknown page_role: {row.get('page_role')}")
        if row.get("priority") not in {"high", "medium", "low", "unknown"}:
            errors.append(f"cluster map has an unknown priority: {row.get('priority')}")
        if row.get("evidence_status") not in {"available", "partial", "missing", "unknown"}:
            errors.append(f"cluster map has an unknown evidence_status: {row.get('evidence_status')}")
        if row.get("cannibalization_status") not in {"none", "potential", "confirmed", "resolved", "unknown"}:
            errors.append(f"cluster map has an unknown cannibalization_status: {row.get('cannibalization_status')}")
    for row in links:
        for field in ["source_url", "target_url"]:
            if row.get(field, "").strip() not in inventory_urls:
                errors.append(f"link plan {field} is missing from inventory: {row.get(field)}")
        if row.get("link_status") not in {"proposed", "live", "missing", "redirected", "broken", "unknown"}:
            errors.append(f"link plan has an unknown link_status: {row.get('link_status')}")
        if row.get("link_type") not in {"pillar-to-cluster", "cluster-to-pillar", "sibling", "guide-to-product", "case-to-product", "product-to-guide", "other"}:
            errors.append(f"link plan has an unknown link_type: {row.get('link_type')}")
        if row.get("target_status") not in {"existing", "draft", "proposed", "redirected", "noindex", "retired", "missing", "unknown"}:
            errors.append(f"link plan has an unknown target_status: {row.get('target_status')}")
    if not any(row.get("orphan_status") == "orphan" for row in inventory):
        errors.append("examples/cluster-architecture-small-site: missing an orphan example.")
    if not any(row.get("cannibalization_status") == "confirmed" for row in clusters):
        errors.append("examples/cluster-architecture-small-site: missing a confirmed cannibalization example.")
    if report_path.is_file():
        report = report_path.read_text(encoding="utf-8")
        for heading in ["Cannibalization decisions", "Content gaps and next pages", "Orphan pages", "Internal-link plan"]:
            if f"## {heading}" not in report:
                errors.append(f"examples/cluster-architecture-small-site/architecture-report.md: missing {heading}.")
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


def validate_cluster_templates(root):
    errors = []
    folder = root / "skills/cluster-architecture/assets"
    expected = {
        "site-inventory.csv": [
            "url", "canonical_url", "status", "title", "h1", "meta_description",
            "page_role", "content_type", "primary_reader", "market", "language",
            "business_value", "conversion_role", "evidence_status",
            "last_modified", "last_checked", "inbound_link_count",
            "orphan_status", "source", "notes",
        ],
        "cluster-map.csv": [
            "cluster_id", "pillar_url", "url", "page_role", "primary_intent",
            "focus_keyword", "parent_pillar", "sibling_urls", "priority",
            "priority_reason", "evidence_status", "cannibalization_status",
            "notes",
        ],
        "link-plan.csv": [
            "source_url", "target_url", "anchor_text", "link_type",
            "link_status", "target_status", "notes",
        ],
    }
    for filename, expected_header in expected.items():
        if csv_header(folder / filename) != expected_header:
            errors.append(f"skills/cluster-architecture/assets/{filename}: invalid headers.")
    for filename in ["architecture-brief.md", "architecture-report.md"]:
        if not (folder / filename).is_file():
            errors.append(f"skills/cluster-architecture/assets/{filename}: missing template.")
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
    errors.extend(validate_cluster_templates(root))
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
