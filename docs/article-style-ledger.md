# Recent-article style ledger

Use one ledger per site or content cluster. It is a rolling memory of the last
published articles, not a batch-writing plan and not a replacement for the
cluster map.

Keep the ledger in the project workspace. Do not store live URLs, customer data
or unpublished material in the installed Skill.

## Create the ledger

Copy the header from
`skills/independent-site-article/assets/article-style-ledger.csv` and add one row
after publication:

```text
date,article_id,url,content_type,reader,title_pattern,opening_move,first_three_h2,proof_type,cta,signature_detail,similar_to,review_note
```

Use the ledger to compare the next article with the last five to ten published
articles, especially the last two or three.

## Before writing

Read the recent rows and add these fields to the brief:

- recent articles reviewed;
- planned differences in opening, first H2 sections, proof, CTA or format;
- one signature detail that belongs only to this article;
- any similarity intentionally kept and the reason.

The signature detail must be concrete: a scenario, constraint, regulation,
calculation, failure mode, decision table or evidence set. "High quality" or
"practical advice" is not a signature detail.

## Before final review

Compare the new article with the recent rows:

- Would the article still work if only the product name and keyword changed?
- Are the opening move and first two or three H2 sections the same?
- Is the proof type the same: test, specification, regulation, price, case,
  calculation or interview?
- Is the CTA doing the same job?
- Are the paragraph rhythm, table/FAQ pattern or repeated phrases noticeably
  similar?

If the same product-swap test passes and the opening, early structure, proof and
CTA all repeat, return `REWORK` unless the reader's task genuinely requires the
same structure and the reason is recorded.

## After publication

Append the published article to the ledger and update `similar_to` and
`review_note`. Keep only the recent history needed for comparison; the ledger is
not an analytics report.
