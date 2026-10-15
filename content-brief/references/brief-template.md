# Brief Output Template

Write to `briefs/{keyword-slug}.md`. Fill every field. A field you can't fill is a signal, not a formatting problem — say what's missing rather than writing filler.

In batch mode, if the edge gate failed, add `STATUS: BLOCKED — no edge` as the first line of the file.

Sections run in this order. Sections marked *(roundups and comparisons)* apply only to those page types; leave them out for other types and say nothing about them.

---

```markdown
# Brief: {keyword}

> STATUS: READY | BLOCKED — no edge
> Created: {date}
> Target URL: {proposed slug}

## Brief at a Glance

{2 to 3 sentences: the page type, who it is for, how many entries or sections, and what it does that the top results don't. A stakeholder should be able to approve or reject the brief from this paragraph.}

## Core Fields

| Field | Value |
|---|---|
| **Keyword** | {primary keyword} |
| **Core question** | {the one question this page answers} |
| **Search intent** | {one primary: informational | commercial investigation | transactional | navigational. Add a secondary intent only if the SERP is mixed} |
| **SERP context** | {country, language, page type: blog post | help article | commercial page | comparison} |
| **Reader** | {specific person — role + context, not a segment} |
| **Decision the reader is making** | {what they are trying to decide or do when they land here} |
| **Reader outcome** | {what they understand or can do after reading} |
| **Funnel stage** | ToFu | MoFu | BoFu |
| **Content type** | Ideas listicle | Commercial roundup | Ranked list | Explainer — see `content-types.md` |
| **Edge** | {the one thing no top-5 result does} |
| **CTA** | {one action + URL} |
| **EEAT signal** | {the specific quote, dataset, or credential this page carries} |
| **Who / How / Why** | {Who: the named author (or `[NEEDS: author]`). How: how the page is made, including any AI assistance and who reviews it. Why: the reader job the page exists to do, beyond attracting search traffic} |
| **SME / reviewer** | {name and what they confirm, or none} |
| **Voice** | {POV — we / you / third person · tone · banned habits} |
| **Format** | Text only | Text + images — visuals listed below |
| **Word count** | {target range, with the per-section budget below} |
| **Relationship to existing pages** | {pillar, landing page or sibling posts: which phrase each page owns, and how they link. "None" if there are none} |
| **Cannibalization** | {none found | resolved: {how}} |
| **Success metric and refresh** | {what this page is judged on · update trigger · owner · next review date} |

## Keywords

| Tier | Keywords | Placement |
|---|---|---|
| **Primary** | {1 keyword} | H1, first paragraph, one H2, meta title, URL |
| **Secondary** | {2–5, deduped} | Second intro paragraph, H2/H3s where they fit naturally, meta description |
| **Related** | {semantic / LSI terms} | Body, where natural. Never forced. |

*Placement is a plan, not a quota. A keyword that doesn't fit a sentence naturally is dropped from the sentence, not jammed into it.*

### Keyword data

Name the tool and the date the numbers came from. If no keyword tool is connected, leave the volume columns as "no data" rather than quoting numbers you can't source.

| Keyword | Intent | Volume / month | KD % | CPC (USD) | SERP features | Read |
|---|---|---|---|---|---|---|
| {keyword} | Informational | {n or "no data"} | {n} | {n} | {AI Overview, People Also Ask, sitelinks, ...} | {what the term tells you: primary, secondary, owned by another page, navigational so don't target it} |

*Navigational terms (a brand name, a login) are not targets. They show the size of the audience, so say so in the Read column.*

**What this changes** — 2 to 4 bullets on what the data does to the brief. For example:

- A People Also Ask box appears → copy its real questions from a live search and swap them in for any FAQ that doesn't match.
- An AI Overview appears → the answer block and the extractable table are what get cited, so keep both tight.
- Volumes too small to measure → say what the page is judged on instead (citations, demo requests, assists), because it is not a traffic play.
- Rankings depend more on inbound links than backlinks → the inbound linking plan matters more than outreach.

### Terminology

Exact product names, spellings and category labels the writer must use, and terms to avoid. AI systems and readers match strings, so inconsistent names weaken both. `[NEEDS: terminology]` if none was given.

## Search Snippet

Two options. Mark one **recommended** and give the reason in one line (for example, it matches the format of a sibling post that already ranks).

| | Option A (recommended) | Option B |
|---|---|---|
| **H1** | | |
| **Meta title** (≤ 60 characters) | | |
| **Meta description** (≤ 155 characters — drawn from the answer block, not written separately) | | |
| **URL** | | |

*A number in any of these ("12 ideas," "Top 10") must equal the item count in the structure below. A year ("2026," "2025 Update") is a promise the data must keep — see `content-types.md`. Keep the visible last-updated date, and re-check every price before publishing.*

## The Answer Block (Intro)

*Sits directly under the H1. Two paragraphs, ~120–160 words. This is what AI Overviews extract.*

**The question it answers:** {one question, in one sentence}

**Paragraph 1** — 40–60 words. Answers the core question directly. Contains the primary keyword.

{Write it. Not a description of it.}

**Paragraph 2** — 80–100 words. What the reader gets from the page; previews the structure (for a list, the count and the categories). Works in the secondary keywords naturally.

{Write it.}

*State the word count of each paragraph. Add no warm-up line above the block.*

## Structure

*Outline uses H2s for sections and H3s for list items or sub-points. For lists, numbering runs continuously across the page.*

### Outline at a glance

| # | H2 | Words | Direction | Evidence and citations |
|---|---|---|---|---|
| — | Answer block (no heading) | {n} | Use the text above exactly. | None needed |
| 1 | | | | |

**Word budget check:** {section budgets added up} = {total}, against a {target} target. If the draft runs long, say which section to trim (the competitor entries, never the section carrying the edge).

**Count check:** the title, H1, answer block and the list H2 all say {n}, and the outline delivers exactly {n} items.

*This table is the one-glance view. The per-section blocks below carry the full spec for any section that needs more than a table cell.*

### H2: {heading}
- **Answers:** {which search question}
- **Direction:** {what the writer must include — name the specific items, e.g. "cover A, B, and C"; "cover best practices" is not direction}
- **Angle:** {one sentence — the point this section makes}
- **Word budget:** {n}
- **Stands alone:** {yes — confirm the section needs no prior context}
- **Citation:** {real URL + the claim it supports} | `[CITE: needed — {claim}]`

*(For list items, add:)*
- **Example:** {org + what they did + source URL} | `[EXAMPLE: needed — {item}]`
- **Not reported:** {what the source doesn't say — attendance, outcomes, pricing}

### H2: {heading}
- **Answers:**
- **Direction:**
- **Angle:**
- **Word budget:**
- **Stands alone:**
- **Citation:**

*(repeat — target 4–7 H2s; H3 items nested underneath)*

### Fact bank

*5 to 8 claims the page can cite. Each is a self-contained, checkable statement, so a writer has real material and an AI summary has something to quote.*

| Claim | Exact figure or statement | Source name | Year | URL | Used in |
|---|---|---|---|---|---|
| | | | | | {H2} |

*A claim missing its source, year or exact figure is `[CITE: needed — {claim}]`, not a row.*

## Entry Research *(roundups and comparisons)*

*One verified-facts row per entry. Method and rules in `entry-research.md`.*

**What readers are replacing** *(for "alternatives to {incumbent}" pages)*: {the incumbent's offer and pricing in a neutral tone, from its own pages, used once in the at-a-glance intro}.

| # | Platform | Best for | Verified facts to use | Limitation | Pricing (checked {date}) |
|---|---|---|---|---|---|
| 1 | | | | | |

**Limitations marked (inference)** come from what the vendor's pages leave out. Write them as "not mentioned on its site".

**Re-check before publishing:** {every cell resting on an unconfirmed page or figure}

### H2: When {incumbent} is still the right choice *(alternatives pages)*

- **Direction:** one intro sentence, then 4 to 5 "Stay with {incumbent} if you..." bullets, each tied to a page of the incumbent's. Close with one sentence on when a specialist fits better. Neutral tone, no brand pitch.
- **Angle:** admitting when a competitor fits makes the rest of the page believable.
- **Word budget:** {n}
- **Stands alone:** yes

### H2: How {Brand} helps with {topic}

*Near the end, before FAQs. Rules in `brand-integration.md`.*

- **The argument:** {one sentence — why the product is the answer to the problems this page raised}
- **Bridge:** {the problem this page raised → the capability}
- **Problem to solution mapping:** {3 to 5 problems in the order the page raised them, each paired with a capability and where the page discussed it}
- **Capabilities:** {5–8 bullets, each tied to a problem earlier on the page}
- **Proof point:** {named customer + exact figure + case-study URL} | none — cut
- **Ground-truth URLs:** {the product pages every claim above traces to}
- **Unverified claims:** {`[VERIFY: …]` list, or none}
- **Disclosure** *(required when the page lists the brand)*: {the exact line, placed under the at-a-glance table, for example: "{Brand} publishes this guide and is listed first. Every entry, ours included, lists its limitations, and pricing comes from each vendor's own site as of {month year}."}
- **Don't claim:** {a list: unpublished numbers, features the product team hasn't confirmed, outcomes with no baseline, anything legal or compliance has restricted}
- **CTA:** {one action + URL}

### H2: FAQs

*3–5 questions. Each answer 2–3 sentences, 40–60 words, first sentence answers. FAQs must not merely repeat an H2 — if they do, cut them or cut the H2.*

| Question | Answer direction | Source |
|---|---|---|
| | | |

**About the People Also Ask box:** {where the questions came from and the capture date; which questions were used and which were dropped as off-topic, and why}

## Top 5 Coverage Map

| # | URL | Angle | Depth | What it misses |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Gap this page exploits:** {one sentence}

### SERP coverage and cannibalization

*Include your own pages that rank for the keyword or a near-synonym, with Search Console figures (position, impressions, date range) when it is connected.*

| Result | What it covers | Gap |
|---|---|---|
| {competitor or own page} | | |

**Cannibalization decision:** {update the existing page | brief a different angle and link the two | proceed anyway}. State which phrase each page owns, which anchor text is off limits on this page, and the **fallback**: if Search Console later shows both pages on page 1 for the same query, which one is merged into the other and redirected with a 301.

### AI answer snapshot

*What AI assistants currently say for the primary query. Record the date.*

| Assistant | Answer in one line | Sources it cites | Where it falls short |
|---|---|---|---|
| Google AI Overview / ChatGPT / Perplexity | | | |

If no snapshot was possible, write `[NEEDS: AI answer snapshot]` and do not infer one.

## Reference & Style

**Sources to draw on** — real URLs opened, with the section each supports.

| Source | What it supports | Section |
|---|---|---|

**Style reference** — {URL · qualities to imitate · what not to reuse}. Omit if none.

## Visuals

*Only if Format is Text + images.*

| Visual | Where | What it shows | Alt text intent |
|---|---|---|---|

## Internal Linking

*Specify both directions. If you don't know the site well enough to name real URLs, mark it `[NEEDS: site audit]` rather than inventing paths.*

**This page links out to:**
| Where in the post | Anchor text | Target page | Why (include Search Console position and impressions when known) |
|---|---|---|---|

**Rules:** no links in the H1, headings or the first sentence of the answer block; at most one link per paragraph; link each URL once; never use an anchor that another page owns.

**These pages should link in:**
| Source page | Section to edit | Exact existing text | Edit (the new sentence and its anchor text) | Owner |
|---|---|---|---|---|

*Quote the existing sentence exactly so the person making the edit can find it. After the draft exists, run the `internal-linking` skill to place the outbound links as real hyperlinks.*

## Schema

- **Types:** {Article, FAQPage, HowTo, ItemList — pick what applies}
- **FAQ entries:** {which H2s or FAQs become FAQPage questions}
- **ItemList:** {for roundups: the items in published order, names matching the H3 titles, each pointing to its on-page anchor}
- **Notes:** {author markup, dates, anything non-obvious}

Hand to the `blog-schema` skill for implementation.

---

## Pre-Publish Check

Run `pre-publish-check` on the finished draft. All five must pass.

1. [ ] First 150 words answer the core question directly
2. [ ] Every H2 maps to a real search question
3. [ ] Every section stands alone out of context
4. [ ] One **verified** cited data point per section
5. [ ] A human gets something an AI summary doesn't

**All YES → publish. Any NO → fix first.**

### Brief-specific checks

- [ ] The answer block is the first text under the H1, word for word, with no warm-up line above it
- [ ] The number in the title, H1, answer block and list H2 matches the item count
- [ ] Every entry, the brand's included, has a limitation *(roundups)*
- [ ] Every price is re-checked against the vendor's page, with "as of" month and year *(roundups)*
- [ ] The disclosure line sits under the at-a-glance table *(roundups that list the brand)*
- [ ] No claim from the Don't-claim list appears
- [ ] No heading or anchor uses a phrase another page owns
- [ ] Outbound links are placed, one per paragraph at most, none in headings
- [ ] One CTA, matched to funnel stage
- [ ] Visible last-updated date, and a review date set with an owner

### Open items

*Every `[VERIFY]`, `[CITE]`, `[EXAMPLE]` and `[NEEDS]` slot in the brief, listed so none ships by accident.*

- [ ] {item}

## Sources

*Pages actually opened, with the date, and the data sources used.*

- {URL or source name, date}
```

