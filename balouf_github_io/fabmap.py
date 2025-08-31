#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from gismap.lab import EgoMap as Map
fabien = Map("Fabien Mathieu", dbs='hal')
fabien.build(target=30)
fabien.save_html("fabmap")

