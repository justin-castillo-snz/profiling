# Business profiling wiki

A public wiki on business profiling: how statistical offices identify and maintain profiles of large, complex businesses. Published at <https://justin-castillo-snz.github.io/profiling/>.

## Repository

- `wiki/` holds the published Markdown. Start at [wiki/index.md](wiki/index.md).
- `AGENTS.md` holds the working agreements for maintaining the wiki.
- `raw/` holds original sources and reading copies. It is git-ignored and never published.
- `mkdocs.yml` configures the site. `.github/workflows/pages.yml` builds it with `mkdocs build --strict` and deploys to GitHub Pages on each push to `main`.

## Build locally

```powershell
python -m venv .venv
.\.venv\Scripts\activate
pip install -r requirements.txt
mkdocs serve
```

Run `mkdocs build --strict` to check links and anchors before pushing.