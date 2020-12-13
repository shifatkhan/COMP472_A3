# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:59:02 2020

@author: NgoWi
"""

seen = set()

seen.add("a")
e = "e"
if e not in seen:
    seen.add("e")

print(seen)