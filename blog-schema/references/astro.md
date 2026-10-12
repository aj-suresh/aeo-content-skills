# Shipping the schema from an Astro site

## 1. Find out whether the site already emits a graph

```bash
grep -rn "ld+json" src/ | head
python3 scripts/schema_check.py inspect https://example.com/blog/some-post
```

Many Astro sites already build a graph in a layout or a `<SEO>` component. When one exists, extend
it. A second `BlogPosting` with a different `@id` gives crawlers two versions of the same page.

## 2. Emit the JSON safely

A component that every layout can reuse:

```astro
---
// src/components/JsonLd.astro
interface Props { graph: Record<string, unknown>[] }
const { graph } = Astro.props;
const json = JSON.stringify({ "@context": "https://schema.org", "@graph": graph })
  .replace(/</g, "\\u003c");
---
<script type="application/ld+json" set:html={json} />
```

- `set:html` stops Astro from escaping the quotes and breaking the JSON.
- The `replace` stops a `</script>` inside a FAQ answer from closing the tag early.
- `JSON.stringify` drops `undefined` values for you.

## 3. Keep one source for visible text and markup

Put the FAQ and the list entries in frontmatter, and render both the page section and the schema
from that data. The two cannot drift.

```yaml
# src/content/blog/example.md
updatedDate: 2026-10-12
faqs:
  - q: "Can I export my data if I cancel?"
    a: "Yes. You can export every project as CSV or JSON from Settings at any time, including after cancellation."
alternatives:
  - name: "Acme Boards"
    bestFor: "Best for small teams that want a simple kanban view"
    id: "acme-boards"
```

```ts
// src/content.config.ts
const blog = defineCollection({
  schema: z.object({
    // ...existing fields
    updatedDate: z.coerce.date().optional(),
    faqs: z.array(z.object({ q: z.string(), a: z.string() })).optional(),
    alternatives: z.array(z.object({
      name: z.string(), bestFor: z.string().optional(), id: z.string(),
    })).optional(),
  }),
});
```

In the layout, show the visible "Last updated" label from `updatedDate`, and build `dateModified`
from the same field.

## 4. Match the canonical URL

Schema URLs must equal the canonical. Astro's `trailingSlash` and `build.format` settings decide
whether `/post` or `/post/` is served. Build every schema URL from one helper, and the same helper
the `<link rel="canonical">` tag uses.

```ts
const canonical = new URL(Astro.url.pathname, Astro.site).href;
```

If the content plan says to 301 one form to the other, check that the redirect points the same way
as the site's `trailingSlash` setting. Opposite directions create a redirect loop.

## 5. Heading ids for ItemList fragments

Markdown headings get ids from `github-slugger` by default. A long heading makes a long id. For
short fragments, write the heading as HTML (`<h3 id="acme-boards">...</h3>`) or add a remark plugin
that reads `{#acme-boards}` suffixes. Then build the ItemList `url` from the same `id` field.

## 6. Verify the built output

```bash
npm run build
python3 scripts/schema_check.py validate dist/blog/some-post/index.html --page src/content/blog/some-post.md
```

Then paste the live URL into https://validator.schema.org. Google's Rich Results Test no longer
evaluates FAQPage, so it cannot confirm that type. Use it for the Article and Breadcrumb nodes.
After deploy, watch Search Console's Enhancements reports for errors on those two.
