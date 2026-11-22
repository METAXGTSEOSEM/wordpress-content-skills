# Architecture method

## Evidence and scope

Record the sitemap or URL source, checked date, market, language, business model
and access limits. A sitemap shows URL presence, not page quality, traffic,
indexation or intent. If a page cannot be read, mark its metadata unknown rather
than inferring it from the URL.

Do not mix sites, brands, markets or languages in one architecture decision
without a recorded reason.

## URL normalization and scope

Inventory only after defining the canonical origin and normalization policy:

- use the canonical URL from the page or sitemap when it is available;
- normalize the host and scheme according to the site policy;
- remove fragments and tracking parameters used only for attribution;
- retain query parameters that change the rendered page;
- do not lowercase a case-sensitive path without evidence;
- keep one logical page per market and language;
- group translations through hreflang or a recorded market/language mapping;
- treat a product variant as a separate page only when it has a distinct,
  indexable intent and canonical URL.

Record excluded patterns and their counts: pagination, search results, tag and
author archives, attachment pages, feeds, APIs, account and checkout paths, and
other non-content URLs. Exclusion is not the same as deletion; record why the
pattern is outside the content architecture.

Keep redirected, noindex, retired and draft URLs in the inventory with their
status, but do not assign them to a normal cluster unless the record explains
the role. Follow the canonical target for normal cluster planning.

Global navigation links do not prove cluster connectivity. A page is an orphan
when no relevant in-content internal link reaches it. Record the inbound count
and the proposed link or retirement action.

## Controlled values

Use these values consistently in the CSV files:

| Field | Allowed values |
| --- | --- |
| Inventory `status` | `existing`, `draft`, `proposed`, `redirected`, `noindex`, `retired`, `unknown` |
| `page_role` | `pillar`, `cluster`, `product-category`, `product`, `comparison`, `case-study`, `faq-glossary`, `utility`, `unknown` |
| `business_value` | `high`, `medium`, `low`, `unknown` |
| `conversion_role` | `inquiry`, `purchase`, `lead-support`, `retention`, `none`, `unknown` |
| `evidence_status` | `available`, `partial`, `missing`, `unknown` |
| `orphan_status` | `not-orphan`, `orphan`, `unknown` |
| `priority` | `high`, `medium`, `low`, `unknown` |
| `cannibalization_status` | `none`, `potential`, `confirmed`, `resolved`, `unknown` |
| `link_type` | `pillar-to-cluster`, `cluster-to-pillar`, `sibling`, `guide-to-product`, `case-to-product`, `product-to-guide`, `other` |
| `link_status` | `proposed`, `live`, `missing`, `redirected`, `broken`, `unknown` |
| `target_status` | `existing`, `draft`, `proposed`, `redirected`, `noindex`, `retired`, `missing`, `unknown` |

Do not create local synonyms that break joins across inventory, cluster and link
files.

## Page roles

| Role | Job | Typical link direction |
| --- | --- | --- |
| Pillar / hub | Explain the category and route readers to sub-topics | Links to cluster pages |
| Cluster article | Answer one intent or decision | Links up to the pillar and to relevant siblings |
| Product / category | Support selection or purchase | Receives links from guides and comparisons |
| Comparison | Compare options on a like-for-like basis | Links to product, category and decision pages |
| Case study | Show a permitted, evidence-backed outcome | Links to the relevant application and product page |
| FAQ / glossary | Define a term or answer a narrow question | Links to the pillar or relevant cluster page |
| Utility / noindex | Serve a function or intentionally stay out of search | No normal cluster role; record why |

## Clustering rules

- A pillar should be useful without pretending to be every child page.
- A cluster page should solve one intent, not repeat the pillar.
- Product and category pages may sit inside a cluster, but their job is
  conversion or selection, not general education.
- Do not merge unrelated products into one cluster merely to reduce the URL
  count.
- Do not split one reader intent across several URLs to create more pages.

## Intent and keywords

One URL gets one primary intent and one focus keyword. A secondary keyword must
support the same reader decision. Keywords with no measured volume may be used
only as labeled hypotheses or explicit owner decisions.

When a keyword list is unavailable, state whether the cluster structure is based
on the sitemap, page copy, SERP research, owner priorities or a hypothesis.
Different sources support different confidence levels.

## Cannibalization decisions

Use the least destructive action that resolves the overlap:

1. Keep both only when the intents, page roles and CTAs are genuinely different.
2. Differentiate the page roles before adding more content.
3. Link the weaker page to the stronger target when the reader can still benefit.
4. Merge when two pages answer the same decision.
5. Canonicalize, noindex or retire only after checking navigation and internal
   links.

Record the owner, date and evidence for every decision.

## Priority

Prioritize by the reason the page is needed:

- high: blocks an important decision, product path or cluster; evidence is ready;
- medium: useful coverage with manageable evidence or dependency gaps;
- low: optional expansion or a page that should wait for better evidence.

Do not turn priority into a fabricated numerical SEO score. If the business
priority or evidence status is unknown, say so.

## Internal links

Plan links by reader movement, not by quota:

- discovery: pillar to cluster;
- diagnosis or education: cluster to pillar and useful sibling;
- selection: guide or comparison to product/category;
- proof: case study to application and product;
- conversion: product page back to the relevant support content.

Every link plan needs a source, target, anchor intent, link type and status.
Unpublished, redirected or missing targets stay pending or blocked.

## Review gate

The architecture plan is complete only when:

- the scope and source limitations are visible;
- canonical origin, URL normalization and exclusions are recorded;
- inventory rows have a role or unknown status;
- controlled values are used consistently;
- every page in scope has one primary intent or a recorded gap;
- duplicate and competing pages have decisions;
- the cluster map has a pillar or an explicit missing-pillar action;
- priorities and dependencies have reasons;
- the link plan is usable and verified where access exists;
- orphan pages have an inbound-link finding and an action;
- the report separates observed facts, proposals and assumptions.

This is a content-architecture plan, not a technical crawl, indexation audit,
legal review or guarantee of search performance.
