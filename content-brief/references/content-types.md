# Content Types

A brief for a listicle, a software roundup, and a ranked data list should not share a skeleton. The question set tells you *what* to cover; the content type tells you *what shape* the page takes and what has to be true of each part.

Pick the type from the SERP, not from habit: whichever format dominates the top 5 is the format the query is asking for. If the user has already chosen a type, use it — and say so if it fights the SERP.

| Signal in the keyword / SERP | Type |
|---|---|
| "{topic} ideas", "{topic} examples", "how to run {topic}" — top results are numbered lists | **A. Ideas listicle** |
| "best {category} software/tools", "{category} platforms", "{X} alternatives" — top results are vendor roundups | **B. Commercial roundup** |
| "top 10 largest/biggest/fastest {things}", "{things} ranked" — top results rank entities by a metric | **C. Ranked list** |
| "what is", "how does", "guide to" — top results are explainers | None of the above. Use the general structure in `SKILL.md` Step 5. |

Every type still goes through the edge gate. A blueprint is a shape, not an edge.

---

## A. Ideas listicle

**Shape**

1. Answer block — names the formats or categories in miniature, not a mood-setting opener
2. *Why this matters now* (optional) — one H2, one dated statistic with its source
3. **The list** — 3–5 category H2s, each with 2–4 numbered items as H3s. **Numbering runs continuously across the page**, not restarting per category.
4. *How to run these well* — 3–5 tips as H3s (personalize, structure, follow up)
5. *How to promote / measure* (optional)
6. Brand section (see [brand-integration.md](brand-integration.md))
7. FAQs

**Item anatomy** — every numbered item carries three things, in this order:

1. **What it is and who it's for** — one or two sentences
2. **How to run it** — 3–4 concrete choices: format, who to invite, a conversation prompt, length. This is the part a reader can act on.
3. **A real-world example** — named organization, what they did, source. See *Sourcing examples* below.

**Watch for**

- **Outline math.** An outline with five categories and five bullets each is 25 ideas. If the title says "12 ideas," decide which number is true *before* the writer sees it. The count in the title must equal the count of numbered items.
- **Category intros** are 1–2 sentences and must stand alone; they're often lifted by themselves.
- **Bullet lists in the outline are seeds, not the final list.** "Include ideas such as: A, B, C" tells the writer what to draw from. It does not mean every seed gets an H3.

**Edge candidates** — deeper subtopic (the top results list ideas; none show them being run), specific ICP, original data.

---

## B. Commercial roundup ("Best X software for Y")

**Shape**

1. Answer block — names the top pick *per situation*, not one winner for everyone
2. **What is {category}** — dictionary-style definition, 2–3 sentences, no fluff. Then 5–10 concrete use cases as a list, then one paragraph on how it differs from the adjacent general-purpose category.
3. **Essential features** — one H3 per feature. Each is 1–2 sentences: what the software should do, and why it matters. Flag the single most important feature and say why. Include modern formats (hybrid/virtual, mobile) if the SERP does.
4. **The platforms** — one H3 per product, titled `{n}. {Product} — Best for {specific situation}`. Each entry: what it is, what it does well, **one real limitation**, who it fits.
5. **Use-case table** — two columns, `Use case | Best-fit platforms`. Built to be extracted by LLMs.
6. **Free vs. paid** — when free tools are enough and the specific needs that push a team to paid
7. **How to choose** — a buying checklist written as questions the reader can answer about their own team
8. Brand section
9. FAQs

**Rules that keep a roundup honest** (and citable):

- **"Best for" must be narrow enough to be false for someone.** "Best for teams that run auctions" is a claim. "Best overall" is filler.
- **Every entry states a limitation.** A roundup where every product is great is an ad, and neither readers nor LLMs treat it as a source.
- **Verify each vendor's claims on the vendor's own page** and record the URL. Pricing and features go stale — never write a price without a date, or say "check current pricing."
- **If the brand is one of the entries, say so.** State the evaluation criteria up front, give the brand's entry the same anatomy (including a limitation), and don't let it be the only entry with a proof point.
- **The use-case table must be supported by the prose.** A platform can't be "best for" a row the entries don't back up. Check every table cell against its H3.
- **Match the table's names to the H3s exactly.** LLMs match strings.

**Edge candidates** — specific ICP where the *ranking changes* (a roundup for teams that must sync with a specific CRM recommends different tools than a generic one), deeper subtopic (the feature every roundup lists in one line), named framework (the buying checklist, if it's actually a model).

---

## C. Ranked list ("Top 10 largest X")

**Shape**

1. Answer block — names the top entries and the metric in the first paragraph
2. **What is {X} and why it matters** — direct, 2–4 sentences
3. **The list** — one-line lead-in, then one H3 per entry: `{rank}. {Name}` followed by the metric with its **year and source**, and 1–2 lines on what makes the entry distinctive
4. **What {ICP} can learn** — the takeaways section. This is usually where the edge lives.
5. **How to build / strengthen yours** — actionable tips, role of tooling
6. CTA and conclusion

**Rules**

- **Define the ranking metric before the list.** "Largest" by what — total members, alumni of record, reachable contacts, dues-paying members? Without a defined metric the list can't be checked and two sources will disagree.
- **Every entry carries number + year + source.** If sources disagree, show the range and say why (different definitions, different years). An entry with no verifiable figure is dropped — never estimated.
- **A year in the title is a promise.** "(2025 Update)" means the figures are that year's or the latest available with the year labeled, and the page shows a visible last-updated date. If you can't deliver that, drop the year.
- **Budget the words.** Ten entries in a 1,000–1,200-word page is roughly 60–90 words per entry once the intro and takeaways are paid for. That's enough for metric + source + one distinguishing fact. It isn't enough for narrative. Say so in the brief so the writer doesn't pad.
- **A list alone is not an edge.** "The top 10, updated" is rejected by the edge gate. The takeaways section, or an explanation of how the number is counted, is what earns the page.

**Edge candidates** — specific ICP (takeaways for the practitioner audience, not a general reader), deeper subtopic (how the metric is measured and why sources differ), original data.

---

## Sourcing examples

Real-world examples are what separate a listicle from a paraphrase of the top 5. They are also where fabrication is most tempting, because a plausible example is easy to invent.

A usable example needs:

- **A named organization** and a specific event, program, or product — not "one university."
- **A source URL you opened.** Not a search snippet, not memory.
- **Only what the source says.** One or two sentences: what they did, for whom, in what format.
- **The gap, stated.** If the page doesn't report attendance or outcomes, the brief's example slot says so — `Not reported: attendance, outcomes` — so the writer says "the source did not report attendance" instead of filling in a number.

Also:

- **Keep the unflattering ones when they're real.** An event that ended early for low attendance is more useful to a reader, and more credible, than a list where everything worked.
- **Prefer recent** (last two years) and **prefer organizations like the reader's.** Note the year in the brief.
- **Vary the examples.** Five from the same institution is one example.
- **Never invent a plausible one.** An unfilled slot reads `[EXAMPLE: needed — {item}]`. That gets caught in review. A fake example doesn't.
