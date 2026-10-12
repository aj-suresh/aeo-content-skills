#!/usr/bin/env python3
"""blog-schema checker. Standard library only.

  schema_check.py inspect URL
      Show what a live page already emits: status, redirect behaviour of the
      trailing-slash twin, canonical, H1, visible dates, and every JSON-LD node.

  schema_check.py validate SOURCE [--page FILE] [--allow-todo]
      SOURCE is a .json file, a .html file, or an http(s) URL.
      Checks structure and required properties per type. With --page (a .md,
      .mdx or .txt copy of the visible page), also checks that every FAQ
      question and answer, list entry, headline and date appears in the text.

Exit code 1 when any ERROR is found.
"""
import argparse
import json
import re
import sys
import unicodedata
import urllib.error
import urllib.request

UA = {"User-Agent": "Mozilla/5.0 (blog-schema checker)"}
LD_RE = re.compile(r"<script[^>]*application/ld\+json[^>]*>(.*?)</script>", re.S | re.I)
ISO_RE = re.compile(
    r"^\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2}(\.\d+)?)?(Z|[+-]\d{2}:?\d{2})?)?$"
)
ARTICLE = {"Article", "BlogPosting", "NewsArticle", "TechArticle"}
BANNED = {"Review", "AggregateRating", "Product", "SoftwareApplication", "Offer"}
SINGLETONS = {"BlogPosting", "Article", "WebPage", "WebSite", "Organization"}
MONTHS = ["january", "february", "march", "april", "may", "june", "july",
          "august", "september", "october", "november", "december"]


# ---------------------------------------------------------------- fetching
class _NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        return None


def fetch(url, follow=True):
    opener = (urllib.request.build_opener() if follow
              else urllib.request.build_opener(_NoRedirect))
    try:
        with opener.open(urllib.request.Request(url, headers=UA), timeout=30) as r:
            return r.status, r.geturl(), r.headers, r.read().decode("utf-8", "ignore")
    except urllib.error.HTTPError as e:
        return e.code, url, e.headers, ""


def blocks_from_html(html):
    blocks, bad = [], 0
    for raw in LD_RE.findall(html):
        try:
            blocks.append(json.loads(raw))
        except json.JSONDecodeError:
            bad += 1
    return blocks, bad


def flatten(data):
    out = []

    def walk(d):
        if isinstance(d, list):
            for x in d:
                walk(x)
        elif isinstance(d, dict):
            if "@graph" in d:
                walk(d["@graph"])
            else:
                out.append(d)

    walk(data)
    return out


def types_of(node):
    t = node.get("@type", [])
    return t if isinstance(t, list) else [t]


def strip_tags(s):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", s)).strip()


