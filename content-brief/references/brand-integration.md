# Brand & Product Integration

A brief that ignores the product produces a page that ranks and converts no one. A brief that leads with the product produces a page that fails the human check — readers and LLMs both discount a page that reads as an ad.

The rule: **the page earns the right to mention the product by being useful first, and every product claim is checkable.**

## 1. Ground truth

The company context gives you one or more product URLs — a landing page, a features page, an events page. Those are the **only** source for product claims in the brief.

- **Fetch them.** Don't work from memory or from what the product "probably" does.
- **Copy capability bullets from the page**, not from what similar products offer.
- A capability the pages don't support gets `[VERIFY: {claim}]` in the brief. Never write it as fact for the writer to inherit.
- If no product URL was given, ask for one. Don't guess.

## 2. Where the brand goes

| Placement | Rule |
|---|---|
| **Intro / answer block** | No. The answer block answers the question. |
| **Body sections** | A contextual link at most, where the product is the natural example. Anchor text describes the capability ("online alumni community"), never "click here" or the bare brand name. |
| **Dedicated brand H2** | Yes — near the end, before FAQs. Titled around the reader's problem: `How {Brand} helps with {topic}`. |
| **Inside a roundup list** | Only in a commercial roundup, and only with the disclosure and the limitation. See `content-types.md`, type B. |

## 3. The brand section

Four parts, in this order, in 150–250 words total:

1. **The bridge** — one or two sentences connecting a problem *this page raised* to the product's capability. If you can't point to the problem earlier on the page, the section is bolted on.
2. **Capabilities mapped to problems** — 5–8 bullets, each tied to something the page discussed (segmented outreach, follow-up, event registration, CRM sync). A feature dump with no tie-back fails.
3. **One proof point, or none** — a named customer, a real number, a cited case-study URL. See below. If you don't have one, cut this part; don't soften it into "customers see great results."
4. **One CTA** — a single action with its URL.

## 4. Proof points

- **Quote the figure exactly.** "3x higher participation" only if the case study says 3x. No rounding up, no rounding to a better-sounding number.
- **Don't imply causation the source doesn't claim.** "Launched in under a week and saw 3x participation" is two facts from the source, not "launching fast caused 3x."
- **Cite the case-study URL** in the brief's citation slot.
- No customer name and figure you can verify → no proof point. `[CITE: needed — customer result]`.

## 5. CTA and funnel stage

The CTA follows the reader, not the company's wish list. One CTA per page.

| Funnel stage | Reader is | CTA that fits |
|---|---|---|
| **ToFu** — definitional, ideas, "what is" | Learning the topic | A guide, template, checklist, or related resource |
| **MoFu** — comparison, "how to choose" | Evaluating approaches | A comparison sheet, a case study, a product tour |
| **BoFu** — "best {software}", vendor-vs-vendor | Ready to shortlist | Demo, trial, pricing |

**If you're putting a demo CTA on a ToFu page anyway**, that's a choice, not a default: keep it to the brand section only, make it the page's one CTA, and note in the brief that it's a deliberate stretch. A demo ask in paragraph two of an ideas listicle costs trust for no gain.

## 6. Style references

Users often point to a page and say "write like this — direct, no fluff." That's a style instruction, and it's useful. Record it as:

```
Style reference: {URL}
Imitate: {the specific qualities — definition-first, short sentences, no filler openers, "the software should…" constructions}
Do not: reuse phrasing, section order, or examples from that page.
```

Fetch the page and name the qualities yourself; "make it like this" without saying what is not a usable instruction for a writer.

## 7. Voice

Record POV and tone in the brief, because both are invisible until a draft comes back wrong:

- **POV** — first person plural ("we"), second person ("you"), or third person. First person plural implies the writer speaks for the company: every "we" claim (we built, we've seen) must be true of the company. Don't let the writer invent company experience.
- **Tone** — e.g. professional and conversational.
- **Habits to ban** — the throat-clearing openers, filler transitions, and any words the user has flagged.
