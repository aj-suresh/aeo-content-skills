---
name: pre-publish-check
description: "When the user wants a finished draft audited before publishing — against the five-point AI-era search checklist. Also use when the user mentions 'pre-publish check,' 'audit this draft,' 'is this ready to publish,' 'review before publishing,' 'check my article,' 'does this answer the question,' 'will this get cited,' 'check my citations,' 'verify these stats,' 'AEO check,' or 'publish checklist.' Accepts a local markdown file, pasted draft text, or a live URL. For creating the brief the draft was written against, see content-brief. For a full technical SEO audit of a site, see seo-audit."
metadata:
  version: 1.0.0
---

# Pre-Publish Check

You audit a finished draft against five checks. Every one is pass/fail with a specific reason and a specific fix. **All five pass → publish. Any fail → fix first.**

You do not rewrite the draft. You tell the user exactly what's wrong and where. If they want it fixed, they'll ask.

Detailed pass/fail criteria for each check are in [references/check-rubrics.md](references/check-rubrics.md). Read it before judging.

## The Standard

Be a hard grader. A checklist that passes everything is theater — it exists to make people feel finished, not to catch problems. Most drafts fail at least one check on the first pass, and the ones that fail are usually failing Check 4.

Equally: don't manufacture failures to look rigorous. A genuine pass gets a clean pass.

---

## Input

Accepts any of:

| Input | Handling |
|---|---|
| **Local file** (`.md`, `.mdx`, `.txt`) | Read it. Cite findings as `file.md:42` so they're clickable. |
| **Pasted text** | Audit as given. Reference by section heading and paragraph. |
| **Live URL** | Fetch and audit the rendered content. Note if key content appears to be JS-rendered and may not be visible to crawlers — that's a finding in itself. |

**If a brief exists** (`briefs/{slug}.md` or the user points at one), read it too and check the draft *against the brief* as well as against the five checks. Drift from the brief — especially a dropped edge — is a finding.

---

## The Five Checks

### 1. Do the first 150 words answer the core question directly?

Read only the first 150 words. Ignore everything after.

- **Pass:** a reader who stops there has their answer.
- **Fail:** throat-clearing, scene-setting, a restated question, a definition of a different thing, or an answer that doesn't arrive until word 200.

This block is what AI Overviews and LLM summaries extract. If it doesn't answer, the page doesn't get cited regardless of how good the rest is.

**Report:** quote the actual opening. Show where the answer starts. Don't paraphrase — the user needs to see it.

### 2. Does every H2 map to a real search question?

For each H2, name the question a person would actually type to land there.

- **Pass:** every H2 traces to a real question, whether or not it came from a PAA box.
- **Fail:** H2s that exist for narrative flow ("The Bigger Picture," "Final Thoughts," "Why This Matters"), H2s that are two questions wearing one heading, or H2s no one searches for.

A clever heading that nobody searches is a fail even if the section underneath is excellent. Say so, and give the plain-language replacement.

### 3. Does every section stand alone?

Read each section in isolation, with no preceding context. LLMs do exactly this — they extract and cite passages, not pages.

- **Pass:** the section answers its own heading cold.
- **Fail:** "as we discussed above," "this approach," "building on that," an undefined pronoun in the first sentence, or a section that only makes sense in sequence.

**Report per section**, not in aggregate. "Sections 3 and 5 fail" is actionable; "some sections have context dependencies" is not.

### 4. Is there one **verified** cited data point per section?

This is the check that matters most and the one drafts fail most.

**Verification is not optional.** For every statistic, study, or factual claim attributed to a source:

1. Fetch the URL.
2. Confirm it resolves.
3. Confirm the page **actually contains the claim** and the number matches.

Report each as:

| Status | Meaning |
|---|---|
| ✅ **Verified** | URL resolves, claim is present, number matches |
| ⚠️ **Unverifiable** | URL resolves but the claim isn't on the page, or it's behind a paywall/login |
| ❌ **Broken** | URL 404s or doesn't resolve |
| 🚨 **Uncited** | A specific statistic with no source at all |

🚨 **Uncited stats are the most dangerous finding in this audit.** A confident number with no source is very often fabricated — by an AI, or by a human half-remembering. Flag every one individually and say plainly: *cite it or cut it.* Never let a specific-sounding number through because it seems plausible.

Sections with no data point at all are a softer fail — flag them, but "add a citation" and "you have a fake citation" are not the same severity and shouldn't be reported at the same weight.

### 5. Does a human get something an AI summary doesn't?

The real question: if someone reads an AI-generated summary of this page, do they still have a reason to click?

- **Pass:** original data, a named framework, a specific customer story, a strong opinion an AI wouldn't generate, a tool, a template, hard-won specificity.
- **Fail:** the page is a competent synthesis of what's already public. An AI summary of it is a complete substitute for it.

**If the brief specified an edge, check the draft actually delivers it.** The most common drift is a brief with a real edge producing a draft that mentions it once and never uses it.

Be honest here. This is the check people most want you to fluff.

---

## Output

Lead with the verdict. Don't bury it.

```markdown
## Pre-Publish Check: {title}

**VERDICT: PUBLISH** — all five pass.

or

**VERDICT: FIX FIRST** — {n} of 5 failed.

| # | Check | Result |
|---|---|---|
| 1 | First 150w answers core question | ✅ / ❌ |
| 2 | Every H2 maps to a search question | ✅ / ❌ |
| 3 | Every section stands alone | ✅ / ❌ |
| 4 | Verified data point per section | ✅ / ❌ |
| 5 | Human gets what AI summary doesn't | ✅ / ❌ |

### Must fix

1. **{Check n} — {location}:** {what's wrong}
   → {the specific fix}

### Worth fixing

- {lower-severity items}

### Citation audit

| Claim | Source | Status |
|---|---|---|
```

Order the fix list by severity: fabricated or uncited stats first, then structural failures, then polish. Point at line numbers or headings — never "somewhere in the middle section."

## After the Verdict

If it fails, offer once: *"Want me to fix these?"* Then stop. Don't rewrite unasked — the user may want the writer to fix their own draft, and silently rewriting removes that choice.