---

## Field Notes

**Reader** — "Ops lead at a 30-person DTC brand, two staff, no dedicated data person" is a reader. "E-commerce professionals" is a segment. Segments produce generic pages.

**Funnel stage** — sets what the CTA can be. See the table in `brand-integration.md`.

**CTA** — one. A page with three CTAs has none. Match the CTA to where the reader actually is: a top-of-funnel definitional query does not convert to a demo, and asking for one signals you didn't think about it.

**EEAT signal** — the concrete artifact that proves a human with real experience wrote this: a named customer quote, a proprietary number, a practitioner credential, a screenshot of the actual thing. "We have expertise in this area" is not an EEAT signal.

**Who / How / Why** — Google's people-first guidance asks who created the content, how it was made, and why it exists. Name a real author or mark `[NEEDS: author]`; never invent one. If AI helped produce the page, say how and who reviewed it. The Why is the reader's job, not "to rank".

**Search intent** — pick one primary intent. If the SERP is mixed, note a secondary intent and serve it in an FAQ or a short section, not by splitting the page. Intent sets the H2 order and the CTA.

**Decision and outcome** — a page with a stated decision ("which platform should we move to?") and a stated outcome ("can name the two that fit their course type") has a job. A page with only a topic does not.

**Voice** — first person plural means the writer speaks as the company. Every "we built / we've seen" claim has to be true. See `brand-integration.md`.

