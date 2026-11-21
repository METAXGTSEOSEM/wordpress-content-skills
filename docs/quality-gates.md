# Quality gates

This page defines what the editorial states mean. `PASS` is a workflow decision,
not a ranking, publishing or legal guarantee.

## PASS

Use `PASS` only when all applicable gates are met:

| Gate | What must be true |
| --- | --- |
| Evidence | Important claims, figures, specifications and qualifications are supported, qualified or marked missing. |
| Audience | The primary reader and decision authority are named; the opening addresses a decision, not a syllabus. |
| Content type | The selected type's required sections, evidence, CTA and review gate are present. |
| Cluster | The page has one role, one primary intent and one focus keyword; the cannibalization decision is recorded. |
| Keywords | Focus and secondary terms have a source and checked date; unverified hypotheses are labeled. |
| SEO/GEO fields | Title, H1, URL, meta description and excerpt are unique and consistent; GEO elements match the body. |
| Images | The plan gives purpose, placement, caption, alt text and rights; rights are cleared or marked missing. |
| Language editing | The specified Humanizer was actually used and its coverage is recorded. |
| Independent review | A separate reviewer checked the exact edited version; self-review is not labeled independent. |
| Delivery | No internal placeholders, invented evidence, unresolved blocking findings or false completion claims remain. |

`PASS` does not mean:

- the page is published, indexed, ranked or cited by an AI service;
- the page will produce traffic, inquiries, orders or revenue;
- the product, regulation or legal classification is correct without expert review;
- the CMS, schema, canonical or tracking implementation has been tested;
- an AI-detector score or authorship result has been achieved.

## REWORK

Use `REWORK` when the work is fixable within the current assignment but one or
more gates fail. Examples:

- the opening is a training-manual introduction without a decision;
- one intent is assigned to two URLs;
- the focus keyword has no source or purpose;
- title, H1 and meta describe different pages;
- an image has no rights status;
- the selected type's required section or CTA is missing;
- an unsupported claim can be removed, qualified or replaced with evidence.

Return specific findings to the responsible role. Recheck the affected stages
after revision. Start with at most two targeted rounds, then report unresolved
evidence needs instead of polishing indefinitely.

## BLOCKED

Use `BLOCKED` when progress requires missing material, access or a separate
approval. Examples:

- central evidence, product data or source permission is missing;
- the required Humanizer is unavailable;
- no independent reviewer or review context exists;
- the owner has not decided the page role, market or focus intent;
- a safety, regulatory or legal claim needs expert review;
- a live-site check needs credentials or authorization that is not available.

Do not turn a blocked fact into a confident sentence to make the draft look
complete. Do not publish a blocked article without an explicit, recorded
exception where an exception is legitimate.

## Technical status is separate

Editorial and technical states are independent:

| Status | Meaning |
| --- | --- |
| `TECH_PASS` | Required technical checks were actually performed and passed. |
| `TECH_REWORK` | A technical check failed or needs implementation changes. |
| `TECH_NOT_CHECKED` | No suitable access, evidence or test was available. |

An editorial `PASS` with `TECH_NOT_CHECKED` is a valid delivery state for a
manuscript, but not proof that the page is ready to publish.

## What this page is not

This is an editorial acceptance guide, not a Google ranking formula, legal
opinion, accessibility audit or security review. The current policy baseline is
dated in the Skill; recheck relevant primary sources for each production run.
