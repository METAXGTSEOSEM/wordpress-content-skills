# Worked example: project management tool evaluation

This folder is a synthetic demonstration of the article workflow. The agency,
tool names and example copy are illustrative. Do not publish the sample as a
real vendor comparison or treat its placeholders as verified facts.

It shows the handoff from a short brief to a revised editorial package with an
explicit final review record:

| File | Purpose |
| --- | --- |
| `brief.md` | Input brief with audience, goal and evidence limits. |
| `sources.csv` | Source ledger, including deliberately missing evidence. |
| `claims.csv` | Claim-level checks and the evidence each claim needs. |
| `draft-v1.md` | First draft with reviewable weaknesses. |
| `review.md` | Version-specific `REWORK` decision and required changes. |
| `final.md` | Revised article after the findings were addressed. |
| `final-review.md` | Synthetic final review record and remaining limits. |
| `wordpress-fields.md` | Publishing fields and handoff notes. |
| `cluster-map.csv` | Page role, parent pillar, siblings and internal-link direction. |
| `keyword-plan.csv` | Focus, secondary and supporting terms with provenance. |
| `image-plan.csv` | Image roles, placement, captions, alt text and rights. |
| `seo-geo-delivery.md` | Search fields, GEO elements, length and image rationale. |

## What the example demonstrates

- The draft is not accepted just because it reads well.
- The brief selects a selection guide, so the outline is organized around buyer criteria rather than a generic definition.
- Unsupported popularity, pricing and comparison claims are removed.
- Missing trial evidence stays visibly missing instead of being invented.
- SEO and AI-search guidance does not override factual accuracy.
- The cluster map shows the page's role and internal links before drafting.
- The SEO/GEO sheet recommends a length and image count with a reason, not a fixed quota.
- The final review record shows the decision fields and the limits of a synthetic
  demonstration.
- The final package includes fields a WordPress editor can use directly.

## Run the same workflow

```text
Use independent-site-article.

Use the example brief at:
examples/project-management-tool-article/brief.md

Produce a new article package. Keep missing trial and pricing evidence marked
as missing. Do not invent vendor rankings, prices, customer counts or results.
Before drafting, show the research plan and the questions that require the
buyer or vendor to answer.
```

The sample is intentionally generic. A real project must use current vendor
documentation, trial notes, approved pricing and the site owner's requirements.
