# Cluster architecture report

This is a synthetic report. All URLs, pages and values are illustrative.

## Scope and sources

- Site and canonical origin: `https://example.com`
- Markets and languages: United States / English
- Business model: B2B and B2C
- Planning scope: commercial coffee equipment section
- Sitemap or inventory source: synthetic sitemap and page export
- Checked date: 2026-11-21
- Access limits: no live crawl, analytics, CMS or search-console access

## Inventory summary

- Existing pages: 8
- Proposed pages: 0
- Retired, redirected or noindex pages: 2
- Unknown metadata: the redirected legacy page and search utility page
- Canonical origin and URL normalization: HTTPS, no `www`, remove tracking
  parameters and fragments, preserve meaningful query parameters
- Excluded URL patterns: search, tags, authors, attachments, feeds, account and
  checkout paths
- Main limitations: no live site was audited and no vendor evidence was supplied

## Cluster overview

| Cluster | Pillar | Existing pages | Proposed gaps | Priority | Reason |
| --- | --- | --- | --- | --- | --- |
| coffee-equipment | Commercial Coffee Equipment | 7 content or product pages | no separate case study yet | high | It is the main commercial discovery path |

## Cannibalization decisions

| URL or pair | Shared intent or query | Evidence | Decision | Owner | Status |
| --- | --- | --- | --- | --- | --- |
| small-cafe guide and espresso buying guide | choose an espresso machine | overlapping titles, H1s and commercial intent | merge or differentiate before another article | content owner | confirmed |
| old coffee equipment guide | legacy equipment guide | 301 target is the commercial hub | keep redirected and remove from cluster | site owner | resolved |

## Content gaps and next pages

| Priority | Page or cluster | Reader decision | Evidence readiness | Dependency | Status |
| --- | --- | --- | --- | --- | --- |
| high | choose an espresso machine | choose a shortlist | partial | current specifications and pricing | needs evidence |
| medium | burr grinder types | understand grinder categories | available | add a pillar link | ready after link fix |
| low | commercial coffee case study | see a permitted application | missing | customer permission and measured outcome | blocked |

## Orphan pages

| URL | Page role | Inbound links | Why it matters | Proposed link or retirement |
| --- | --- | --- | --- | --- |
| https://example.com/blog/burr-grinder-types | cluster | 0 relevant in-content links | Grinder education is not reachable from the hub | Add a proposed pillar-to-cluster link |

## Internal-link plan

Use `link-plan.csv`. The proposed hub-to-grinder link removes the orphan finding;
the decision-guide-to-category link connects education to commercial discovery.
The redirected legacy guide must not receive new cluster links.

## Handoff to article production

- Next page: `https://example.com/blog/choose-espresso-machine-small-cafe`
- Cluster row: `coffee-equipment` / `cluster`
- Reader and decision: cafe owner chooses a shortlist for a small cafe
- Keyword source: AI hypothesis only; owner must validate
- Required evidence: current specifications, configuration, pricing and trial notes
- Internal links in and out: hub, product-category, grinder sibling
- Remaining blockers: duplicate selection intent and missing product evidence

## Assumptions and limits

- Proposed URLs and links are not live pages.
- Missing metadata stays unknown.
- No traffic, ranking, volume, revenue or AI-citation result is claimed.