# ----------------------------------------------------------------- inspect
def cmd_inspect(url):
    status, final, hdr, html = fetch(url)
    print(f"GET {url} -> {status}; final URL {final}")
    twin = url[:-1] if url.endswith("/") else url + "/"
    s2, _, h2, _ = fetch(twin, follow=False)
    loc = h2.get("Location") if h2 else None
    print(f"Twin {twin} -> {s2}" + (f" (Location: {loc})" if loc else ""))

    for tag in re.findall(r"<link\b[^>]*>", html, re.I):
        if re.search(r"rel=[\"']canonical[\"']", tag, re.I):
            m = re.search(r"href=[\"']([^\"']+)", tag, re.I)
            print("Canonical:", m.group(1) if m else "(no href)")
    print("H1:", [strip_tags(h) for h in re.findall(r"<h1[^>]*>(.*?)</h1>", html, re.S | re.I)][:2])
    alts = [(re.search(r"hreflang=[\"']([^\"']+)", t, re.I), re.search(r"href=[\"']([^\"']+)", t, re.I))
            for t in re.findall(r"<link\b[^>]*rel=[\"']alternate[\"'][^>]*>", html, re.I)]
    alts = [(a.group(1), b.group(1)) for a, b in alts if a and b]
    if alts:
        print("hreflang siblings (each has its own page and its own schema):",
              ", ".join(lang for lang, _ in alts))
    article = re.search(r"<article\b.*?</article>", html, re.S | re.I)
    ids = re.findall(r"<h[23][^>]*\sid=[\"']([^\"']+)", article.group(0) if article else html, re.I)
    print("Heading ids in the article (first 4):", ids[:4] or "none; headings carry no ids")

    body = re.sub(r"<(script|style)\b.*?</\1>", " ", html, flags=re.S | re.I)
    text = strip_tags(body)
    dates = re.findall(r"(?:Last updated|Updated|Published)?[:\s]*"
                       r"([A-Z][a-z]{2,8}\.? \d{1,2}, \d{4}|\d{1,2} [A-Z][a-z]{2,8} \d{4})", text)
    print("Visible dates (first 5):", dates[:5] or "none found")
    print("Has 'Last updated' label:", bool(re.search(r"last\s+updated", text, re.I)))

    blocks, bad = blocks_from_html(html)
    print(f"JSON-LD blocks: {len(blocks)}" + (f" ({bad} unparseable)" if bad else ""))
    nodes = [n for b in blocks for n in flatten(b)]
    for n in nodes:
        line = f"  - {'/'.join(types_of(n))}  @id={n.get('@id', '(none)')}"
        if set(types_of(n)) & ARTICLE:
            line += (f"  headline={n.get('headline')!r}  published={n.get('datePublished')}"
                     f"  modified={n.get('dateModified')}")
        print(line)
    flags = []
    if final.rstrip("/") == url.rstrip("/") and final != url:
        flags.append(f"{url} redirects to {final}; use the served URL in every schema url and @id")
    if not nodes:
        flags.append("page emits no JSON-LD")
    if sum(1 for n in nodes if set(types_of(n)) & ARTICLE) > 1:
        flags.append("more than one article node")
    floating = [t for n in nodes if "@id" not in n for t in types_of(n)
                if t in {"Person", "ImageObject", "BreadcrumbList"}]
    if floating:
        flags.append("nodes without @id (cannot be referenced): " + ", ".join(floating))
    for f in flags:
        print("FLAG:", f)


# ---------------------------------------------------------------- validate
def norm(s):
    s = unicodedata.normalize("NFKC", str(s))
    for a, b in (("’", "'"), ("‘", "'"), ("“", '"'), ("”", '"'),
                 ("–", "-"), ("—", "-"), (" ", " ")):
        s = s.replace(a, b)
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>|]", "", s)
    return re.sub(r"\s+", "", s).lower()


def github_slugs(md):
    seen, slugs = {}, set()
    for m in re.finditer(r"^#{1,6}\s+(.+?)\s*$", md, re.M):
        h = m.group(1)
        custom = re.search(r"\{#([\w-]+)\}\s*$", h)
        if custom:
            slugs.add(custom.group(1))
            continue
        h = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", h)
        s = re.sub(r"[^\w\- ]+", "", h.strip().lower().replace("*", "")).replace(" ", "-")
        n = seen.get(s, 0)
        seen[s] = n + 1
        slugs.add(s if n == 0 else f"{s}-{n}")
    return slugs


def date_forms(iso):
    y, m, d = iso[:10].split("-")
    month, day = MONTHS[int(m) - 1], int(d)
    forms = [f"{month} {day}, {y}", f"{month[:3]} {day}, {y}", f"{month[:3]}. {day}, {y}",
             f"{day} {month} {y}", f"{day} {month[:3]} {y}", f"{y}-{m}-{d}",
             f"{month} {d}, {y}"]
    return {norm(f) for f in forms}


class Report:
    def __init__(self, allow_todo):
        self.errors, self.warns, self.allow_todo = [], [], allow_todo

    def err(self, msg):
        self.errors.append(msg)

    def warn(self, msg):
        self.warns.append(msg)

    def todo(self, msg):
        (self.warns if self.allow_todo else self.errors).append(msg)


