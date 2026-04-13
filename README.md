# Source of Fabien Mathieu's Webpage

Live site: <https://balouf.github.io>

The site is built with [Sphinx](https://www.sphinx-doc.org/) from the Markdown
sources in [`docs/`](docs/), plus two interactive co-authorship maps generated
by [`balouf_github_io/fabmap.py`](balouf_github_io/fabmap.py) using
[`gismap`](https://github.com/balouf/gismap).

Pushes to `main` are auto-built and deployed to GitHub Pages by the
[`docs.yml`](.github/workflows/docs.yml) workflow (native Pages-from-Actions
flow — no `gh-pages` branch).

## Local build

```bash
uv sync --all-extras
uv run python build.py             # full build (regenerates the maps — slow)
uv run python build.py --no-maps   # skip map regeneration
```

Then open `build/index.html`.
