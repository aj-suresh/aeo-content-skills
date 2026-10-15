# SERP Research

Two outputs: the **question set** and the **top-5 coverage map**. Everything downstream depends on these being real.

## The Honest Limitation

Web search approximates the People Also Ask box. It does not scrape Google's actual PAA widget, and the questions you surface will overlap heavily with — but not exactly match — what a user sees in the browser.

**Say this out loud at the confirmation gate.** Do not present inferred questions as if they were pulled from the live PAA box. For a keyword that matters, the right move is for the user to run the search themselves and paste the real box in; the confirmation gate exists for exactly this.

Never invent a PAA question to round out a set. Four real questions beat eight where half are fabricated.

## Building the Question Set

Run several angles rather than one search — a single query gives you one slice of the intent space.

1. **The keyword itself** — what comes back, and what the results assume the reader already knows
2. **Question forms** — `what is {keyword}`, `how to {keyword}`, `{keyword} vs`, `why {keyword}`, `{keyword} best practices`
3. **"Related searches"** and autocomplete-style variants surfaced in results
4. **Forums and communities** — Reddit, Hacker News, industry Slack and Discord, Stack Overflow, trade association forums. Practitioners ask the questions SEO pages avoid, and these are disproportionately good H2s.
5. **The user's own support surface** — if they have docs, a help center, or a sales team, ask what people actually ask. This is the highest-signal source and it costs one question.

### Then filter

| Step | What to drop |
|---|---|
| **Dedup** | Near-synonyms — "what is X" / "what does X mean" / "X definition" are one question |
| **Intent filter** | Questions whose searcher wants a different page than this one. Appearing near your keyword is not proof of belonging on your page. |
| **Depth filter** | Questions answerable in one sentence — those are FAQ entries, not H2s |

What survives is your candidate H2 set. Expect to keep 4–7 out of 15–20 raw.

## Building the Coverage Map

Fetch the top 5 organic results. Actually fetch them — reading the SERP snippet is not reading the page, and the gap analysis in Step 6 is worthless if it's based on meta descriptions.

For each, record:

| Column | What you're capturing |
|---|---|
| **URL** | |
| **Angle** | The stance or framing — definitional, comparison, how-to, opinion |
| **Depth** | Shallow overview / solid / genuinely deep |
| **Structure** | H2 pattern — this shows you the consensus shape and where to break it |
| **Data** | Do they cite original numbers, or recycle the same industry stat? |
| **Author** | Practitioner, staff writer, or anonymous — an authority read |
| **What it misses** | The column that feeds the edge gate |

### Read for the pattern

Once the five are mapped, ask:

- **What do all five do?** That's table stakes. You have to cover it, and covering it is not an edge.
- **What does exactly one do well?** That's a differentiator someone already claimed.
- **What does none do?** That's your candidate edge — carry it to Step 6.
- **What do they all get wrong or gloss over?** Often the strongest angle, and the most defensible.

If the top 5 are near-identical, that's a real signal: either the topic is genuinely settled (find a different topic) or nobody has done the work yet (a large opening). The coverage map tells you which.

## Reference URLs the user supplied

If the user gave reference pages ("see how this one is written"), fetch them whether or not they rank:

- If one ranks in the top 5, it's already a row in the coverage map.
- If it doesn't, note it separately as a **style or structure reference**: what specifically is worth imitating (definition-first, direct sentences, how a section is laid out) and what isn't. Style, not phrasing — the brief should never tell a writer to reproduce another page's text or section order wholesale.

## Keyword data

If a keyword-research tool is connected in the session (Semrush, Ahrefs, or similar), use it for the keyword cluster and SERP data, and say which tool the numbers came from. If not, don't quote search volumes or difficulty scores you can't source — a cluster without volumes is fine; a cluster with invented volumes is not. Whatever the source, dedupe the cluster and sort it into primary / secondary / related.

## Comparison and roundup queries

When the SERP is vendor roundups, the coverage map needs a second layer. For each vendor you plan to name, fetch **that vendor's own** features and pricing pages, and record the URL and date. Claims about a competitor come from the competitor's page, not from another roundup's description of it. The method, table and labels for this layer are in [entry-research.md](entry-research.md).

Read the SERP for what is *not* there. If the "alternatives" results are auto-generated directories, a vendor's own pages, or lists of unrelated products, there is no editorial roundup to beat, and the gap is the whole format: stated criteria, dated pricing and a limitation on every entry. Say that at the gate, and note which pages you could not open.

## The AI answer snapshot

For the primary query, record what AI assistants currently say. This is where an AEO brief finds its gap.

1. Run the query in Google (note whether an AI Overview appears and which sources it cites) and, where the session allows it, in ChatGPT and Perplexity.
2. For each, record: the answer in one line, the sources it cites, and where the answer falls short (outdated, generic, missing a segment, no numbers).
3. Date the capture. AI answers change faster than organic rankings.
4. A cited source that is not in the organic top 5 is a second competitor. Add it to the coverage map.

If you cannot run the assistants, write `[NEEDS: AI answer snapshot]` and ask the user to paste the answers and their sources. Do not infer what an assistant would say.

The snapshot shows where a page can add value, and it does not predict citations. Treat any statistic about citation rates from a vendor blog as unverified until you have read the original study.

## Your own pages and Search Console

If Search Console is connected, or the user supplied an export, add the user's own pages to the coverage map:

- Pages that already rank for the keyword or near-synonyms, with position, impressions and the date range.
- Which phrase each page owns. This decides the cannibalization call in Step 1 and the anchor text off-limits on the new page.
- Pages sitting at positions 5 to 20 for related topics. They are the best internal-link targets.

State the date range with every figure. Without Search Console, say so and do not quote positions.

## Also Worth Checking

- **Is there an AI Overview for this query?** If yes, note which sources it pulls from — that's the citation target, and it's often not the #1 result.
- **Does the SERP skew to a format** you're not planning — video, tools, forums? Format mismatch beats content quality. If the top 5 are all calculators, a blog post will not rank.
- **How old are the top results?** A SERP full of 2019 pages on a topic that changed is a freshness opening. A SERP full of last-month pages on a stable topic means recency won't help you.

## What to Present at the Gate

Keep it scannable. Two tables and a claim:

1. **Question set** — question, intent read, keep/drop with reason
2. **Coverage map** — the table above, five rows, with the user's own ranking pages added when known
3. **AI answer snapshot** — what AI assistants say now, their sources, where they fall short (or the line saying it could not be captured)
4. **Gaps I think are real** — 1–3 candidates, stated as claims the user can push back on

Then ask for corrections, and flag explicitly that pasting the real PAA box will improve the structure.

In batch mode, compress to one row per keyword and take a single approval for the whole set.