def walk_all(obj, path=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from walk_all(v, f"{path}.{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from walk_all(v, f"{path}[{i}]")
    else:
        yield path, obj


def need(r, node, label, *props):
    for p in props:
        v = node.get(p)
        if v in (None, "", [], {}):
            r.err(f"{label}: missing {p}")


def is_iso(r, label, key, val):
    if isinstance(val, str) and val.strip().upper().startswith("TODO"):
        return False  # reported once as a placeholder by check_values
    if not isinstance(val, str) or not ISO_RE.match(val):
        r.err(f"{label}: {key} is not ISO 8601 ({val!r})")
        return False
    return True


def check_nodes(r, nodes):
    for n in nodes:
        ts = set(types_of(n))
        label = "/".join(sorted(ts)) or "(no @type)"
        if not ts:
            r.err("node without @type")
            continue
        if ts & BANNED:
            r.err(f"{label}: type not allowed on a blog or roundup page")
        if ts & ARTICLE:
            need(r, n, label, "headline", "datePublished", "dateModified", "image",
                 "author", "publisher", "mainEntityOfPage")
            pub, mod = n.get("datePublished"), n.get("dateModified")
            ok_p = is_iso(r, label, "datePublished", pub) if pub else False
            ok_m = is_iso(r, label, "dateModified", mod) if mod else False
            if ok_p and ok_m and mod[:10] < pub[:10]:
                r.err(f"{label}: dateModified is earlier than datePublished")
            a = n.get("author")
            for au in (a if isinstance(a, list) else [a] if a else []):
                if not isinstance(au, dict) or len(au) == 1:
                    continue  # a bare @id reference; the Person node is checked on its own
                if not (au.get("url") or au.get("sameAs")):
                    r.warn(f"{label}: author {au.get('name')!r} has no url or sameAs")
                if re.search(r",|\b(COO|CEO|CTO|Dr\.|PhD)\b", str(au.get("name", ""))):
                    r.warn(f"{label}: author name holds a title; use jobTitle")
        if "Person" in ts:
            need(r, n, "Person", "name")
        if "Organization" in ts:
            need(r, n, "Organization", "name", "url", "logo")
        if "BreadcrumbList" in ts:
            items = n.get("itemListElement") or []
            if not items:
                r.err("BreadcrumbList: itemListElement is empty")
            for i, it in enumerate(items, 1):
                if it.get("position") != i:
                    r.err(f"BreadcrumbList: position {it.get('position')} should be {i}")
                if not it.get("name"):
                    r.err(f"BreadcrumbList: item {i} has no name")
                if i < len(items) and not it.get("item"):
                    r.err(f"BreadcrumbList: item {i} has no item URL")
        if "FAQPage" in ts:
            qs = n.get("mainEntity") or []
            if not qs:
                r.err("FAQPage: mainEntity is empty")
            names = []
            for q in qs:
                name = q.get("name")
                ans = (q.get("acceptedAnswer") or {}).get("text")
                if q.get("@type") != "Question" or not name or not ans:
                    r.err(f"FAQPage: malformed Question ({name!r})")
                    continue
                names.append(name)
                if len(ans) < 40:
                    r.warn(f"FAQPage: very short answer for {name!r}")
            if len(set(names)) != len(names):
                r.err("FAQPage: duplicate questions")
        if "ItemList" in ts:
            items = n.get("itemListElement") or []
            if not items:
                r.err("ItemList: itemListElement is empty")
            if n.get("numberOfItems") not in (None, len(items)):
                r.err(f"ItemList: numberOfItems={n.get('numberOfItems')} but {len(items)} entries")
            for i, it in enumerate(items, 1):
                if it.get("position") != i:
                    r.err(f"ItemList: position {it.get('position')} should be {i}")
                if not it.get("name"):
                    r.err(f"ItemList: entry {i} has no name")
                if isinstance(it.get("item"), dict):
                    r.err(f"ItemList: entry {i} nests an item object; use name and url only")
        if "VideoObject" in ts:
            need(r, n, "VideoObject", "name", "thumbnailUrl", "uploadDate")


def check_graph(r, nodes, data):
    ids, refs = set(), []

    def collect(o):
        if isinstance(o, dict):
            if "@id" in o:
                if len(o) > 1:
                    ids.add(o["@id"])
                else:
                    refs.append(o["@id"])
            for v in o.values():
                collect(v)
        elif isinstance(o, list):
            for v in o:
                collect(v)

    collect(data)
    for ref in sorted(set(refs) - ids):
        r.warn(f"@id {ref} is referenced but not defined here (fine if another page defines it)")
    top = [n["@id"] for n in nodes if "@id" in n]
    for i in {x for x in top if top.count(x) > 1}:
        r.err(f"duplicate @id {i}")
    for t in SINGLETONS:
        same = {n.get("@id") for n in nodes if t in types_of(n)}
        if len(same) > 1:
            r.warn(f"{len(same)} different {t} nodes; keep one")


def check_values(r, data):
    for path, v in walk_all(data):
        if isinstance(v, str):
            if v.strip().upper().startswith("TODO"):
                r.todo(f"placeholder left in {path}: {v[:50]!r}")
            key = path.rsplit(".", 1)[-1].split("[")[0]
            if key in {"url", "item", "thumbnailUrl", "contentUrl"} and not re.match(r"^https?://", v):
                r.err(f"{path} is not an absolute URL: {v!r}")
        elif v is None:
            r.err(f"null value at {path}")


def check_page(r, nodes, page_path):
    raw = open(page_path, encoding="utf-8").read()
    text = norm(raw)

    def seen(s):
        return norm(s) in text

    for n in nodes:
        ts = set(types_of(n))
        if ts & ARTICLE:
            if n.get("headline") and not seen(n["headline"]):
                r.err(f"headline not found in page text: {n['headline'][:70]!r}")
            mod, pub = n.get("dateModified"), n.get("datePublished")
            if mod and ISO_RE.match(str(mod)):
                if not any(f in text for f in date_forms(mod)):
                    r.err(f"dateModified {mod[:10]} is not visible on the page in any common format")
                if not re.search(r"updated", raw, re.I):
                    r.warn("no 'Last updated' label found on the page")
            if pub and ISO_RE.match(str(pub)) and not any(f in text for f in date_forms(pub)):
                r.warn(f"datePublished {pub[:10]} is not visible on the page")
        if "FAQPage" in ts:
            for q in n.get("mainEntity") or []:
                if not seen(q.get("name", "")):
                    r.err(f"FAQ question not on the page: {q.get('name', '')[:70]!r}")
                ans = (q.get("acceptedAnswer") or {}).get("text", "")
                if ans and not seen(ans):
                    r.err(f"FAQ answer differs from page text: {q.get('name', '')[:60]!r}")
        if "ItemList" in ts:
            slugs = github_slugs(raw) | set(re.findall(r"""id=["']([\w-]+)["']""", raw))
            for it in n.get("itemListElement") or []:
                if it.get("name") and not seen(it["name"]):
                    r.err(f"ItemList entry not on the page: {it['name'][:70]!r}")
                if it.get("description") and not seen(it["description"]):
                    r.err(f"ItemList description not on the page: {it['description'][:70]!r}")
                u = it.get("url", "")
                if "#" in u and u.split("#", 1)[1] not in slugs:
                    r.warn(f"ItemList url fragment not matched to a heading id: {u.split('#', 1)[1][:70]}")


def cmd_validate(source, page, allow_todo):
    if re.match(r"^https?://", source):
        _, _, _, html = fetch(source)
        blocks, bad = blocks_from_html(html)
    elif source.endswith((".html", ".htm")):
        blocks, bad = blocks_from_html(open(source, encoding="utf-8").read())
    else:
        blocks, bad = [json.load(open(source, encoding="utf-8"))], 0
    r = Report(allow_todo)
    if bad:
        r.err(f"{bad} JSON-LD block(s) failed to parse")
    if not blocks:
        r.err("no JSON-LD found")
    for b in blocks:
        if isinstance(b, dict) and "@context" not in b:
            r.err("top-level object has no @context")
        nodes = flatten(b)
        check_values(r, b)
        check_nodes(r, nodes)
        check_graph(r, nodes, b)
        if page:
            check_page(r, nodes, page)
    for w in r.warns:
        print("WARN ", w)
    for e in r.errors:
        print("ERROR", e)
    print(f"\n{len(r.errors)} error(s), {len(r.warns)} warning(s)"
          + ("" if page else "  (no --page given: text-match checks skipped)"))
    sys.exit(1 if r.errors else 0)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    i = sub.add_parser("inspect")
    i.add_argument("url")
    v = sub.add_parser("validate")
    v.add_argument("source")
    v.add_argument("--page")
    v.add_argument("--allow-todo", action="store_true")
    a = p.parse_args()
    if a.cmd == "inspect":
        cmd_inspect(a.url)
    else:
        cmd_validate(a.source, a.page, a.allow_todo)


if __name__ == "__main__":
    main()
