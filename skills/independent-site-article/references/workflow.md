# Stages, handoffs, and acceptance criteria

These stages are editorial conventions, not a Google ranking formula. See `policy-sources.md` for primary guidance.

## Assignment

Create a project directory for each article. Keep the brief, cluster map, keyword plan, research, source and claim records, image plan, draft versions, reviews, final manuscript, and publishing record there. Do not store customer or unpublished product material in the installed Skill.

Choose the requested mode:

- New article: research the topic, agree on direction, then write.
- Revision: read the existing article and preserve useful material.
- Review only: report findings without rewriting unless requested.
- Outline only: deliver an outline and evidence, not a full manuscript.

Select one primary content type from `content-types.md` and record it in the brief. The type determines the reader's job, required sections, evidence and CTA. Do not use a fixed word count as the framework.

Confirm the primary reader role and decision authority, competitor URL or brand if supplied, existing pages or sitemap, keyword assets, and image assets. Read `audience-and-voice.md` and `cluster-and-keywords.md`.

English is the default for content and working documents. An explicit language request overrides it. Ask about missing context when it would change the work; do not require every optional brief field.

## Cluster and keyword plan

Before the outline:

1. Build the cluster map with page roles, parent pillar, sibling pages and internal-link direction.
2. Ask whether the owner has a keyword list. If yes, use it and preserve source and date.
3. If no list exists, offer DataForSEO or another authorized source. AI-generated candidates must be labeled unverified; never invent volume, difficulty or rankings.
4. Assign one primary intent and one focus keyword to the URL.
5. Check existing titles, H1s, URLs, meta descriptions and intents for cannibalization.
6. Record the action: merge, differentiate, canonical, link, noindex, retire, or keep with evidence.
7. If a recent-article style ledger is supplied, read the last five to ten rows and record the planned differences and one signature detail.

Use `cluster-map.csv` and `keyword-plan.csv`. A competitor URL is a research reference, not a template to copy.

## Research and outline

1. Check relevant official guidance and document updates. Record the date and any access limits.
2. Read the website and existing content. Decide whether to update, consolidate, or create a page. Check its cluster role and cannibalization status.
3. Research the target market and language. Record actual query conditions.
4. Distinguish exact SERP data from general search samples. Missing volume, difficulty, or rank data stays missing.
5. Read representative results and primary sources. Government, standards, forum, and video results may explain intent; do not exclude them mechanically.
6. Identify reader questions and the additional help this article can credibly provide.
7. Match the opening to the reader's decision and avoid a training-manual structure.
8. Record the anti-template difference from two or three sibling pages and from recent published articles in the style ledger.

Record what each source supports, when it was read, and its scope. Internal material needs a provider, version, and permission to disclose.

The outline connects each section to a reader question, evidence, and a useful conclusion. Apply the selected type's required sections and evidence priorities, the primary reader's decision, and the cluster role. Verify internal-link targets. Do not prescribe fixed word counts, keyword density, paragraph length, or FAQ counts.

After the outline, set a provisional content-length range and image-count plan before Draft v1. Use English words for English output and Chinese characters only for Chinese output. Record the basis. Do not set the range after drafting to fit the finished article.

## Draft v1

The writer uses the brief, content type, audience notes, cluster map, keyword plan, outline, and evidence. Put important figures, specifications, standards, comparisons, cases, captions, and commercial claims in the claim record. Match the CTA to the type, reader authority and business model.

Answer the main question before adding conditions, reasoning, and next steps. Preserve technical terms that matter to the reader.

Remove unsupported nonessential claims or narrow them to what the evidence supports. Missing evidence for a central conclusion blocks that conclusion. Do not invent first-hand experience, credentials, measurements, or customer stories.

Keep citations useful and accessible. Internal review notes do not belong in publishable prose.

Use the provisional length range as a writing budget. Complete the SEO/GEO delivery sheet and image plan. Record the actual length and explain material variance; do not use a universal word quota or "one image every N words."

## Review v1 and revise v2

Fact and search reviewers may inspect the same fixed draft in parallel. They submit findings; the writer makes the changes.

Fact review checks whether the source supports the actual wording, including units, dates, jurisdiction, model, version, sample, comparison, negation, and causality. Use supported, partially supported, conflicting, unsupported, or not applicable.

High-risk technical or safety claims need suitable evidence or expert review. A manufacturer's statement is not an independent test.

Search review checks intent, business relevance, original help, type fit, audience fit, cluster role, cannibalization, keyword mapping, structure, entity meaning, titles, summaries, links, and technical evidence. Scores and formulas cannot offset factual problems.

