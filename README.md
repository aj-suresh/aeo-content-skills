# AEO Content Skills

Two agent skills for writing content that ranks on Google **and** gets cited by AI Overviews, ChatGPT, Perplexity, and Claude.

Compatible with Claude Code, Claude Cowork, Codex, Cursor, and other [agentskills.io](https://agentskills.io)-compatible agents.

| Skill | Input | Output |
|---|---|---|
| **`content-brief`** | A keyword | A brief a writer or an agent can execute against |
| **`pre-publish-check`** | A finished draft | Pass/fail on five checks, with specific fixes |

## Why these exist

The failure mode of AI-assisted content isn't bad writing. It's *competent, well-structured, entirely redundant* writing — pages that read fine and add nothing to what already ranks. Those pages don't rank, don't get cited, and cost real money to produce.

These two skills are built around gates that catch that before it becomes a draft, and before a draft becomes a published page.

---

## `content-brief`

Takes a keyword through seven steps:

1. **Cannibalization check** — do you already have a page targeting this? Two pages fighting over one query is the most common self-inflicted SEO wound, and it's invisible for months.
2. **SERP research** — the question set people actually search, a coverage map of the top 5, and the content type the SERP is asking for (ideas listicle, commercial roundup, ranked list, explainer).
3. **Confirmation gate** — you review and correct the research before any structure gets built.
4. **The answer block** — the two-paragraph, ~120–160-word intro that AI Overviews extract, with keyword placement planned. Written out, not described.
5. **The structure** — a blueprint for the content type, with search questions mapped to H2s, deduped and intent-filtered. Every section has to stand alone, because LLMs cite passages, not pages. Each section gets direction (named items, not "cover best practices"), a word budget, and a citation slot; the count in the title has to match the count in the outline.
6. **The edge gate** — see below.
7. **Write** — brief file with the core fields, keyword cluster, H1 / meta title / meta description options, H2 outline with direction and citation slots, a brand section, FAQs, internal linking plan, and schema spec.

### Built for real briefs

- **Bring your own outline.** Pre-set outlines, keyword clusters, reference URLs, and word counts are treated as constraints. The skill reconciles them (a "12 ideas" title over 25 seeded bullets, a 1,000-word target for ten entries) instead of overwriting or silently accepting them.
- **Page-type blueprints.** Ideas listicles, commercial roundups ("best X software"), and ranked lists each get their own shape and rules — see `references/content-types.md`.
- **Real examples only.** List items carry a named, sourced example, plus a note of what the source *didn't* report so the writer doesn't fill the gap with a number.
- **A brand section that stays honest.** Every product claim traces to a URL you provided, proof points quote the source's figure exactly, and roundups that include your own product disclose it and require a limitation on every entry — see `references/brand-integration.md`.

### The edge gate

The step that makes this different from an outline generator.

Before writing the brief, the skill asks what the top 5 results *don't* do, and requires one of:

- **Original data** — a number only you can produce
- **Specific ICP** — a segment the others address generically, where the advice actually changes
- **Named framework** — a repeatable model this page defines and names
- **Deeper subtopic** — the thing everyone mentions in one line and nobody explains

Then it forces the sentence: *"This page does {X}, which no one else in the top 5 does."*

**If you can't complete that sentence with something specific and real, the skill stops and refuses to write the brief.** "More thorough," "better written," and "our unique perspective" are all rejected explicitly.

This is deliberate and it will occasionally be annoying. It's cheaper than a writer's week spent on a page nobody cites.

### Batch mode

Pass a list of keywords and it takes one approval for the whole set instead of one per keyword. In batch mode the edge gate marks briefs `STATUS: BLOCKED — no edge` rather than halting the run, so you get a triage pile instead of a dead batch.

---

## `pre-publish-check`

Audits a finished draft. Accepts a local markdown file, pasted text, or a live URL. Works whether or not a brief ever existed — point it at content you published two years ago.

1. **First 150 words answer the core question directly** — no throat-clearing, no deferral
2. **Every H2 maps to a real search question** — "The Bigger Picture" fails
3. **Every section stands alone** — no "as we discussed above," no orphan pronouns
4. **One *verified* cited data point per section**
5. **A human gets something an AI summary doesn't**

### Check 4 does real verification

It fetches every citation URL, confirms it resolves, and confirms the page actually contains the claim with a matching number. Each gets a status:

| | |
|---|---|
| ✅ Verified | Resolves, claim present, number matches |
| ⚠️ Unverifiable | Resolves but claim absent, or paywalled |
| ❌ Broken | 404 |
| 🚨 **Uncited** | A specific statistic with no source — **highest severity** |

A confident statistic with no link is the most dangerous sentence in a draft: it reads authoritative, it survives review because it sounds like something someone read, and it's frequently invented. The rubric says **cite it or cut it**, and explicitly rejects "soften it to 'many teams'" as a fix — that launders a fabricated number into vague-but-still-unsupported prose.

If a brief exists, the audit also checks the draft against it. A declared-but-undelivered edge — named in the intro, then abandoned for 1,800 words — reports as drift.

---

## Install

Clone anywhere, then symlink into your agent's skills directory.

**Claude Code:**

```bash
git clone https://github.com/aj-suresh/aeo-content-skills.git
cd aeo-content-skills
ln -sfn "$PWD/content-brief" ~/.claude/skills/content-brief
ln -sfn "$PWD/pre-publish-check" ~/.claude/skills/pre-publish-check
```

**Codex / `.agents` convention:**

```bash
ln -sfn "$PWD/content-brief" ~/.agents/skills/content-brief
ln -sfn "$PWD/pre-publish-check" ~/.agents/skills/pre-publish-check
```

Symlinking rather than copying means editing the repo updates the live skill.

## Use

No configuration required — both skills ask for what they need.

```
write me a content brief for "inventory turnover ratio"
```

```
run pre-publish-check on drafts/inventory-turnover.md
```

```
audit https://example.com/blog/inventory-turnover before I republish it
```

### Optional: skip the questions

`content-brief` needs six things — your product in one sentence, your reader, your competitors, your proprietary assets (data, frameworks, case studies), your ground-truth product URLs and CTA destination, and your voice (tone and POV). It asks for whatever it doesn't have.

To stop it asking every run, put them in `.agents/product-marketing.md` (or `.claude/product-marketing.md`, or `~/.agents/product-marketing.md` for a global default). This is a shared convention — several other skills read the same file.

A stub full of `TODO` is treated as absent, so a half-filled file won't silently produce a brief written for nobody.

## A limitation worth knowing

The SERP research approximates the People Also Ask box via web search. It does **not** scrape Google's live PAA widget, and the questions it surfaces will overlap with but not exactly match what you'd see in a browser.

The confirmation gate exists for this. For a keyword that matters, run the search yourself and paste the real box in. The skill will say this out loud rather than presenting inferred questions as if they came from the widget.

## Structure

```
content-brief/
├── SKILL.md
└── references/
    ├── brief-template.md      # output format + field notes
    ├── content-types.md       # blueprints: ideas listicle, roundup, ranked list; sourcing examples
    ├── brand-integration.md   # ground truth, brand section, proof points, CTA by funnel stage, voice
    ├── edge-gate.md           # the four valid edges, with pass/fail examples per page type
    └── serp-research.md       # research method, filters, coverage map

pre-publish-check/
├── SKILL.md
└── references/
    └── check-rubrics.md     # worked pass/fail examples per check
```

## License

MIT — see [LICENSE](LICENSE).
