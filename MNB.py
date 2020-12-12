# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:20:08 2020

@author: NgoWi
"""

import math
import util

class MNB:
    
    def __setup(self):
        num_yes = 0
        num_no = 0
        total_tweets = len(self.training_dataset)
        
        for tweet in self.training_dataset:
            tweet_id = tweet[0]
            tweet_text = tweet[1]
            tokenized_text = tweet_text.lower().split()
            label = tweet[2]
            
            if label == 'yes':
                # add tokens to vocabulary in yes class
                for token in tokenized_text:
                    if token not in self.yes_vocab:
                        self.yes_vocab[token] = 1
                    else:
                        self.yes_vocab[token] += 1
                
                # add tweet text to dictionary of tweets labeled yes
                self.yes_tweets[tweet_id] = tweet_text
                num_yes += 1
            else:
                # add tokens to vocabulary in no class
                for token in tokenized_text:
                    if token not in self.no_vocab:
                        self.no_vocab[token] = 1
                    else:
                        self.no_vocab[token] += 1
                
                self.no_tweets[tweet_id] = tweet_text
                num_no += 1
        
        self.p_yes = num_yes/total_tweets
        self.p_no = num_no/total_tweets
        
        
    def __init__(self, vocabulary, training_set, smoothing = 0.01):
        self.vocab = vocabulary
        self.smoothing = smoothing
        self.p_yes = 0
        self.p_no = 0
        self.training_dataset = training_set
        self.yes_tweets = {}
        self.no_tweets = {}
        self.yes_vocab = {}
        self.no_vocab = {}
        self.__setup()
    
    # def __find_p_token_no(token):
    #     return self.no_vocab[token]
    # def __find_p_token_yes(token):
        
        
    def train(test_dataset):
        for tweet in test_dataset:
            tweet_id = tweet[0]
            tweet_text = tweet[0]
            tokenized_text = tweet_text.lower().split()
            
            score_yes = 0
            score_no = 0
            
            # for tokens in tokenized_text:
                
            
        
        
        
        
        
        
        
        
        
        
        