"""Local + CI build: regenerate the gismap maps, then build the Sphinx site.

The maps (fabmap.html, npa.html) are written *directly into docs/*, which is
the single canonical location Sphinx reads them from (see the :file:
directives in docs/about_me.md and docs/research.md). Kept on disk between
runs so `--no-maps` can skip the slow DBLP/HAL scraping when iterating on
prose only.

Usage:
    uv run python build.py            # full build (maps + sphinx)
    uv run python build.py --no-maps  # skip the slow map regeneration
"""
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PKG = ROOT / "balouf_github_io"
DOCS = ROOT / "docs"
OUT = ROOT / "build"


def run(*args, cwd=None):
    print("$", *args)
    subprocess.run(args, check=True, cwd=cwd)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-maps",
        action="store_true",
        help="skip running fabmap.py (use the maps already in docs/)",
    )
    args = parser.parse_args()

    if not args.no_maps:
        # Run fabmap.py with cwd=docs/ so save_html() writes the maps
        # straight into docs/ — no move step, no double location.
        run(sys.executable, str(PKG / "fabmap.py"), cwd=str(DOCS))

    run("sphinx-build", "-a", "-E", "-b", "html", str(DOCS), str(OUT))
    print(f"\nBuilt site at: {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
