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
| **Edge** | {the one thing no top-5 result does} |
| **CTA** | {one action, not three} |
| **EEAT signal** | {the specific quote, dataset, or credential this page carries} |
| **Word count** | {target range} |
| **Cannibalization** | {none found | resolved: {how}} |

## The Answer Block

*Sits directly under the H1. 100–150 words. This is what AI Overviews extract.*

{Write the actual block here. Not a description of it.}

## Structure

### H2: {heading}
- **Answers:** {which search question}
- **Covers:** {2–3 bullets of substance}
- **Stands alone:** {yes — confirm the section needs no prior context}
- **Citation:** {real URL + the claim it supports} | `[CITE: needed — {claim}]`

### H2: {heading}
- **Answers:**
- **Covers:**
- **Stands alone:**
- **Citation:**

*(repeat — target 4–7)*

## Top 5 Coverage Map

| # | URL | Angle | Depth | What it misses |
|---|---|---|---|---|
| 1 | | | | |
| 2 | | | | |
| 3 | | | | |
| 4 | | | | |
| 5 | | | | |

**Gap this page exploits:** {one sentence}

## Internal Linking

**This page links out to:**
| Target page | Anchor text | Why |
|---|---|---|

**These pages should link in:**
| Source page | Anchor text | Section to edit |
|---|---|---|

## Schema

- **Types:** {Article, FAQPage, HowTo — pick what applies}
- **FAQ entries:** {which H2s become FAQPage questions}
- **Notes:** {author markup, dates, anything non-obvious}

Hand to the `schema` skill for implementation.

## Sources Available

*Real, verified URLs the writer can draw on. Do not list a source you have not opened.*

| Source | What it supports |
|---|---|

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

**CTA** — one. A page with three CTAs has none. Match the CTA to where the reader actually is: a top-of-funnel definitional query does not convert to a demo, and asking for one signals you didn't think about it.

**EEAT signal** — the concrete artifact that proves a human with real experience wrote this: a named customer quote, a proprietary number, a practitioner credential, a screenshot of the actual thing. "We have expertise in this area" is not an EEAT signal.

**Word count** — derive it from the top-5 median, then adjust for the edge. Don't pad to beat a competitor's length; length is not the ranking factor people assume it is, and a padded page fails Check 3 in the audit.
