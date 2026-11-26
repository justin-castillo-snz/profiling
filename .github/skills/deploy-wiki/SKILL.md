---
name: deploy-wiki
description: Publish pending wiki changes to the public GitHub Pages site. Use when the user asks to deploy, publish, push or release the wiki after ingests or edits.
---

# Deploy the wiki

Pushing to `main` triggers `.github/workflows/pages.yml`, which builds with `mkdocs build --strict` and publishes to https://justin-castillo-snz.github.io/profiling/. Only `wiki/` is published; `raw/` is git-ignored and must never be linked from wiki pages.

## 1. Check links

From the repository root:

```powershell
python .github/skills/ingest-source/check_links.py
```

Fix anything reported and rerun until it prints `OK`.

## 2. Strict build

Reuse `.venv` if it exists, otherwise `python -m venv .venv` then `.venv\Scripts\python.exe -m pip install -r requirements.txt`. Run MkDocs through `python -m` because `mkdocs.exe` can be blocked by group policy.

```powershell
$env:NO_MKDOCS_2_WARNING = '1'
.\.venv\Scripts\python.exe -m mkdocs build --strict
```

Fix every warning; the same build runs in CI and a warning fails the deploy.

- **Link into `raw/`:** replace it with a plain-text filename citation.
- **Link to a file outside `wiki/`** (for example `AGENTS.md`): use the absolute `https://github.com/justin-castillo-snz/profiling/blob/main/...` URL.
- **"not included in the nav" INFO:** add each new page to `nav` in `mkdocs.yml`, under its folder's section, so it appears in the sidebar.

## 3. Commit and push

```powershell
git status --short
git add -A
git commit -m "<what changed, e.g. Ingest <source> into wiki>" -m "Co-authored-by: Copilot <223556219+Copilot@users.noreply.github.com>"
git push origin main
```

Confirm `git status --short` shows nothing unexpected before committing (`raw/`, `site/` and `.venv/` are ignored). If the push asks for credentials in a non-interactive shell, stop and ask the user to run `git push origin main` themselves.

## 4. Confirm

After about a minute, check the Actions run for "Deploy wiki to GitHub Pages" and open the site. Pages must have Source set to **GitHub Actions** (Settings > Pages); if the site still shows a plain Jekyll page, that setting is the cause.
