# Cluster architecture worked example

This is a synthetic example for the `cluster-architecture` workflow. The site,
URLs and business details are fictional. It does not contain live traffic,
keyword volume, rankings or customer data.

It shows how a small commercial-equipment site can be normalized, clustered,
checked for cannibalization, audited for orphan pages and handed to article
production one page at a time.

## Files

| File | Purpose |
| --- | --- |
| `architecture-brief.md` | Scope, sources, normalization rules and limits |
| `site-inventory.csv` | One row per known or proposed URL |
| `cluster-map.csv` | Pillar and cluster roles, intent, priority and cannibalization |
| `link-plan.csv` | Existing and proposed internal links |
| `architecture-report.md` | Summary, gaps, orphan pages, priorities and handoff |

## What to notice

- The sitemap is synthetic and the checked date is explicit.
- Redirected and noindex URLs stay in the inventory but do not receive normal
  cluster roles.
- The grinder article is an orphan until the proposed pillar link is implemented.
- The duplicate buying guide has a confirmed cannibalization decision rather
  than another keyword target.
- Priority has a reason; it is not a fabricated numerical SEO score.

## Use the example

Copy the CSV headers into a project workspace and replace the synthetic rows
with the user's supplied sitemap or URL list. Do not publish the fictional page
titles, URLs or claims as real site data.
