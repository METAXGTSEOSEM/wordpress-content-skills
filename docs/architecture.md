# WordPress Content Skills architecture

## A module is the installation boundary

Every released workflow lives under `skills/<skill-id>/` and has one `SKILL.md` entry. The folder includes all references, templates, and host metadata needed for that module.

A host or installer may copy only that folder. A Skill must not depend on `../../docs`, another module's private files, or the maintainer's local paths.

Repository documentation can link to multiple modules. Runtime instructions must remain installable on their own.

## Catalog states

`catalog.json` records modules and versions.

- `available`: a real Skill exists at `path`, with matching name and version.
- `planned`: a reserved idea or specification, with `path` and `version` set to `null`.

Do not create empty Skill entries for planned work. Product discovery and installation must expose only available catalog entries.

The README catalog mirrors these states. Update it when a module changes status.

## Names and versions

Keep `independent-site-article` stable. It is the article module's installation identity, not the name of the whole library.

The product name is WordPress Content Skills and its repository is `https://github.com/METAXGTSEOSEM/wordpress-content-skills`. Library release `1.5.0` keeps the article module at `1.3.0`.

The library version describes repository changes. Each available module also has its own version in the catalog and Skill metadata.

Use a patch version for corrections that preserve the workflow, a minor version for compatible additions, and a major version for a breaking contract change. Explain migration in the changelog.

## Shared principles without broken dependencies

Evidence, language editing, explicit review states, and publishing boundaries apply across the library. Document them centrally for contributors, then include the relevant operational rules inside each released module.

Do not force articles, product pages, case studies, and UI/UX into the same production prompt. They have different evidence requirements and acceptance criteria.

Some repetition is acceptable when it keeps a copied Skill usable. Validate links so that reference extraction does not break installation.

## Roles are execution instructions

The article module describes eight responsibilities in `references/roles.md`. They are not eight installed Skills or eight automatically registered subagents.

A coordinator may delegate roles using the host's actual capabilities. If independent review is unavailable, report the limitation. Do not turn a host-dependent feature into a promise.

Future modules can reuse this execution pattern while defining different reviewers.

## Repository maintenance

Repository maintenance belongs under `.github/` as an internal contributor workflow, outside the product catalog, Skill discovery, and installation.

## Public examples and guides

`examples/` contains complete, clearly labeled synthetic packages that show the
input, review evidence and final handoff. Examples are documentation, not
installable Skills. `docs/` contains field mapping, publishing checks,
compatibility, data handling and FAQ guidance for users.

Do not present a synthetic sample as a real customer result. Keep sample product
data visibly fictional or marked as missing.

## UI and documentation

The repository interface is the GitHub README: a local SVG cover, navigation, a status catalog, host-independent installation instructions, and a workflow diagram.

The UI/UX module is separate planned work. A redesigned README is not an implementation of that module.

Keep text readable without images. Status must be stated in text, not color alone. Keep visual assets local and avoid scripts or external font dependencies in SVGs.

## User material stays outside the repository

Store production drafts, customer records, screenshots, credentials, and review runs in the user's project workspace. Publish only general workflows and blank templates.

## Validation

`python3 scripts/validate.py` checks catalog consistency, module names and versions, local links, packaging boundaries, English-only text, and SVG structure. It does not prove editorial quality, current policy accuracy, or performance.

Run the official Skill validator separately when available. Test meaningful behavior before marking a new module available, including missing evidence, missing tools, and changes after approval.
