"""Local + CI build: regenerate the gismap maps, then build the Sphinx site.

Usage:
    uv run python build.py            # full build (maps + sphinx)
    uv run python build.py --no-maps  # skip the slow map regeneration
"""
import argparse
import shutil
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).parent
PKG = ROOT / "balouf_github_io"
DOCS = ROOT / "docs"
OUT = ROOT / "build"


def run(*args):
    print("$", *args)
    subprocess.run(args, check=True)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--no-maps",
        action="store_true",
        help="skip running fabmap.py (use the maps already in docs/)",
    )
    args = parser.parse_args()

    if not args.no_maps:
        run(sys.executable, str(PKG / "fabmap.py"))
        for html in PKG.glob("*.html"):
            shutil.move(str(html), DOCS / html.name)

    run("sphinx-build", "-a", "-E", "-b", "html", str(DOCS), str(OUT))
    print(f"\nBuilt site at: {OUT / 'index.html'}")


if __name__ == "__main__":
    main()
