# Choosing schema types

Last checked against Google Search Central on 2026-10-12. Google changes this list, so re-check
the gallery (https://developers.google.com/search/docs/appearance/structured-data/search-gallery)
when the date here is more than six months old.

## Decide in this order

1. **What does the visible page contain?** Types come from the page, not from the brief.
2. **What does the site already emit?** Extend it. Add only the missing nodes.
3. **Can the type earn a Google feature today?** If not, ship it only when it is cheap, accurate
   and the brief or user asked for it. Say in the report that it is machine-readable only.

## The table

| Type | Ship when | Google feature today | Notes |
|---|---|---|---|
| **BlogPosting** (or Article) | Always, on every post | Article is supported. No required properties; Google recommends headline, image, datePublished, dateModified, author | BlogPosting is a subtype of Article. Use it for pages under `/blog/` |
| **Person** (author) | A byline is visible | Supported inside Article | `name` holds the name only. Job title goes in `jobTitle`. Add `url` or `sameAs` pointing at a bio or profile |
| **Organization** (publisher) | Always, as `publisher` | Supported | Define once for the whole site and reference it by `@id` |
| **BreadcrumbList** | A breadcrumb trail is visible | Supported | Items match the visible trail, in order |
| **WebPage / WebSite** | The site's graph already uses them to connect nodes | None | Do not add them just to add them |
| **FAQPage** | A visible Q&A section exists and the brief or user wants it | **None.** Google stopped showing FAQ rich results on 2026-05-07 and removed Rich Results Test support in June 2026 | Still valid schema.org. Costs little, earns no SERP feature. Say so |
| **ItemList** | A visible list of 3 or more entries is the core of the page (roundups, ranked lists) | **None for software or tool lists.** Google's carousel covers only Course list, Movie, Recipe and Restaurant | Use plain entries with `name` and `url`. Never nest SoftwareApplication or Product in the entries |
| **VideoObject** | A video plays on the page | Supported | Needs `name`, `thumbnailUrl`, `uploadDate` |
| **HowTo** | Never by default | Not in Google's current gallery | Skip, even for tutorials, unless the user asks and accepts no SERP feature |
| **Review, AggregateRating, Product, SoftwareApplication, Offer** | Never on a roundup or a vendor-written comparison | SoftwareApplication needs `offers.price` plus a rating or review to qualify | A list entry has neither. Ratings on a page that ranks your own product are a trust risk. Block these in the validator |
| **Event** | The page is a webinar or event page | Supported | A blog post about an event is still a blog post |
| **QAPage** | User-submitted answers | Supported for forums | Editorial FAQs are FAQPage, not QAPage |
| **Speakable, Table, Dataset, Course, Recipe, JobPosting** | Wrong page type | | Skip |

## Brief versus draft

The brief says what the writer planned. The draft says what shipped. When they disagree, the draft
wins for anything the markup repeats, and you list the disagreement in the report.

Common disagreements:

- **FAQ count.** The brief plans 5 and the draft has 4. Mark up the 4 that are on the page.
- **List count.** The brief says "7 entries" and the draft numbers 2 to 5. The ItemList follows
  the visible numbers, so flag the numbering for the editor.
- **Dates.** The brief says "show a Last updated date" and the draft has none. `dateModified`
  stays a placeholder until the date is visible.
- **H1.** The brief offers two options and the draft uses a third. `headline` follows the draft.

## When the input is only a brief

Mark the output **PROVISIONAL**. FAQ answers in a brief are answer directions, not final text, and
markup that drifts from the published answer breaks the matching rule. Build the structure, write
the answers as the brief gives them, and tell the user to rerun the skill on the finished draft.
