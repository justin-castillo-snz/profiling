---
name: lint
description: Lint the business profiling wiki after new data lands. Refreshes wiki/index.md and updates the provisional analyses (profiling approaches and practices) from pages added or changed since the last lint. Use when the user asks to lint, refresh the index, or bring the analyses up to date.
---

# Lint the profiling wiki

Follow [AGENTS.md](../../../AGENTS.md) for the standing rules (evidence and citation, confidentiality, scope). This skill never reads or changes `raw/` and never deploys.

## 1. Find the new data

- Find the most recent `## [date] lint | ...` heading in `wiki/log.md`. If there is none, start from the first entry.
- New data is the pages added or changed since then: take the **Added** and **Changed** lists of every later log entry, and cross-check with `git log --since=<date> --name-only -- wiki/` and `git status`.
- If nothing is new, say so, still refresh the index (step 2) and stop.
- Read each new or changed page in full before using it.

## 2. Refresh `wiki/index.md`

- List every page under `wiki/` exactly once, in its section: Sources and comparisons, Concepts and units, or the Country evidence table. Keep the intro and the log link.
- Add missing pages, remove entries for deleted pages, and rewrite one-line descriptions that no longer match the page's scope, period or source.
- Keep the existing style: relative links, one line each, dated evidence labelled as such.
- This step is mechanical and can be applied directly.

## 3. Draft updates to the provisional analyses

Compare the new data with [profiling-approaches.md](../../../wiki/analyses/profiling-approaches.md) and [profiling-practices.md](../../../wiki/analyses/profiling-practices.md).

**Approaches** (same rules as step 6 of the [ingest-source skill](../ingest-source/SKILL.md)):

1. Identify each office's approach from the changed pages.
2. Add a new general approach only if it differs substantially in starting evidence, decision rule or output; otherwise record a variant of the matching approach.
3. Add or update the office's row in **Country approaches** with source, section and reference date; use "approach not identified" when the source does not say how units are formed.
4. Put ambiguous single passages under open questions, not general approaches.

**Practices:** add or revise comparison rows and the "Questions for later sources" where the new data gives contrasting evidence or answers a question.

Also check the changed pages for terms missing from the [glossary](../../../wiki/concepts/glossary.md) (new acronyms, or a known term used differently) and propose entries; glossary additions follow the same approval gate as the analyses. Also check the changed pages for contradictions with earlier evidence, stale claims, missing cross-links and answered or newly raised questions. Keep source evidence, user notes, interpretation and implications for Stats NZ distinct, and never present one office's practice as a universal rule.

## 4. Approval gate

**Do not edit the analyses yet.** Present a summary of proposed changes: page, section, current text → proposed text, and the evidence (page and source section) for each. Include any contradictions found. Wait for the user to approve, amend or reject. Then apply only what was approved.

Mechanical fixes (index entries, broken links, missing back-links) do not need approval; list them in the report.

## 5. Log

Append `## [YYYY-MM-DD] lint | Short title` to `wiki/log.md` with `### Added`, `### Changed` and `### Removed` sections. Link the affected pages, write `None.` for an empty category, and never rewrite earlier entries.

## 6. Verify

From the repository root:

```
python .github/skills/ingest-source/check_links.py
```

Fix problems and rerun until it prints `OK`.

## 7. Report

Summarise: the new data found, index changes, analysis changes applied or declined, contradictions and open questions. Do not claim coverage of anything you did not read.

## Pitfalls

- Do not use `raw/` as the source of new data; lint works from wiki pages only. Ingesting new documents is the job of the ingest-source skill.
- A shared tool, LCU or contact mode is not evidence two offices use the same delineation method.
- Heading anchors change when headings are renamed; rerun the checker after edits.
