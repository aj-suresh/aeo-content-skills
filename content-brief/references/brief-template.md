# Brief Output Template

Write to `briefs/{keyword-slug}.md`. Fill every field. A field you can't fill is a signal, not a formatting problem — say what's missing rather than writing filler.

In batch mode, if the edge gate failed, add `STATUS: BLOCKED — no edge` as the first line of the file.

---

```markdown
# Brief: {keyword}

> STATUS: READY | BLOCKED — no edge
> Created: {date}
> Target URL: {proposed slug}

## Core Fields

| Field | Value |
|---|---|
| **Keyword** | {primary keyword} |
| **Core question** | {the one question this page answers} |
| **Reader** | {specific person — role + context, not a segment} |
| **Funnel stage** | ToFu | MoFu | BoFu |
| **Content type** | Ideas listicle | Commercial roundup | Ranked list | Explainer — see `content-types.md` |
| **Edge** | {the one thing no top-5 result does} |
| **CTA** | {one action + URL} |
| **EEAT signal** | {the specific quote, dataset, or credential this page carries} |
| **Voice** | {POV — we / you / third person · tone · banned habits} |
| **Format** | Text only | Text + images — visuals listed below |
| **Word count** | {target range, with the per-section budget below} |
| **Cannibalization** | {none found | resolved: {how}} |

## Keywords

| Tier | Keywords | Placement |
|---|---|---|
| **Primary** | {1 keyword} | H1, first paragraph, one H2, meta title, URL |
| **Secondary** | {2–5, deduped} | Second intro paragraph, H2/H3s where they fit naturally, meta description |
| **Related** | {semantic / LSI terms} | Body, where natural. Never forced. |

*Placement is a plan, not a quota. A keyword that doesn't fit a sentence naturally is dropped from the sentence, not jammed into it.*

## Search Snippet

**H1 options** (2)
1. 
2. 

**Meta title options** (2, ≤ 60 characters)
1. 
2. 

**Meta description options** (2, ≤ 155 characters — drawn from the answer block, not written separately)
1. 
2. 

*A number in any of these ("12 ideas," "Top 10") must equal the item count in the structure below. A year ("2026," "2025 Update") is a promise the data must keep — see `content-types.md`.*

## The Answer Block (Intro)

*Sits directly under the H1. Two paragraphs, ~120–160 words. This is what AI Overviews extract.*

**Paragraph 1** — 40–60 words. Answers the core question directly. Contains the primary keyword.

{Write it. Not a description of it.}

**Paragraph 2** — 80–100 words. What the reader gets from the page; previews the structure (for a list, the count and the categories). Works in the secondary keywords naturally.

{Write it.}

## Structure

*Outline uses H2s for sections and H3s for list items or sub-points. For lists, numbering runs continuously across the page.*

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

### H2: How {Brand} helps with {topic}

*Near the end, before FAQs. Rules in `brand-integration.md`.*

- **Bridge:** {the problem this page raised → the capability}
- **Capabilities:** {5–8 bullets, each tied to a problem earlier on the page}
- **Proof point:** {named customer + exact figure + case-study URL} | none — cut
- **Ground-truth URLs:** {the product pages every claim above traces to}
- **Unverified claims:** {`[VERIFY: …]` list, or none}
- **CTA:** {one action + URL}

### H2: FAQs

*3–5 questions. Each answer 2–3 sentences, 40–60 words, first sentence answers. FAQs must not merely repeat an H2 — if they do, cut them or cut the H2.*

| Question | Answer direction | Source |
|---|---|---|
| | | |

## Top 5 Coverage Map

| # | URL | Angle | Depth | What it misses |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Gap this page exploits:** {one sentence}

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

**This page links out to:**
| Target page | Anchor text | Why |
|---|---|---|

**These pages should link in:**
| Source page | Anchor text | Section to edit |
|---|---|---|

## Schema

- **Types:** {Article, FAQPage, HowTo, ItemList — pick what applies}
- **FAQ entries:** {which H2s or FAQs become FAQPage questions}
- **Notes:** {author markup, dates, anything non-obvious}

Hand to the `schema` skill for implementation.

---

## Pre-Publish Check

Run `pre-publish-check` on the finished draft. All five must pass.

1. [ ] First 150 words answer the core question directly
2. [ ] Every H2 maps to a real search question
3. [ ] Every section stands alone out of context
4. [ ] One **verified** cited data point per section
5. [ ] A human gets something an AI summary doesn't

**All YES → publish. Any NO → fix first.**
```

---

## Field Notes

**Reader** — "Ops lead at a 30-person DTC brand, two staff, no dedicated data person" is a reader. "E-commerce professionals" is a segment. Segments produce generic pages.

**Funnel stage** — sets what the CTA can be. See the table in `brand-integration.md`.

**CTA** — one. A page with three CTAs has none. Match the CTA to where the reader actually is: a top-of-funnel definitional query does not convert to a demo, and asking for one signals you didn't think about it.

**EEAT signal** — the concrete artifact that proves a human with real experience wrote this: a named customer quote, a proprietary number, a practitioner credential, a screenshot of the actual thing. "We have expertise in this area" is not an EEAT signal.

**Voice** — first person plural means the writer speaks as the company. Every "we built / we've seen" claim has to be true. See `brand-integration.md`.

**Word count** — derive it from the top-5 median, then adjust for the edge. Don't pad to beat a competitor's length; length is not the ranking factor people assume it is, and a padded page fails Check 3 in the audit. Then divide it: the per-section budgets must sum to the target, and an item that gets under ~60 words can't carry an example and a takeaway. Cut items or raise the target.

**Keywords** — dedupe the cluster before you place it. The same phrase listed twice in the input is a signal the list was pasted together, not chosen.

**Meta description** — build it from the answer block. A description written separately from the page tends to promise something the page doesn't deliver.
