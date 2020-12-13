# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 13:20:08 2020

@author: NgoWi
"""

import math
import util

class MNB:
    
    """
    Function to set up the classifier using a given dataset
    """
    def __setup(self, training_set):
        # num used for calculating p(yes) and p(no)
        num_tweets_yes = 0
        num_tweets_no = 0
        
        total_tweets = len(training_set)
        
        for tweet in training_set:
            tweet_id = tweet[0]
            tweet_text = tweet[1]
            tokenized_text = tweet_text.lower().split()
            label = tweet[2]
            
            if label == 'yes':
                # add tokens to the vocabulary of the yes class
                for token in tokenized_text:
                    if token not in self.yes_vocab:
                        self.yes_vocab[token] = 1
                    else:
                        self.yes_vocab[token] += 1
                        
                    # total number of words that are in tweets labelled yes
                    self.total_w_yes += 1 
                    
                num_tweets_yes += 1
            else: # if tweet is labelled no
            
                # add tokens to vocabulary in no class
                for token in tokenized_text:
                    if token not in self.no_vocab:
                        self.no_vocab[token] = 1
                    else:
                        self.no_vocab[token] += 1
                        
                    # total number of words that are in tweets labelled no
                    self.total_w_no += 1 
                    
                num_tweets_no += 1
        
        # calculate p(yes) p(no)
        self.p_yes = num_tweets_yes/total_tweets
        self.p_no = num_tweets_no/total_tweets
        
        
    def __init__(self, vocabulary, training_set, smoothing = 0.01):
        # vocabulary from trainin set
        self.vocab = vocabulary
        self.smoothing = smoothing
        
        # probability of a tweet being yes or no
        self.p_yes = 0
        self.p_no = 0
        
        # total number of words that are in class yes / no
        # used in the calculation of p(w|c) = (freq of w in c / total_w_c)
        self.total_w_yes = 0
        self.total_w_no = 0
        
        # all words that appear in yes / no class {word : frequency}
        self.yes_vocab = {}
        self.no_vocab = {}
        
        self.__setup(training_set)
    
    """
    Calculates P(w | c) for w = given token and c = class 'no'
    """
    def __find_p_token_no(self, token):
        fw = 0 + self.smoothing
        total_w = self.total_w_no + (len(self.vocab) * self.smoothing)
        
        if token in self.no_vocab:
            # p(w|c) = frequency of w in c / total num of words in c
            fw += self.no_vocab[token]
            
        return fw / total_w
    
    """
    Calculates P(w | c) for w = given token and c = class 'yes'
    """
    def __find_p_token_yes(self, token):
        fw = 0 + self.smoothing
        total_w = self.total_w_yes + (len(self.vocab) * self.smoothing)

        if token in self.yes_vocab:
            # p(w|c) = frequency of w in c / total num of words in c
            fw += self.yes_vocab[token]
            
        return fw / total_w
    
    """
    Calculates the score for a given tweet.
    """
    def get_scores(self, tweet):
        tweet_id = tweet[0]
        tweet_text = tweet[1]
        tokenized_text = tweet_text.lower().split()
        
        score_yes = math.log(self.p_yes, 10)
        score_no = math.log(self.p_no, 10)
        
        for token in tokenized_text:
            # only work with words that appear in our training vocab
            if token in self.vocab:
                p_yes_token = self.__find_p_token_yes(token)
                p_no_token = self.__find_p_token_no(token)
                
                # score = p(yes)
                score_yes += math.log(p_yes_token, 10)
                score_no += math.log(p_no_token, 10)
        
        return score_yes, score_no
                
                
            
        
        
        
        
        
        
        
        
        
        
        