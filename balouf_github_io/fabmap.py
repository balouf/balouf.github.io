#!/usr/bin/env python
# coding: utf-8

from gismap.lab import EgoMap as Map, Lip6Lab
fabien = Map("Fabien Mathieu")
fabien.build(target=70)
fabien.save_html("fabmap")

npa = Lip6Lab()
npa.update_authors()
npa.update_publis()
npa.expand()
npa.save_html("npa")
