# FAQ

## Is this a WordPress plugin?

No. It is a set of agent instructions and templates. It produces a manuscript
and publishing fields; it does not install into WordPress.

## What if I do not know which content type to use?

Describe what the reader must decide or do. The Skill selects one of eight
primary types, records the assumption and uses the matching outline, evidence
and CTA. If two types compete, it chooses the first decision and treats the
other as a follow-up rather than blending everything into one page.

## Does it publish automatically?

No. Publishing, scheduling, CMS writes and live-site changes require separate
authorization and a human review.

## Does it need an API key?

No specific paid API is required. Optional research tools and the external
Humanizer Skill have their own setup and terms.

## Does it guarantee rankings, traffic or AI citations?

No. It supports research, structure, evidence checks and review. It cannot
guarantee indexing, rankings, traffic, conversions or citation by an AI search
service.

## Can it write Chinese?

Yes, when Chinese output is explicitly requested. The workflow then uses
`humanizer-zh` for language editing. English is the default.

## Which SEO plugin does it support?

The output is plugin-agnostic. Map the fields to Yoast SEO, Rank Math or the
site's existing setup. Plugin labels and behavior vary by version.

## What happens when product data is missing?

The workflow marks it as missing or asks for it. It must not invent product
specifications, certifications, prices, lead times, warranties or test results.

## Can it help if I do not know the product well?

Yes, at the level of structure and evidence. It turns an incomplete brief into
questions, missing-evidence records and a draft plan. It does not replace the
product owner, engineer or legal reviewer, and it must not fill gaps with
plausible-sounding specifications.

## Can it help with topic clusters?

It builds a cluster map for the assigned topic: page role, parent pillar,
sibling pages, one intent and focus keyword per URL, a cannibalization decision
and internal links in both directions. A full site-wide architecture audit is a
separate scope; do not describe one article as a complete site strategy.

## Will it remove the AI feel from a draft?

The workflow routes the manuscript through the specified Humanizer and then an
independent review. That can remove generic phrasing and repetition, but it does
not guarantee a particular AI-detector score, authorship result or editorial
quality without human review.

## Will every article look the same?

Not if you provide recent articles or the style ledger. The Skill compares the
new brief and final copy with the last five to ten published rows, especially
the last two or three. It records the opening, early H2 order, proof type, CTA
and one signature detail, then rejects a product-name swap even when the prose
reads naturally. It does not automatically remember earlier articles without
that input.

## Can it write differently for procurement, owners and engineers?

Yes. The audience and voice reference calibrates the opening, evidence depth and
CTA to the primary reader's role and decision authority. A procurement lead
should not receive the same opening as an owner or an engineer. If the brief
names several readers, the Skill chooses one primary reader and marks the
secondary audience separately.

## Where does keyword data come from?

The Skill first asks whether you already have a keyword list. If you do, it uses
that list with its source and date. If not, it can use DataForSEO or another
authorized source. AI-generated keywords may be proposed only as clearly labeled
unverified candidates; they are never presented as measured volume or
difficulty.

## How do you prevent keyword cannibalization?

It builds a cluster map before writing, assigns one primary intent and one focus
keyword to each URL, and checks existing titles, H1s, URLs, meta descriptions and
intents. If two pages compete, it records a decision: merge, differentiate,
canonicalize, link, noindex, retire, or keep with evidence.

## How many words and images will an article have?

There is no universal quota. English lengths are measured in words; Chinese
lengths are measured in characters. The Skill sets a provisional range after the
outline and before drafting, based on the type, reader decision, required
evidence and current results. It then records the basis, actual length and any
variance. Images are planned by role (product, factory, structure, detail,
application, chart) with caption, alt text and rights status.

## Will it copy a competitor page?

No. A competitor URL or brand is reference material for understanding the market
and reader expectations. The Skill does not copy its text, structure, images or
claims, and the anti-template check requires the article to differ from sibling
pages.

## Can I use it for Shopify?

The article workflow can produce general content, but the field pack is
WordPress-oriented. A Shopify implementation needs its own field mapping and
theme checks.

## How do I update an installed Skill?

Read the changelog, replace the complete Skill folder, and keep the same Skill
identifier. Do not copy only `SKILL.md`; the references and templates are part
of the workflow.

## Who owns the generated content?

The repository license covers the Skill material. The output is subject to your
own agreements, the rights of any sources or images you use, and the terms of
the tools you run. This is not legal advice.
