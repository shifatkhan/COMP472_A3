# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:55:08 2020

@author: NgoWi
"""

import util

def create_dictionary(dataset_list):
    tweet_dict = {}
    for row in dataset_list:
        text = row[1]
        tokens = text.split()
        
        for word in tokens:
            lower_word = word.lower()
            if lower_word not in tweet_dict:
                tweet_dict[lower_word] = 1
            else:
                tweet_dict[lower_word] += 1
    
    return tweet_dict