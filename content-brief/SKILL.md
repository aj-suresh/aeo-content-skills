---
name: content-brief
description: "When the user wants a content brief for a keyword or topic — a spec a writer or Claude can execute against. Also use when the user mentions 'content brief,' 'write me a brief,' 'brief for this keyword,' 'AEO brief,' 'brief this topic,' 'what should this article cover,' 'outline this post,' 'H2 structure,' 'PAA questions,' 'people also ask,' 'answer block,' 'AI Overviews brief,' 'content spec,' or 'batch briefs.' Produces a brief engineered to rank on Google AND get cited by AI Overviews and LLMs. For auditing a finished draft against the brief, see pre-publish-check. For deciding which topics to brief in the first place, see content-strategy. For broad AI search strategy, see ai-seo."
metadata:
  version: 1.0.0
---

# Content Brief for AI-Era Search

You produce content briefs that survive contact with two different readers: Google's ranking systems and the LLMs that summarize the page without sending a click. A brief that only satisfies one of them is a wasted draft.

Your output is a **spec, not an essay**. Someone should be able to hand the brief to a writer or to Claude and get back a publishable draft without asking follow-up questions.

## The Non-Negotiable

**A brief without an edge is not a brief.** If the page has nothing the top 5 results lack — no original data, no specific ICP the others ignore, no named framework, no deeper subtopic — then the page has no reason to exist and the brief is not ready. This is enforced at Step 6 and it is the single most important step in this skill. Do not soften it.

---

## Before Starting

### 1. Get company context

The brief needs four things about the company. **Ask for whatever you don't have — never guess.** A wrong ICP silently degrades every downstream step.

| Need | Why |
|---|---|
| **Product, one sentence** | Grounds the answer block and CTA |
| **Reader** — role + context, specific enough to change the advice | Feeds the reader field and the ICP edge |
| **Competitors** likely to rank for this keyword | Seeds the coverage map |
| **Proprietary assets** — data, frameworks, quotable customers | Feeds the edge gate at Step 6 |

**Shortcut:** if a product marketing context file exists, read it instead of asking. Check in this order and use the first one found:

1. `.agents/product-marketing.md` (working directory)
2. `.claude/product-marketing.md`
3. `product-marketing-context.md`
4. `~/.agents/product-marketing.md` (global fallback)

This is a convention shared with other skills in the agentskills ecosystem. It's an optimization, not a requirement — the skill works fine without it by asking.

**Treat a stub as absent.** If the file exists but its fields are unfilled — `TODO`, `STATUS: STUB`, placeholder text, empty headings — do not use it. Ask for the fields inline instead. A file full of `TODO` is worse than no file: it silently produces a brief written for nobody.

If you asked inline and the user seems likely to run this again, offer **once**: *"Want me to save this so I stop asking?"* Drop it if they decline.

### 2. Detect mode

| Input | Mode |
|---|---|
| One keyword | **Single** — full pipeline, hard stop at the edge gate |
| A list, a file of keywords, or "batch" | **Batch** — one confirmation for the whole set, edge failures marked not halted |

### 3. Confirm the output location

Default: `briefs/{keyword-slug}.md` relative to the working directory. Create the folder if missing. Say where you're writing before you write.

---

## The Pipeline

Run these in order. Do not skip steps 1 and 3 to save time — they are where the cheap failures get caught.

### Step 1 — Cannibalization check

Before researching anyone else, check whether the user already covers this.

- Search for existing pages on their domain targeting this keyword or a near-synonym.
- If a page already exists, stop and present the choice:

> You already have [URL] targeting this. Three options: **update** that page (usually the right call — it has age and links), **brief a genuinely different angle** and internally link the two, or **proceed anyway** and accept the two pages will compete.

Do not proceed past this without an answer. Two pages fighting over one query is the most common self-inflicted SEO wound and it is invisible until months later.

### Step 2 — SERP research

Run the research described in [references/serp-research.md](references/serp-research.md). You need two things out of it:

1. **The question set** — what people also ask around this keyword
2. **The top-5 coverage map** — what each ranking page actually covers, so Step 6 has something to be a gap against

**State the limitation plainly when you present results:** web search approximates the People Also Ask box; it does not scrape the literal Google widget. The confirmation gate exists so the user can paste in the real PAA questions when the keyword matters enough.

### Step 3 — Confirmation gate

Show your work and stop.

**Single mode** — present:
- The candidate question set, deduped, with your intent read on each
- The top-5 coverage table
- The gaps you think are real

Then ask: *"Correct anything before I build the structure — especially if you have the real PAA box in front of you."*

**Batch mode** — present one table, all keywords, one approval:

| Keyword | Core question | Candidate H2s | Cannibalization risk |
|---|---|---|---|

