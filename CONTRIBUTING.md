# Contributing to WordPress Content Skills

Product development covers the available article Skill and the separately planned product-page, case-study, and UI/UX modules. Repository operations are documented in [the internal maintenance guide](.github/MAINTENANCE.md).

## Update an existing Skill

1. Identify the actual request or failure the change addresses.
2. Edit the relevant module without expanding unrelated triggers.
3. Check current primary sources when changing factual policy guidance.
4. Preserve required editor routing, evidence boundaries, and review states.
5. Bump the module version in `SKILL.md` and `catalog.json`.
6. Update the library version and `CHANGELOG.md` where appropriate.
7. Run `python3 scripts/validate.py` and the official Skill validator if available.
8. Check affected behavior and the README rendering before publishing.

Keep all documentation, instructions, templates, filenames, and interface metadata in English. Default generated output to English; preserve explicit user language choices where a module supports them.

## Add a workflow

Start with the [roadmap](docs/roadmap.md). A planned entry has no installed path or version.

When implementation is ready, add:

```text
skills/<skill-id>/
  SKILL.md
  agents/openai.yaml
  references/
  assets/
```

Use lowercase letters, numbers, and hyphens for the ID. Match the folder, frontmatter name, and catalog ID.

Only add references or assets the workflow actually uses. Keep the entry concise, with task-specific detail in supporting files. Do not make one module read sibling files that an installer may omit.

Define:

- Trigger and boundaries.
- Essential inputs and handling of missing evidence.
- Responsibilities and handoffs.
- Required versus optional external capabilities.
- Deliverables and acceptance states.
- What invalidates approval after a revision.
- External-action authorization.

Test a realistic request, a missing-evidence case, and unavailable required capabilities. Document actual limits rather than inventing a successful result.

Then mark the catalog entry `available`, set its path and version, and update the README. Do not publish an empty module to make the roadmap appear complete.

## Documentation UI

Keep the product README focused on WordPress content, discovery, installation, use, and release status. Keep repository operations in contributor documentation. Use local SVG assets with a viewBox, accessible text, and no embedded scripts or remote resources.

Use text labels for status. Keep planned and available modules visibly distinct. Update catalog counts, headings, and links together.

Use WordPress Content Skills as the display name and `https://github.com/METAXGTSEOSEM/wordpress-content-skills` as the repository URL. Installation instructions must be host-independent and preserve each complete Skill folder and required language-editor routing.

## Examples and public guidance

Examples must be complete enough to inspect, but they must not present fictional
product data as verified. Label synthetic samples and preserve missing evidence.
When a change alters the user-facing deliverable, update the relevant example and
check that its links still resolve.

A complete example package includes the brief, sources, claims, draft, review,
final article, cluster map, keyword plan, image plan and SEO/GEO delivery sheet.
The validator checks that these files exist and that CSV headers match the
templates.

## Release notes

Record added capabilities, behavior changes, compatibility, dependencies, and what was tested. Do not claim that editing policy references proves ranking or citation improvements.

Never commit user content, credentials, local absolute paths, or private review runs.
