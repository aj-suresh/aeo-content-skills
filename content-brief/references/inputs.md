# Inputs That Make a Better Brief

A brief is only as good as what goes into it. A bare keyword produces a competent brief. Add the inputs below and it produces one a writer can execute without a follow-up question, and one with something real to say.

Use this file two ways:

- **When the user gives only a keyword**, offer the intake list once (see "The intake list" below) and ask for the Tier 1 items you don't have. Do not interrogate. Ask for what is missing, in one message.
- **When writing the brief**, trace each field back to an input. A field with no input behind it is a signal, not a formatting problem. Say what is missing.

## Tier 1: Required

These six are in `SKILL.md` ("Get company context"). Never guess them.

| Input | Feeds |
|---|---|
| Product, one sentence | Answer block, CTA |
| Reader: role + context | Reader field, ICP edge |
| Competitors likely to rank | Coverage map |
| Proprietary assets: data, frameworks, quotable customers, case studies with numbers | Edge gate, proof point |
| Ground-truth URLs and the CTA destination | Every product claim |
| Voice: tone, POV, banned words | Voice field |

Add two more that decide the page's shape:

| Input | Feeds |
|---|---|
| **Target keyword and page type** (blog post, help article, commercial page, comparison) | Content type, funnel stage |
| **Country and language** | Keyword database, SERP read |

## Tier 2: High impact

Each of these changes the brief, not just decorates it.

| Input | Why it matters | Feeds |
|---|---|---|
| **The real People Also Ask box**, pasted, with the date | Web search only approximates it. The pasted box is the actual question set. | Question set, FAQs |
| **What AI assistants say now** for the primary query: the answer text and the sources it cites | Shows the citation target and where the current answer falls short. This is the gap an AEO brief can fill. | AI answer snapshot, answer block |
| **Search Console data** (connected, or an export of queries, pages, positions, impressions) | Finds cannibalization, which existing pages sit at positions 5 to 20, and which pages deserve an internal link. | Cannibalization, internal linking |
| **Keyword data** (Semrush or Ahrefs connected, or an export): volume, difficulty, CPC, SERP features | Without it the cluster has no numbers, and the brief says so. | Keyword table |
| **Customer language**: questions from sales calls, support tickets, community threads | The highest-signal source for H2s the top 5 skip. | Question set, edge |
| **A named author or subject-matter expert**, and what only they know | Google's people-first guidance asks who wrote the page and what first-hand knowledge backs it. | Who/How/Why, EEAT signal |
| **The decision the reader is making** and what they should understand or be able to do afterwards | Turns a topic into a page with a job. | Core question, reader outcome |
| **Existing related pages**: pillar, landing page, siblings | Decides which page owns which phrase, and how they link. | Relationship to existing pages |
| **Claims to avoid**: legal or compliance limits, unproven numbers, terms the company won't use | Stops a draft inheriting a claim the company can't defend. | Don't claim list |
| **Required terminology**: exact product names, spellings, category labels | AI systems and readers match strings. Inconsistent names weaken both. | Keyword and terminology notes |
| **Success metric and an owner for the refresh** | A page with no metric and no owner goes stale unnoticed. | Measurement and refresh |

## Tier 3: Nice to have

| Input | Feeds |
|---|---|
| Two or three reference URLs, with what to imitate and what not | Style reference |
| A sample of approved writing in the brand's voice | Voice |
| Screenshots, diagrams, product visuals the writer may use | Visuals |
| Briefs from earlier posts that performed | Calibration |
| Word count, a pre-set outline, must-link and must-avoid pages | Constraints (treated as constraints, not suggestions) |
| A site config for internal linking (sites in scope, money pages) | Internal linking plan |

## The intake list

Offer this once, when the user supplies only a keyword. Keep it short and let them skip lines.

```
To make the brief specific, send what you have. Skip anything you don't.

1. Keyword, page type, country and language
2. Reader: role and situation, and the decision they are making
3. Product in one sentence, plus the product, pricing and CTA URLs
4. Competitors to name or beat, and any reference pages
5. Anything only you can say: data, customer results, a framework, an expert's view
6. The People Also Ask box for the keyword (paste it, with the date)
7. What ChatGPT, Perplexity or Google's AI Overview currently say for it (paste the answer and its sources)
8. Existing pages on this topic (pillar, landing page, older posts), and Search Console data if you have it
9. Claims you can't make, and exact product or category terms to use
10. Author or reviewer, and how you will judge the page
```

If the user says "just run it", run it. Mark every empty input as `[NEEDS: ...]` in the brief instead of filling it with a guess.

## Minimum viable input, and the best input

| | Gets you |
|---|---|
| **Keyword only** | A structurally sound brief. The edge gate will probably stop it, because nothing proprietary was supplied. |
| **Keyword + Tier 1** | A brief with a real reader, real product claims and a real edge candidate. |
| **Keyword + Tier 1 + the real PAA box + current AI answers + Search Console** | A brief that targets the actual gap in what ranks and what AI systems cite, with cannibalization and linking already resolved. |

## Why these inputs, and how far to trust the research behind them

- **Primary source.** Google's guidance on creating helpful, people-first content frames self-assessment around original value beyond what other results offer, clear authorship, and being transparent about how a page was made. It is the basis for the "Who / How / Why" and "Value beyond the top 5" fields. See [Creating helpful, reliable, people-first content](https://developers.google.com/search/docs/fundamentals/creating-helpful-content).
- **Practitioner sources.** The advice to capture current AI answers, keep a fact bank, name required terminology, set a refresh owner, and front-load the audience and problem before SEO instructions comes from practitioner write-ups, for example [Prose Media's AI-era brief template](https://www.prosemedia.com/blog/content-brief-template-ai-era-seo) and [Core Ranks' writer brief format](https://coreranks.substack.com/p/the-content-brief-format-i-use-for-writers). They are reasonable, not proven. Treat any citation-rate statistic you find in vendor blogs as unverified until you have read the original study.
- **Keep the brief usable.** A template nobody uses fails. If a field goes unused across several briefs, sharpen it or drop it for that page type, and say why in one line.
