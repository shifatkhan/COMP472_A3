# -*- coding: utf-8 -*-
import csv

#Make output cleaner
#import warnings
#warnings.filterwarnings('ignore') 


#read files
train_filepath = './datasets/covid_training.tsv'
test_filepath = './datasets/covid_test_public'

#output path
output_dir = "./output"

"""
Utility method for reading tsv files.
Input is file path of the tsv file
Returns a 2d array representation of the tsv file
"""
def load_tsv(filepath):
    temp = [] #1d arr
    training_data = [] #2d array

    try:    
        with open(filepath, 'r', encoding="mbcs") as tsvfile:
            lines = csv.reader(tsvfile, delimiter='\t')
            
            #create 2d array
            for line in lines:
                temp = []
                
                for item in line:
                    temp.append(item)
                    
                training_data.append(temp)
            
            if filepath == train_filepath:
                training_data.pop(0)
                
            return training_data
        
    except FileNotFoundError:
        print(f"File not found: {filepath}")
    