Record changes by issue ID: fixed, not adopted with evidence, or awaiting information. Recheck new factual claims and substantial structural changes. Close blocking issues before language editing.

## Language editing v3

Read and execute `humanizer` for English. Use `humanizer-zh` only for explicitly requested Chinese output. The project links are in the Skill entry.

If the required editor is missing, report it. Do not call an ordinary rewrite a completed Humanizer pass.

Match the author's real sample and the content type. Preserve information, citations, units, negation, scope, conditions, dates, and certainty. Do not invent detail to make prose feel specific.

Record the actual path, version or available hash, scope, and important edits. Review bilingual output separately. Do not promise detector results.

## Independent final review

Inputs: v3, v2, the brief, evidence, claim records, and prior findings. Recheck important sources rather than inheriting an earlier pass.

Verify:

- The reader's task is answered and the promised value is present.
- The selected content type's gate is met; a generic article is not substituted for the chosen type.
- The primary reader sees a decision-led opening, not a training manual.
- The anti-template fingerprint is recorded and the page is not a near-duplicate of a sibling.
- The cluster role, cannibalization decision and internal links are consistent.
- The keyword plan and SEO/GEO fields use one focus keyword and unique title/H1/URL/meta.
- The image plan has purpose, caption, alt text and rights status.
- The length range was set before drafting; actual length and any variance are recorded.
- The recent-article ledger comparison and signature detail show that the page is not a product-name swap.
- Editing did not change figures, conditions, certainty, negation, or attribution.
- Titles, metadata, captions, tables, and CTA match the manuscript.
- The specified editor was actually used and coverage limits are disclosed.
- Blocking findings are closed; no internal placeholders or invented material remain.

`PASS` requires a separate review context or another reviewer. Without delegation, a useful draft and self-review can be delivered, but the full workflow remains `BLOCKED: independent review pending`.

A same-model subagent is still AI review, not human or expert review. The final reviewer reports a decision and specific findings rather than silently rewriting and approving its own changes.

Return `REWORK` to the relevant role. Recheck affected stages after revision. Start with two targeted rounds; if central evidence is still missing, report the gap instead of continuing indefinitely.

## Freeze and deliver

Record the accepted file, version, reviewer, time, and available hash. Substantive changes invalidate the earlier final decision.

Deliver the manuscript, cluster map, keyword plan, SEO/GEO delivery sheet, image plan, source and claim records, and review results separately.

Include a length rationale, actual length, variance note, recent-article differentiation note, and an image-count/placement rationale for the specific article.

After publication, append the article to the project's `article-style-ledger.csv`
and update `similar_to` and `review_note`. Keep the ledger outside the installed
Skill.

Editorial status: `PASS`, `REWORK`, or `BLOCKED`.

Technical status: `TECH_PASS`, `TECH_REWORK`, or `TECH_NOT_CHECKED`.

Content approval does not prove technical eligibility, indexing, ranking, or AI citation.

## Optional CMS QA

Create drafts, publish, or change settings only within explicit authorization. Identify the CMS, editor, theme, and SEO plugin before changing implementation.

Check page identity, manuscript consistency, mobile readability, tables, units, citations, links, images, public response, body accessibility, canonical, index and snippet controls, and discovery paths.

Check relevant AI-appearance controls, search crawlers, and CDN/WAF behavior where required. Without account, log, or network evidence, record the limit; a successful browser visit does not prove crawler access.

Structured data must match visible facts. Check plugin output before adding markup. Do not fabricate authors, dates, ratings, or certifications.

A protected draft can be normal. Do not publish it merely to test public access.

Normal release requires editorial `PASS`, all required technical checks at `TECH_PASS`, and publishing authorization. An untested requirement remains `TECH_NOT_CHECKED`. Explicit acceptance of specific technical gaps must retain the exception and authorization record. Factual and editorial blockers are not waived this way.

When only an article is requested, stop at delivery and state that technical QA is pending.

## Optional follow-up

Do not imply monitoring or create recurring jobs without a request and available data access.

Publication, crawling, indexing, impressions, clicks, AI citations, and business outcomes are separate observations. Compare matching time windows, queries, countries, and devices.

For AI checks, record platform, time, language, question, cited URL, and evidence. One missing citation does not establish absence from an entire platform. Referral clicks do not measure all citations.

Use qualified inquiries for B2B and appropriate order or margin measures for B2C. Record actual mistakes, corrections, and evidence before updating the workflow. Do not infer an algorithm rule from one traffic change or change dates merely to imply freshness.
