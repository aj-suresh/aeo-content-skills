# Entry Research (Roundups and Comparisons)

For a commercial roundup, an "alternatives to X" page, or a ranked list of products, the brief carries a **verified-facts table**: one row per entry, every cell traceable to a page you opened. It is what lets the writer draft 10 fair entries without inventing a feature, a price or a customer.

This builds on the roundup rules in [content-types.md](content-types.md) (type B) and the claim rules in [brand-integration.md](brand-integration.md).

## The table

One row per entry, in the order the page will show them. The brand's own entry is row 1 if the page lists it first, and gets the same columns.

| # | Platform | Best for | Verified facts to use | Limitation | Pricing (checked {date}) |
|---|---|---|---|---|---|
| 1 | {Entry} | {The specific situation it fits} | {3 to 5 facts from the vendor's own page: features, integrations, named customers, compliance} | {One real limitation} | {Exact figure and unit, or "Custom; demo request", or "Not published"} |

Rules for each column:

- **Best for** is narrow enough to be false for someone. "Best for teams that need X" is a claim. "Best overall" is filler.
- **Verified facts** come only from the vendor's own pages (home, product, pricing, docs). Record the URL and the date opened. A fact from another roundup's description of the vendor does not count.
- **Limitation** is real and specific. Every entry gets one, the brand's own included.
- **Pricing** is the exact figure, its unit (per user, per month, per seat), and the date checked. If the page does not publish a price, write "Not published" and do not estimate. If the extracted text is ambiguous about which plan a figure belongs to, mark `[VERIFY]` and say what is unclear.

## Inference labels

A limitation often comes from what the vendor's pages leave out. Mark those:

- Tag the cell **(inference)**.
- Tell the writer to say "not mentioned on its site", never "doesn't support".
- A limitation the vendor states itself (a deprecation notice, a published cap) needs no tag. Link the source.

## Vendor-reported results

Case-study numbers on a vendor's page ("2x completion", "40% faster") are claims, not facts.

- Attribute them: "reported by {vendor}".
- Never put one in a table cell as a plain fact.
- Do not carry a vendor's figure into a comparison with another vendor's different metric.

## Baseline block: what readers are replacing

When the page is "alternatives to {incumbent}", add a short block that states, neutrally, what the incumbent offers and what it costs, taken from its own pages.

- List its product lines and the clouds, integrations or platforms it supports.
- State pricing with the unit, the date, and what is not published.
- Use these facts once, in the at-a-glance intro, in a neutral tone.
- Do not criticise the incumbent. A reader switching from it already knows its flaws, and an unfair line costs the page its credibility.

## When to stay: an honest counterpoint

For an "alternatives to {incumbent}" page, give the incumbent a short section on when it is still the right choice. Four or five "Stay with {incumbent} if you..." bullets, each tied to a page of the incumbent's. This makes the rest of the recommendations believable, and it is rare enough in the top results to count toward the edge. Keep the tone neutral and do not pitch the brand in this section.

## The use-case fit table

Build the "use case → best-fit platforms" table last, from the rows above.

- Every cell must be supported by the entry it names. If an entry's row does not back a use case, remove the cell.
- Add a runner-up column when two entries fit a use case.
- Names match the H3 titles exactly. LLMs match strings.
- Close with one line the reader can act on, such as "If you teach three or more of these, one platform that covers them all costs less to run than three tools." Only write it if it is true for the entries listed, and check that it does not unfairly favour the brand.

## Re-check list

End the table with a **Re-check before publishing** line naming every cell that rests on something unconfirmed:

- a pricing page that did not load
- a compliance claim you want confirmed on the vendor's security page
- an allowance or limit that the page states loosely
- an ambiguous figure
- any capability the brand's own product team must confirm (`[VERIFY with product team]`)

Dates matter. Pricing and features go stale, so the brief states the date checked and the page shows "as of {month year}" next to every price.

## Count integrity

If the title says "10", the table has 10 rows, the outline has 10 H3s, the answer block says 10, and the schema `ItemList` has 10 items. Count them.
