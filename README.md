# AEO Content Skills

Four agent skills for writing content that ranks on Google **and** gets cited by AI Overviews, ChatGPT, Perplexity, and Claude.

Compatible with Claude Code, Claude Cowork, Codex, Cursor, and other [agentskills.io](https://agentskills.io)-compatible agents.

| Skill | Input | Output |
|---|---|---|
| **`content-brief`** | A keyword | A brief a writer or an agent can execute against |
| **`pre-publish-check`** | A finished draft | Pass/fail on five checks, with specific fixes |
| **`internal-linking`** | A draft (Word / Google Doc) | A linked copy of the draft, plus the existing pages that should link to it |
| **`blog-schema`** | A brief or a draft | One validated JSON-LD `@graph` that matches the visible page, plus a report of what ships, what was skipped and what is missing |

## Why these exist

The failure mode of AI-assisted content isn't bad writing. It's *competent, well-structured, entirely redundant* writing — pages that read fine and add nothing to what already ranks. Those pages don't rank, don't get cited, and cost real money to produce.

These skills are built around gates that catch that before it becomes a draft, and before a draft becomes a published page.

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

## `internal-linking`

Adds internal links to a draft before it goes live, in both directions.

1. **Inventory**: reads your sitemap and fetches every page's title, headings and text. It drops translated copies, thank-you pages, tag archives, and noindex or canonicalised pages, then caches the result for a week.
2. **Shortlist**: scores every page against the draft. For each candidate it names the paragraph where a link fits and the phrases already in that paragraph that would make a natural anchor.
3. **Search Console** (optional): checks which page Google already associates with each concept, prioritises pages sitting at positions 5–20, and flags cannibalization when an existing page already ranks for the draft's keyword.
4. **Insert**: writes real hyperlinks into a *copy* of the .docx. Bold, italics and fonts are kept, the original is never touched, and every link is verified afterwards.
5. **Inbound plan**: the 3–6 existing pages that should link to the new post, each with the exact sentence to edit and the anchor inside it.

Inbound is the half everyone forgets, and it's what gets a new post crawled and ranked.

### Judgment, not a quota

The defaults are about 1 link per 150–250 words, one per paragraph, each URL once, none in headings or the opening sentence, and 1–3 commercial pages scaled to funnel stage. They're stated as defaults with reasons, and writer instructions override them. The skill asks for those instructions up front: sites in scope, target keyword, must-link pages, pages to avoid.

Anchors come from the writer's own words. If an important link has no natural anchor, the skill proposes wording in the report and leaves the prose alone.

When a site has five posts on one topic, it links the strongest one rather than all five.

### Multi-site companies

If you run sister brands, list them in `config/sites.md` with the topics each one owns. The skill only links across brands when the draft really covers that brand's topic, and labels those links so the writer sees them.

### Setup

Copy `internal-linking/config/sites.example.md` to `config/sites.md` and `patterns.example.json` to `patterns.json`, then fill in your sites, Search Console properties and money-page paths. Both files are gitignored. Without them, the skill asks for your site URL each run.

The first run creates a small venv with `python-docx` in `~/.cache/internal-linking/`. Google Docs work through a .docx round trip: download, link, upload. Hyperlinks survive the conversion.

---

## `blog-schema`

Turns a brief's schema spec, or a finished draft, into JSON-LD for the post. It is the skill `content-brief` hands off to.

1. **Collects the page facts**: URL as served, H1, dates, byline, hero image, the visible FAQ, and the list entries the page is built around.
2. **Inspects the live site** (`scripts/schema_check.py inspect <url>`): the canonical, how the trailing-slash twin redirects, and every JSON-LD node already emitted. If the site already builds a graph, the skill extends it and reuses its `@id` values instead of adding a second `BlogPosting`.
3. **Picks the types the page earns** and records each skip with a reason. FAQPage and ItemList are marked machine-readable only, because Google ended FAQ rich results on 2026-05-07 and its carousel covers only courses, movies, recipes and restaurants.
4. **Builds one `@graph`** and **validates it** (`scripts/schema_check.py validate`). With `--page` it confirms that every FAQ question and answer, list entry, headline and date appears in the visible text, and it blocks Review, AggregateRating, Product and SoftwareApplication on roundups.
5. **Reports** what ships, what changed on the live page, where the brief and the draft disagree, and what it still needs from you.

It never invents an author, date, image or logo. Gaps become `TODO_` placeholders, and the validator fails until they are filled. A brief on its own produces a PROVISIONAL result, since brief answers are directions and not final text.

`references/astro.md` covers shipping the graph from an Astro site. The checker uses only the Python standard library.

---

## Install

Clone anywhere, then symlink into your agent's skills directory.

**Claude Code:**

```bash
git clone https://github.com/aj-suresh/aeo-content-skills.git
cd aeo-content-skills
ln -sfn "$PWD/content-brief" ~/.claude/skills/content-brief
ln -sfn "$PWD/pre-publish-check" ~/.claude/skills/pre-publish-check
ln -sfn "$PWD/internal-linking" ~/.claude/skills/internal-linking
ln -sfn "$PWD/blog-schema" ~/.claude/skills/blog-schema
```

**Codex / `.agents` convention:**

```bash
ln -sfn "$PWD/content-brief" ~/.agents/skills/content-brief
ln -sfn "$PWD/pre-publish-check" ~/.agents/skills/pre-publish-check
ln -sfn "$PWD/internal-linking" ~/.agents/skills/internal-linking
ln -sfn "$PWD/blog-schema" ~/.agents/skills/blog-schema
```

Symlinking rather than copying means editing the repo updates the live skill.

## Use

No configuration required. Each skill asks for what it needs.

```
write me a content brief for "inventory turnover ratio"
```

```
run pre-publish-check on drafts/inventory-turnover.md
```

```
audit https://example.com/blog/inventory-turnover before I republish it
```

```
add internal links to drafts/inventory-turnover.docx and tell me which posts should link to it
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

internal-linking/
├── SKILL.md
├── config/
│   ├── sites.example.md       # sites, Search Console properties, topic ownership, house rules
│   └── patterns.example.json  # money-page and exclusion regexes per site
├── references/
│   ├── linking-rules.md       # density, placement, anchors, sister sites, cannibalization, examples
│   └── report-template.md
└── scripts/
    ├── inventory.py           # sitemap crawl + page cache (stdlib)
    ├── candidates.py          # outbound/inbound shortlist (stdlib)
    ├── docx_links.py          # extract / insert / verify hyperlinks in .docx
    └── run.sh                 # runs docx_links.py in a private venv

blog-schema/
├── SKILL.md
├── references/
│   ├── type-selection.md      # which types to ship or skip, with Google's current status
│   ├── jsonld-patterns.md     # templates and matching rules per type
│   └── astro.md               # emitting the graph from Astro, canonical URLs, heading ids
└── scripts/
    └── schema_check.py        # inspect a live page; validate JSON-LD against the visible text (stdlib)
```

## License

MIT — see [LICENSE](LICENSE).
