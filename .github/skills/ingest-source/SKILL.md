---
name: ingest-source
description: Ingest one user-selected source from raw/ into the business profiling wiki. Use when the user asks to ingest, process or add a document (PDF, Markdown notes, etc.) to the wiki, including country accounts and profiling approaches.
---

# Ingest a source into the profiling wiki

Follow [AGENTS.md](../../../AGENTS.md) for the standing rules (evidence and citation, confidentiality, scope). This skill holds the full ingest procedure and conventions.

## 1. Prepare the source

- **If the source is a PDF:** convert it to Markdown with the `convert-pdf-to-md` skill and keep the result, with its assets, under `raw/md/<source-name>/`. Read the Markdown, not the PDF. The conversion is a reading copy, not a second source.
- For a single PDF, `-o` is the exact destination and the converter replaces it if it exists. Verify it is a new, source-specific folder (for example `raw/md/WBG - Statistical Units/`), never the shared `raw/md/` directory. Reuse an existing reading copy rather than overwriting it.
- **Otherwise** (for example the user's Markdown notes): read it in place. No conversion.
- Never edit, rename or delete anything in `raw/` except to add the reading copy under `raw/md/`.
- Read the **whole** document, including annexes, boxes, tables and footnotes. Country examples can be anywhere, not only in the profiling chapter. For long files, search the reading copy for key terms (`top-down`, `bottom-up`, `profil`, country names) to catch passages you would otherwise miss.

## 2. Identify the source

Record the issuer, edition or date, reference period, scope, units covered and limitations. If any is unknown, say so. User notes are analyst interpretation, not a published source: label them as such.

## 3. Write the source note

Create `wiki/sources/<kebab-name>.md` naming the original file and reading copy in plain text (never link into `raw/`; it is git-ignored and the wiki is published), a section-by-section evidence guide with page or section references, and limitations. Keep what the source says separate from what it might mean for profiling.

## 4. Update concepts and units

- Search `wiki/index.md` and the existing pages for each concept the source covers. Integrate into the existing page, not a near-duplicate.
- If the source uses a familiar concept differently, put both usages in the **same section**. Cite each and explain the difference in unit, purpose or period; do not silently replace the older definition.
- Add new pages only for new concepts, using the layout: source notes in `wiki/sources/`, methods and processes in `wiki/concepts/`, statistical units in `wiki/units/`, reusable comparisons in `wiki/analyses/`. Use relative Markdown links.
- For adjacent topics such as LCUs, distinguish profiling itself from work that uses a profile or triggers its revision.

## 5. Update country pages

- One cumulative page per country in `wiki/countries/`: add each practice with its source, period and section, and keep earlier evidence.
- Link each practice to the concept or unit page that explains it, and link back from that page.
- Distinguish regional method, national implementation, trial, proposal and analyst comparison.

## 6. Update the approaches catalogue

Update [profiling-approaches.md](../../../wiki/analyses/profiling-approaches.md):

1. Identify each office's approach from the source.
2. Compare it with **General approaches**. If it is substantially different in starting evidence, decision rule or output, add a new general approach with its source. Otherwise record it as a variant or tweak of the matching approach, noting the tweak.
3. Add or update the office's row in **Country approaches** in either case, with source, section and reference date. If the source does not say how units are formed, list the office under "approach not identified".
4. Do not add a general approach from one ambiguous passage; put it under open questions.
5. Cite by source, period and section, and cross-link the country page.

## 7. Index and log

- Add every new page to `wiki/index.md` with a one-line description. Update descriptions that have changed.
- Append the log entry as `## [YYYY-MM-DD] ingest | Short title` with `### Added`, `### Changed` and `### Removed` sections. Link the affected pages, write `None.` for an empty category, and never rewrite earlier entries.

## 8. Verify

Run the link checker from the repository root:

```
python .github/skills/ingest-source/check_links.py
```

It checks relative links, heading anchors and that every wiki page is in the index. Fix problems and rerun until it prints `OK`.

## 9. Report

Summarise the scope and key findings, the pages changed, conflicts with earlier evidence, and open questions, keeping source evidence, user notes and interpretation distinct. Do not say the source was fully reviewed if any part was unreadable.

## Pitfalls

- `apply_patch` does not roll back a partly failed batch. Re-view the files before reapplying.
- Sources can disagree internally, for example prose versus table counts. Record both and mark the issue unresolved.
- Do not treat authorship, a trial roster or an LCU's existence as proof that an office uses a given method.
- Wiki links are relative, and heading anchors change when headings are renamed. Rerun the checker after renaming.
