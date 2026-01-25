#!/usr/bin/env python
# coding: utf-8

from gismap.lab import EgoMap as Map

from gismap.lab_examples.lip6 import Lip6Map


fabien = Map("Fabien Mathieu")
fabien.build(target=70)
fabien.save_html("fabmap")

npa = Lip6Map()
npa.update_authors()
npa.update_publis()
npa.expand()
npa.save_html("npa")