Get one approval or one round of edits for the whole set. Do not ask per keyword.

### Step 4 — The answer block

The single highest-leverage 150 words on the page.

- **One question.** What is the one question this page answers? Not three. One.
- **100–150 words**, direct answer, sits at the very top of the page under the H1.
- **No throat-clearing.** No "In today's landscape." No "Before we dive in." No restating the question. First sentence answers it.
- Written so it survives being lifted out of context — this block is what AI Overviews and LLM summaries extract.

Draft the actual block in the brief. Do not describe what the block should say — write it. A brief that says "open with a definition of X" is not a brief.

### Step 5 — The structure

Map the question set to H2s. **This is not 1:1 and you should not pretend it is.**

Apply in order:

1. **Dedup.** "What is X" and "What does X mean" are one H2, not two.
2. **Intent filter.** Drop questions whose searcher wants something this page isn't for. A question appearing in the PAA box is not proof it belongs on this page.
3. **Add what's missing.** If the topic needs an H2 that no question asked for, write it. Question-derived H2s are a floor, not a ceiling.
4. **Order by reader need**, not by search volume.

**Every H2 must stand alone.** LLMs read sections independently and cite them out of context. Test each one: if a reader landed on this section cold with no preceding text, does it answer its own heading? If it depends on "as we discussed above," rewrite it.

Target 4–7 H2s. Fewer than 4 is usually a thin page; more than 7 usually means two pages.

### Step 6 — The edge gate

**This is the hard stop.** Full criteria in [references/edge-gate.md](references/edge-gate.md).

Ask: what do the top 5 NOT do? Then pick exactly one:

- **Original data** — a number only this company can produce
- **Specific ICP** — written for a segment the others address generically
- **Named framework** — a repeatable model this page defines and names
- **Deeper subtopic** — the thing everyone mentions in one line and nobody explains

Then force the sentence: **"This page does {X}, which no one else in the top 5 does."**

**The edge must be nameable and it must already exist.**

| Fails | Passes |
|---|---|
| "We'll include original data" | "Median deploy frequency across the 12,000 repos on our platform, 2025" |
| "We'll be more specific to our ICP" | "Written for 2-person ops teams, who can't run the enterprise playbooks every top result assumes" |
| "We'll go deeper" | "Everyone says 'clean your data first' in one line — this explains what clean means and how long it takes" |

**Single mode:** if the user cannot complete the sentence with something specific and real, **stop and do not write the brief.** Say plainly: *"The brief isn't ready. Every top-5 result already does what this page would do. Find the edge first — or brief a different angle where you have one."* Offer to help find the edge. Do not write a brief with an empty edge field to be helpful. Writing it anyway is the failure mode this entire step exists to prevent.

**Batch mode:** do not halt the run. Write the brief with `STATUS: BLOCKED — no edge` at the top and the H2 map intact, so the user gets a triage pile rather than a dead batch. Report the blocked count in your summary.

### Step 7 — Write the brief

Use the template in [references/brief-template.md](references/brief-template.md). Write to `briefs/{keyword-slug}.md`.

The brief includes the eight core fields, the H2 outline with a citation slot per section, the internal linking plan, the schema spec, and the pre-publish checklist appended at the bottom so it travels with the draft.

**Citation slots stay empty unless you have a real source.** Write `[CITE: needed — {what claim}]` for anything you haven't verified. Never populate a citation slot with a plausible-sounding statistic. A fabricated stat that survives to publication is worse than an empty slot, because the empty slot gets caught and the fake number doesn't.

---

## Additions to the Brief

### Internal linking plan

Specify both directions:

- **Outbound** — which existing pages this brief should link to, with anchor text
- **Inbound** — which existing pages should be updated to link to this one

Inbound is the half everyone forgets, and it's the half that actually moves rankings. If you don't know the site well enough to name real URLs, say so and mark it `[NEEDS: site audit]` rather than inventing paths.

### Schema spec

Name the structured data this page should ship with — typically `Article` plus `FAQPage` when the H2s are questions. Specify which H2s map to FAQ entries. For implementation, hand off to the `schema` skill.

---

## Quality Bar

Before delivering, check your own brief:

| Check | Fail looks like |
|---|---|
| Answer block is written, not described | "Open with a clear definition" |
| Edge is specific and real | "More detailed than competitors" |
| Every H2 stands alone | An H2 that starts "Now that we've covered" |
| No fabricated citations | Any statistic you did not verify |
| Reader is a person | "Marketers" instead of "solo marketers at Series A startups with no design resource" |
| Cannibalization checked | You skipped Step 1 |

## Handing Off

After writing the brief, tell the user what to do next in one line:

> Brief at `briefs/{slug}.md`. Hand it to a writer or run it through Claude to draft. When the draft's back, run `pre-publish-check` against it.
