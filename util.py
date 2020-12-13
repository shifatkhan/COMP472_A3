# -*- coding: utf-8 -*-
import csv
from pathlib import Path

#Make output cleaner
#import warnings
#warnings.filterwarnings('ignore') 


#read files
train_filepath = './datasets/covid_training.tsv'
test_filepath = './datasets/covid_test_public.tsv'

#output path
output_dir = "./output"
output_OV_filename = output_dir + "/trace_NB-BOW-OV.txt"
output_FV_filename = output_dir + "/trace_NB-BOW-FV.txt"

eval_OV_filename = output_dir + "/eval_NB-BOW-OV.txt"
eval_FV_filename = output_dir + "/eval_NB-BOW-FV.txt"

"""
Utility method for reading tsv files.
Input is file path of the tsv file
Returns a 2d array representation of the tsv file
"""
def load_tsv(filepath):
    temp = [] #1d arr
    training_data = [] #2d array

    try:    
        with open(filepath, 'r', encoding="utf-8") as tsvfile:
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
    
"""
Utility method for the output
Input is file path of output file
"""
def output(filepath, output_data):
    try:
        # Create output dir if it doesn't exist.
        Path(output_dir).mkdir(parents=True, exist_ok=True)
        
        # newline="" because there are empty lines between rows.
        with open(filepath, mode='w', encoding="utf-8") as file:
            
            # Loop through 2d array
            for row in output_data:
                for col in row:
                    file.write(str(col))
                    file.write("  ")
                file.write("\n")
                
    except FileNotFoundError:
            print(f"File not found: {filepath}")


"""
Function to output dictionary to file
"""    
def write_dictionary(dictionary, filename):
    path = f"output/{filename}.txt"
    with open(path, 'w', encoding="utf-8") as index_out:
        output = "{\n"
        for item in dictionary:
            output += "\t\'" + item + "\' : " + str(dictionary[item]) + "\n"
        output += "}"
        
        index_out.write(output)