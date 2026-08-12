# Check Rubrics

Pass/fail criteria with worked examples. Read before judging a draft.

Examples below are drawn from different industries on purpose — the distinctions are about structure and specificity, not about any one vertical.

---

## Check 1 — First 150 words

**Method:** count 150 words from the first word of body copy. Ignore the H1, dek, and anything after word 150. Judge only that window.

### Fails

> "In today's rapidly evolving e-commerce landscape, brands face unprecedented challenges in managing inventory. As margins tighten and customer expectations rise, ops teams are being asked to do more with less. In this article, we'll explore..."

Nothing has been answered. This is 40 words of weather report followed by a table of contents.

> "What is inventory turnover? It's a question many brands grapple with. Before we can answer it, we need to understand the history of retail supply chains..."

Restates the question, then defers. Deferral is the tell.

### Passes

> "Inventory turnover is how many times you sell through and replace your stock in a period — annual COGS divided by average inventory value. Most brands track it as a single number, which hides more than it shows: a turnover of 6 driven by one fast SKU is a different business than one where every SKU turns evenly. Track it per category, not in aggregate. A healthy figure depends entirely on what you sell — grocery runs 12 to 15, apparel 4 to 6, furniture 2 to 4 — so comparing yourself to a cross-industry benchmark tells you almost nothing..."

First sentence answers. Everything after adds specificity. Extractable as a standalone block — which is the whole point.

### Edge cases

- **A hook that works.** A one-sentence hook before the answer is fine if the answer lands by sentence three. Two paragraphs of hook is not.
- **Definitional queries.** Answer with the definition immediately. There is no version of "what is X" where the reader wants context first.
- **Comparison queries.** The answer is the verdict, not the criteria. "X suits small teams, Y suits enterprise" up front; the comparison table below.

---

## Check 2 — H2s map to search questions

**Method:** for each H2, write the query someone types to land there. If you can't, it fails.

| H2 | Verdict |
|---|---|
| "How to calculate inventory turnover" | ✅ direct query |
| "Inventory turnover benchmarks by category" | ✅ real query, well qualified |
| "The Bigger Picture" | ❌ nobody searches this |
| "Why This Matters for Your Business" | ❌ narrative filler |
| "Rethinking the Inventory Paradigm" | ❌ clever, unsearchable |
| "Final Thoughts" | ❌ delete or rename to its actual content |

**Exception worth honoring:** an H2 covering something genuinely necessary that nobody searches for yet — a new framework the page defines — passes if it's *named plainly*. "The Activation Ladder framework" passes. "A New Way to Think About Onboarding" doesn't.

**Report:** for each fail, give the plain replacement. "The Bigger Picture" → "How inventory turnover affects cash flow." The fix should take the writer ten seconds.

---

## Check 3 — Sections stand alone

**Method:** copy each section into a blank context and read it. No H1, no preceding sections.

### Fails

> "As we discussed above, the three metrics each require different tracking. This approach works best when..."

Two failures in one sentence: an explicit backreference and an undefined "this approach."

> "That's why the second method is usually better for smaller teams."

Meaningless in isolation. What second method?

### Passes

> "Sell-through rate — the percentage of received inventory sold in a given period — is the hardest of the three metrics to track accurately, because it depends on knowing exactly when stock landed. Most teams approximate it from purchase order dates, which drift by a week or more..."

Reintroduces its own subject. A reader landing here cold is oriented in one sentence.

### The test that catches most failures

Read the **first sentence** of each section alone. If it contains a pronoun or demonstrative whose referent is in a previous section — "this," "that," "it," "these," "the approach" — the section almost certainly fails.

### Not a failure

- Sections that build on shared vocabulary defined in the answer block, as long as the term is *used*, not referenced. Using "sell-through rate" is fine; saying "the first metric we covered" is not.
- Sequential how-to steps, where order is inherent. "Step 3" legitimately follows step 2. But it should still name what it's doing rather than saying "now do the next part."

---

## Check 4 — Verified citations

The check with the most consequence. Work it carefully.

### Procedure

1. Extract every factual claim attributed to a source, plus every specific statistic whether attributed or not.
2. For each attributed claim, **fetch the URL**.
3. Confirm the page resolves, contains the claim, and the number matches.
4. For each unattributed statistic, flag it.

Do not skip step 2 for sources that look reputable. A plausible domain is not verification — fabricated citations overwhelmingly point at real, reputable domains, because that's what makes them plausible.

### Status definitions

| Status | Criteria | Severity |
|---|---|---|
| ✅ Verified | Resolves, claim present, number matches | — |
| ⚠️ Unverifiable | Resolves but claim absent, or paywalled/login-gated | Medium — ask the writer for the page/quote |
| ❌ Broken | 404 or no resolve | Medium — find a live source or cut |
| 🚨 Uncited | Specific statistic, no source | **Highest** — cite or cut |
| ⬜ No data | Section has no data point at all | Low — enrichment, not a defect |

### On uncited statistics

"Studies show 73% of teams struggle with data quality" with no link is the single most dangerous sentence in a draft. It reads authoritative, it survives review because it sounds like something someone read, and it is very frequently invented.

Flag every one individually. Say **cite it or cut it** — those are the only two options. Do not suggest "soften to 'many teams'" as the primary fix; that launders a fabricated number into vague-but-still-unsupported prose. If a real source exists, cite it. If not, the claim goes.

### Number drift

A source saying 68% cited in the draft as 73% is a fail, not a rounding note. Report the actual number from the source.

### Self-citation

Citing the company's own data is legitimate and often the strongest EEAT signal on the page — but it needs a stated basis: sample size, timeframe, method. "Our data shows" alone is ⚠️ Unverifiable. "Across 12,000 accounts in FY2025" is ✅.

---

## Check 5 — Human gets what an AI summary doesn't

**Method:** write a two-sentence summary of the page as an AI would. Then ask: does the summary substitute for the page?

### Fails

A synthesis of publicly available information, organized well. Nothing on the page originates with the author. An AI summary loses only the formatting.

The tell: you could write this page from the top 5 search results without talking to anyone or opening a single internal system.

### Passes

At least one of:

- **Original data** with a stated basis — "median 4.2 turns across 900 brands, 2025"
- **A named framework** the page defines and teaches
- **A specific story** — a named customer, a real timeline, an actual outcome including what went wrong
- **A genuine opinion** — a defensible position an AI wouldn't volunteer, e.g. "aggregate turnover is actively misleading and here's what it hides"
- **A working asset** — a template, calculator, or checklist a reader downloads and uses

### Checking against the brief

If a brief exists, its `Edge` field is the claim being tested. The common drift: a brief with a real edge produces a draft that names it in the intro and never uses it again.

- Brief says "original benchmark data across 900 brands"
- Draft mentions the dataset once, then reverts to generic advice for 1,800 words
- **Fail.** The edge was declared, not delivered. Report it as drift and point at where the draft stops using it.

### Be honest

This is the check people most want fluffed, because failing it means the piece may not be worth publishing at all — which is expensive news after the draft is written. Deliver it anyway. That's the job, and it's cheaper than publishing a page nobody cites.
