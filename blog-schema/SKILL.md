---
name: blog-schema
description: "When the user wants JSON-LD structured data (schema markup) for a blog post, built from a content brief or a draft. Also use when the user mentions 'what schema should I add,' 'schema for this post,' 'generate JSON-LD,' 'structured data for this draft,' 'FAQ schema,' 'FAQPage,' 'BlogPosting,' 'Article schema,' 'ItemList schema,' 'schema spec from the brief,' 'hand to the schema skill,' or 'add schema before publishing.' Reads the brief's schema spec or the draft itself, checks what the live page already emits, picks the types the page earns, and writes one validated @graph that matches the visible text. For writing the brief, see content-brief. For auditing the draft, see pre-publish-check. For a whole-site schema audit, see seo-audit."
metadata:
  version: 1.0.0
---

# Blog Schema

You turn a content brief or a blog draft into JSON-LD that describes the page exactly as it will be
published. You decide which types the page earns, you reuse what the site already emits, and you
prove the result with a validator before you hand it over.

## The Non-Negotiable

**Schema describes visible content.** Every headline, question, answer, date and list entry in the
markup must appear on the page. If you cannot point at the visible text a node comes from, that
node does not ship.

The corollary: **you never invent a fact.** A missing author, date, image or logo becomes a
`TODO_...` placeholder and appears in the report under "Needs from you". The validator fails on
every placeholder, so none can reach production by accident.

## Say what the markup will and will not do

Google ended FAQ rich results on 2026-05-07, and its carousel feature covers only courses, movies,
recipes and restaurants, so a list of software tools gets no feature. Article and Breadcrumb
markup still count. Tell the user which types can earn a Google feature and which only make the
page easier for machines to read. Do not promise traffic from the second group.

Details and sources: [references/type-selection.md](references/type-selection.md).

---

## Input

| You get | Handling |
|---|---|
| **A content brief** (.docx, .md, pasted, Google Doc, SharePoint) | Read its Schema section, FAQ table and outline. Mark the output **PROVISIONAL**: brief answers are directions, not final text |
| **A draft** | The source of truth for every visible string |
| **Both** | The draft wins for visible facts. List every disagreement with the brief |
| **A live URL** | Run `inspect` (Step 2) and read the existing JSON-LD |

Read the file with whatever access you have: a local path, an export, a connector, pasted text.
Text pulled from Word often has stray spaces inside words and numbering that the converter
dropped. Clean the spacing when you copy, and flag numbering you cannot confirm.

## The Pipeline

### Step 1: Collect the page facts

Find each of these in the draft, then fill gaps from the brief:

| Fact | Where it comes from |
|---|---|
| Canonical URL | Brief or user, then confirm in Step 2 |
| H1 | The draft's visible H1 |
| Meta description | The draft or brief |
| Original publish date | The live page, if the post is an update |
| Visible "Last updated" date | The draft. Missing means a placeholder |
| Author, and reviewer if the brief names one | The visible byline |
| Hero image URL | The live page or the user |
| FAQ questions and answers | The visible FAQ section only |
| List entries | The numbered or named entries the page is built around |
| Embedded video | The draft |

Ask the user for anything that is neither in the files nor on the live page. Do not stall on it:
build the rest and leave a placeholder.

### Step 2: Check what the site already emits

If the page is live, or a sibling post is, run:

```bash
python3 scripts/schema_check.py inspect <url>
```

It prints the canonical, the redirect behaviour of the trailing-slash twin, the visible dates,
and every JSON-LD node with its `@id`. Three findings change your plan:

1. **A graph already exists.** Extend it. Reuse its `@id` values, add only the missing nodes,
   update values that changed, and never emit a second `BlogPosting` or `Organization`.
2. **The served URL differs from the URL in the brief.** Use the served one. Flag the conflict:
   a content plan that redirects the other way creates a loop.
3. **Nodes without an `@id`**, such as a floating Person. Give them one so nodes can reference
   each other.

For a post that is not live yet, inspect a published sibling to learn the site's `@id` style,
organization values and author pattern.

### Step 3: Choose the types

Use [references/type-selection.md](references/type-selection.md). The short version:

- **Always:** BlogPosting, the author Person, the publisher Organization, BreadcrumbList.
- **When the page earns it:** FAQPage for a visible Q&A section, ItemList for a visible list of
  three or more entries, VideoObject for a playing video.
- **Never on a roundup:** Review, AggregateRating, Product, SoftwareApplication, Offer.
- **Skip by default:** HowTo.

Write down every type you skipped and the reason. The user will ask.

### Step 4: Build the graph

Use [references/jsonld-patterns.md](references/jsonld-patterns.md). One `@graph`, `@id` on every
node that is referenced, absolute URLs as served, ISO 8601 dates, no empty values.

Copy visible text exactly. For an update, `datePublished` keeps the original date and
`dateModified` takes the visible "Last updated" date.

### Step 5: Validate and fix

```bash
python3 scripts/schema_check.py validate schema/{slug}.json --page drafts/{slug}.md
```

`--page` takes a `.md`, `.mdx` or `.txt` copy of the visible page. With it the checker confirms
that every FAQ question and answer, every list entry, the headline and the dates appear in the
text, and that ItemList fragments match heading ids. Without it, only structure is checked, and
you say so in the report.

Fix every ERROR. Run with `--allow-todo` only while you wait on inputs, and report the status as
blocked until the placeholders are filled.

### Step 6: Write the file and the report

Write the bare JSON (no `<script>` tag) to `schema/{slug}.json` and say where before you write.
Then report in this shape:

```
## Schema for {title}
Page: {url} | Input: {brief | draft | both} | Status: READY | PROVISIONAL | BLOCKED (n placeholders)

Ships:    {type}: {what it carries}. {Google feature | machine-readable only}
Skipped:  {type}: {reason}
Already on the page:   {nodes the site emits today}
Changes to existing:   {value}: {old} -> {new}
Mismatches:            {brief vs draft vs live, one line each}
Needs from you:        {placeholder or decision, one line each}
Validation:            {n errors, n warnings; text-match checked or skipped}
File:                  schema/{slug}.json
```

Keep each line short. "Mismatches" and "Needs from you" are the lines the user acts on, so put
the specific thing there, such as "Brief plans 5 FAQs; the draft has 4. Marked up 4."

Then offer the implementation. For Astro, see [references/astro.md](references/astro.md).

---

## Rules that catch real mistakes

- **Match the page, not the plan.** A brief lists five FAQs and the draft has four: mark up four.
- **Do not duplicate the page into FAQ markup.** Only the visible FAQ section goes in.
- **Respect the brief's exclusions.** If it says no Review or rating markup on the entry for your
  own product, the validator already blocks those types. Keep it that way.
- **Names and titles stay separate.** `author.name` holds a name. A job title goes in `jobTitle`.
- **A visible date is a promise.** If `dateModified` says October 12, the page shows October 12.
- **Take the author from the visible byline.** Never pick one because the name sounds credible.
  If the page shows no byline, ask.
- **Test what you ship.** Rich Results Test no longer evaluates FAQPage. Use
  https://validator.schema.org for every type and Search Console for Article and Breadcrumb.

## Related skills

- **content-brief** writes the brief whose Schema section this skill implements.
- **pre-publish-check** audits the draft. Run it before this skill so the visible text is final.
- **internal-linking** edits the draft. Run it first as well, since links can change answer text.
- **seo-audit** reviews structured data across a whole site.
