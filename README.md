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
uv run python balouf_github_io/fabmap.py
mv balouf_github_io/*.html docs/
uv run sphinx-build -a -E -b html docs build
```

Then open `build/index.html`.
