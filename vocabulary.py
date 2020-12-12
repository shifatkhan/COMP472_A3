# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 13:55:08 2020

@author: NgoWi
"""

import util

"""
Creates a dictionary where the keys are the tokens and the values are the term frequency
dataset list is a 2d array that contains the information of the dataset tsv
"""
def create_original_vocabulary(dataset_list):
    tweet_dict = {}
    for row in dataset_list:
        
        text = row[1]
        tokens = text.split()
        
        for word in tokens:
            lower_word = word.lower()
            
            # Add to dictionary if doesn't exist yet
            if lower_word not in tweet_dict:
                tweet_dict[lower_word] = 1
            else:
                # else increment frequency
                tweet_dict[lower_word] += 1
    
    return tweet_dict

def create_filtered_vocabulary(dataset_list):
    tweet_dict = {}
    for row in dataset_list:
        
        text = row[1]
        tokens = text.split()
        
        # seen is a set that will 
        seen = set()
        for word in tokens:
            
            # if the word appears once, put it in set
            if word not in seen:
                seen.add(word)
            # else if the word appears more than once, add it to dictionary
            else:
                lower_word = word.lower()
                
                # Add to dictionary if doesn't exist yet
                if lower_word not in tweet_dict:
                    tweet_dict[lower_word] = 2
                else:
                    # else increment frequency
                    tweet_dict[lower_word] += 1
    
    return tweet_dict


