# Changelog

## Unreleased

- Complete the worked example with cluster map, keyword plan, image plan and SEO/GEO delivery sheet.
- Add a synthetic training-manual versus decision-led opening example.
- Validate example completeness, CSV template headers and README role-table consistency.
- Add a public quality-gate guide for `PASS`, `REWORK`, `BLOCKED` and separate technical statuses.
- Add a security policy and project code of conduct with private reporting paths.
- Add a rendered delivery preview and update the README overview and latest-release line.
- Add a structured Show and tell discussion template for redacted article packages.
- Align the worked example's length range, visible table, FAQ, image markers and final-review record.
- Validate example length, GEO elements, image markers and final-review decisions.
- Clarify README quality boundaries and remove the unsupported publish-ready claim.
- Record length units and set provisional ranges before drafting; record actual length and variance at delivery.

## 1.5.0 - 2026-11-20

- Add audience and voice calibration so procurement, owner, engineer and operator readers receive different openings, evidence and CTAs.
- Add a topic-cluster map, one-intent-per-URL rule, cannibalization decisions and internal-link planning.
- Add keyword planning with owner-supplied lists, authorized DataForSEO data or clearly labeled AI hypotheses.
- Add SEO/GEO delivery fields, image planning, and per-article length/image-count rationale.
- Add anti-template checks against sibling pages and guardrails against training-manual openings.
- Add cluster, keyword, image and SEO/GEO templates to the article Skill.
- Bump the article module to `1.3.0`; keep the existing Skill ID.

## 1.4.0 - 2026-11-20

- Add a primary content-type framework to the article Skill: awareness, selection, comparison, specification, application, troubleshooting, certification and procurement.
- Define type-specific required sections, evidence priorities, CTAs, failure modes and review gates.
- Record the selected type and rationale in the brief and review/delivery record.
- Update the worked example to declare a selection-guide type.
- Add guardrails against fixed word counts, keyword density, copied competitor outlines and invented EEAT experience.
- Bump the article module to `1.2.0`; keep the existing Skill ID.

## 1.3.0 - 2026-11-18

- Rebrand the product as WordPress Content Skills at `https://github.com/METAXGTSEOSEM/wordpress-content-skills`.
- Focus discovery on WordPress article writing, SEO content, and GEO / AI search review.
- Keep the article Skill ID `independent-site-article` and module version `1.1.0` unchanged.
- Keep product pages, case studies, and UI/UX improvements explicitly planned.
- Remove repository maintenance from the product catalog and installation guidance; direct contributors to internal `.github/` documentation.
- Replace periodic maintenance with GitHub feedback events, secret-backed Telegram delivery, and an automated receipt for new Issues.
- Remove daily validation scheduling and the local four-hour heartbeat; validation runs on changes or an explicit manual dispatch.
- Keep feedback routing distinct from diagnosis and repair; no autonomous model backend, merge, or release is enabled.
- Replace host-specific installation steps with complete-folder installation and required `humanizer` / `humanizer-zh` routing.
- Refresh the local SVG cover and remove an attribution for code that was not copied.
- Preserve evidence requirements, independent review, publishing authorization, and the limits on ranking and AI-citation claims.
- Add a complete synthetic article package from brief and evidence ledger through review, final copy, and WordPress fields.
- Add WordPress field mapping, publishing checklist, compatibility, data handling, and FAQ documentation.
- Add public quickstart, release badges, issue templates, and community links for usage questions and redacted examples.
- Exclude repository-owner and bot events from feedback notification to avoid self-notification noise; keep manual dispatch for delivery tests.
- Clarify who the article workflow helps: article structure, topic placement, incomplete product evidence and revision of AI-assisted drafts.

## 1.2.0 - 2026-11-18

- Add the self-contained `project-maintenance` Skill alongside the article module.
- Integrate multi-channel feedback intake, deduplication, revision-bound review, and repository checks.
- Configure GitHub Issues, PR feedback, and CI for this library; leave other channels disabled until scoped and authorized.
- Exclude website feedback and website monitoring because there is no website to maintain.
- Add a local run guard, state templates, a recurring-run prompt, and maintenance documentation.
- Keep remote changes and external replies separate from the default local-repair authorization.
- Add a daily validation schedule in GitHub Actions; this is a structural check, not an autonomous repair agent.

## 1.1.0 - 2026-11-17

### Library

- Present the repository as a modular workflow library under its previous name.
- Add a machine-readable catalog and extension architecture.
- Reserve product-page, case-study, and UI/UX modules as planned work.
- Add contribution instructions and repository validation.
- Redesign the README with a local SVG cover, navigation, module status, and workflow diagram.

### Article module

- Translate all instructions, templates, references, and interface metadata into English.
- Default output to English while retaining explicitly requested Chinese editing through `humanizer-zh`.
- Preserve the Skill identifier and the then-current repository URL for existing installations.
- Retain factual verification, specified Humanizer routing, version-bound independent review, and separate publishing authorization.

## 1.0.0 - 2026-11-17

- Publish the first article-production Skill.
- Include research, writing, fact-checking, search review, language editing, independent review, and optional CMS QA.
- Include source, claim, brief, and delivery templates.
