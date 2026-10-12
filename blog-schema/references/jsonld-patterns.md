# JSON-LD patterns

One `<script type="application/ld+json">` per page holding one `@graph`. Every node that another
node points at gets an `@id`.

## Conventions

- **URLs:** absolute, and exactly as the page is served. Run `schema_check.py inspect` to see the
  canonical and the trailing-slash behaviour. If the site 301s `/post/` to `/post`, every `url`,
  `@id` and breadcrumb `item` uses `/post`.
- **@id style:** copy the site's existing pattern. If the site uses `https://example.com#organization`,
  do not introduce `https://example.com/#org`. Default for a new site:
  `{origin}/#organization`, `{origin}/#website`, `{url}#post`, `{url}#faq`, `{url}#list`.
- **Dates:** ISO 8601. `2026-10-12` is valid. Add a time and offset (`2026-10-12T09:00:00+05:30`)
  only when you know them. Do not invent `T00:00:00Z`.
- **Empty values:** leave the property out. No empty strings, no `null`.
- **Placeholders:** `TODO_WHAT_IS_NEEDED` as the whole string value. The validator fails on any
  string that starts with `TODO`.

## BlogPosting

```json
{
  "@type": "BlogPosting",
  "@id": "{url}#post",
  "headline": "{H1 exactly as shown}",
  "description": "{meta description}",
  "url": "{url}",
  "datePublished": "{original publish date, never reset on an update}",
  "dateModified": "{the visible Last updated date}",
  "author": { "@id": "{origin}/#author-{slug}" },
  "publisher": { "@id": "{origin}/#organization" },
  "image": { "@type": "ImageObject", "url": "{hero image URL}" },
  "inLanguage": "en",
  "mainEntityOfPage": { "@type": "WebPage", "@id": "{url}" },
  "about": { "@type": "Thing", "name": "{primary topic}", "sameAs": "{reference URL}" }
}
```

- `headline` equals the visible H1. If the H1 and the title tag differ, use the H1.
- `datePublished` is the date of first publication. Updating a post changes `dateModified` only.
- `dateModified` equals the date the page shows next to "Last updated". If the page shows none,
  the date is a placeholder and the report tells the editor to add the label.
- `image` points at a crawlable file. Google wants at least 50,000 pixels and one of the 16:9,
  4:3 or 1:1 ratios.
- `about` is optional. Include one entity at most, and only with a `sameAs` that resolves.

## Person (author)

```json
{
  "@type": "Person",
  "@id": "{origin}/#author-{slug}",
  "name": "{name only}",
  "jobTitle": "{title}",
  "url": "{bio page}",
  "sameAs": ["{LinkedIn URL}"]
}
```

`name` holds the name and nothing else: no title, no "by", no company. Use the byline that is
visible on the page. Never choose an author because the name sounds credible. If the brief asks
for a reviewer, add a `WebPage` node with `reviewedBy` pointing at a second Person. `reviewedBy`
is valid on WebPage, not on BlogPosting.

## Organization (publisher)

```json
{
  "@type": "Organization",
  "@id": "{origin}/#organization",
  "name": "{brand}",
  "url": "{origin}/",
  "logo": { "@type": "ImageObject", "url": "{logo URL}" },
  "sameAs": ["{LinkedIn company page}"]
}
```

Take every value from the site's existing JSON-LD or from the user. Never write them from memory.

## BreadcrumbList

```json
{
  "@type": "BreadcrumbList",
  "@id": "{url}#breadcrumb",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "Blog", "item": "{origin}/blog" },
    { "@type": "ListItem", "position": 2, "name": "{visible label}", "item": "{url}" }
  ]
}
```

The list mirrors the breadcrumb a visitor sees. If the page shows `Home > Blog > Post`, the list
has three items. If it shows `Back to Blog`, the list has two.

## FAQPage

```json
{
  "@type": "FAQPage",
  "@id": "{url}#faq",
  "url": "{url}",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "{question exactly as shown}",
      "acceptedAnswer": { "@type": "Answer", "text": "{answer exactly as shown}" }
    }
  ]
}
```

Rules:

1. Mark up only the visible FAQ section. A question that is an H2 elsewhere on the page does not
   belong here.
2. `name` and `text` equal the visible text. Copy it; do not paraphrase or shorten.
3. Plain text is safest. Links and lists survive as limited HTML (`<a>`, `<p>`, `<ul>`, `<ol>`,
   `<li>`, `<br>`, `<b>`, `<strong>`, `<i>`, `<em>`).
4. Draft files converted from Word often carry stray spaces inside words ("existi ng",
   "ge neralized"). Remove them when you copy, then confirm against the page with `--page`.
5. No offers, prices or calls to action inside an answer unless the page shows them in that answer.

## ItemList

```json
{
  "@type": "ItemList",
  "@id": "{url}#list",
  "name": "{what the list is}",
  "itemListOrder": "https://schema.org/ItemListUnordered",
  "numberOfItems": 7,
  "mainEntityOfPage": { "@id": "{url}" },
  "itemListElement": [
    {
      "@type": "ListItem",
      "position": 1,
      "name": "{entry name as the heading starts}",
      "description": "{the 'best for' line, exactly as shown}",
      "url": "{url}#{heading-id}"
    }
  ]
}
```

Rules:

1. `position` follows the visible numbering. If the page numbers the entries 2 to 5, fix the page
   or the numbers before you ship.
2. `itemListOrder` is `ItemListOrderAscending` only when the page ranks the entries. A list
   sorted alphabetically, or by category, is `ItemListUnordered`.
3. `name` is the entry's name as the heading shows it. `description` is optional and must be text
   from the page.
4. `url` is an in-page fragment. In Astro, Markdown headings get ids from `github-slugger`, which
   lowercases, drops punctuation, and joins words with hyphens. The validator derives the same ids
   from `.md` and `.mdx` files and warns when a fragment has no heading.
5. Entries stay plain. No `item` object, no SoftwareApplication, no Product, no rating.

## VideoObject

```json
{
  "@type": "VideoObject",
  "name": "{title}",
  "description": "{what the video shows}",
  "thumbnailUrl": "{image URL}",
  "uploadDate": "{ISO date}",
  "embedUrl": "{player URL}"
}
```

Only when the video plays on this page.

## Putting it together

```json
{
  "@context": "https://schema.org",
  "@graph": [ Organization, WebSite, Person, WebPage, BlogPosting, BreadcrumbList, FAQPage, ItemList ]
}
```

Order does not matter. Keep each type to one node unless the page really has two of them.
