#!/usr/bin/env python
# coding: utf-8

from gismap.lab import EgoMap as Map

from bs4 import BeautifulSoup as Soup
from gismap.lab.lab import Lab
from gismap.lab.lab_author import AuthorMetadata, LabAuthor
from gismap.utils.requests import get


class Lip6Lab(Lab):
    """
    Class for handling a LIP6 team using `https://www.lip6.fr/recherche/team_membres.php?acronyme=*team_acronym*` as entry point.
    Default to `NPA` team.
    """

    name = "NPA"

    def _author_iterator(self):
        url = f"https://www.lip6.fr/recherche/team_membres.php?acronyme={self.name}"
        soup = Soup(get(url), "lxml")
        for a in soup.table("a"):
            name = a.text.replace("\xa0", " ").strip()
            if not name:
                continue
            metadata = AuthorMetadata(group=self.name)
            previous = a.find_previous_sibling()
            if previous is not None and "user" in previous.get("class", []):
                metadata.url = previous["href"].strip()
            fiche = "https://www.lip6.fr/" + a['href'].split('/', 1)[1]
            img = Soup(get(fiche), 'lxml').img
            if img and "reflet" in img['class'] and "noPhoto" not in img['src']:
                metadata.img = "https://www.lip6.fr/" + img['src'].split('/', 1)[1]
            yield LabAuthor(name=name, metadata=metadata)



fabien = Map("Fabien Mathieu")
fabien.build(target=70)
fabien.save_html("fabmap")

npa = Lip6Lab()
npa.update_authors()
npa.update_publis()
npa.expand()
npa.save_html("npa")