**Word count** — derive it from the top-5 median, then adjust for the edge. Don't pad to beat a competitor's length; length is not the ranking factor people assume it is, and a padded page fails Check 3 in the audit. Then divide it: the per-section budgets must sum to the target, and an item that gets under ~60 words can't carry an example and a takeaway. Cut items or raise the target.

**Keywords** — dedupe the cluster before you place it. The same phrase listed twice in the input is a signal the list was pasted together, not chosen.

**Meta description** — build it from the answer block. A description written separately from the page tends to promise something the page doesn't deliver.

**Fact bank** — material for the writer, not decoration. Five to eight claims, each with source, year and exact figure. A brief with no verifiable claims leaves the writer to fill the gap, and that is where invented statistics come from.

**Relationship to existing pages** — when a pillar, landing page or sibling post exists for a nearby phrase, say which phrase each page owns, and ban the other page's phrase from this page's headings and anchors. Decide the fallback now (which page merges into which, with a 301) so the answer exists when Search Console shows both ranking.

**Success metric and refresh** — a page with no metric and no owner goes stale. Name what the page is judged on, what event triggers an update (a pricing change, a product release, a changed SERP), who owns it, and a review date. Pick a cadence that matches how fast the topic moves. Pricing and feature pages age quickly.

**Keep it usable** — a template nobody uses fails. If a field goes unused across several briefs, sharpen it or drop it for that page type, and say why in one line.
