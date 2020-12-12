# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:20:08 2020

@author: NgoWi
"""

import math

class MNB:
    
    
    def __init__(self, vocabulary, smoothing, log):
        self.vocab = vocabulary
        self.smoothing = smoothing
        self.log = log
        
        