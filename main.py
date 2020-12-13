# -*- coding: utf-8 -*-
import util
import vocabulary
from MNB import MNB

# INPUT
training_data = util.load_tsv(util.train_filepath)
test_data = util.load_tsv(util.test_filepath)

def createVocabulary():
    OV = vocabulary.create_original_vocabulary(training_data)
    FV = vocabulary.create_filtered_vocabulary(training_data)
    
    util.write_dictionary(OV, "OV")
    util.write_dictionary(FV, "FV")

def runOV():
    # Setup Vocabulary
    OV = vocabulary.create_original_vocabulary(training_data)
    util.write_dictionary(OV, "OV")
    
    model_OV = MNB(OV, training_data)
    
    trace = []
    row = []
    
    for tweet in test_data:
        row = []
        
        # Add tweet ID
        row.append(tweet[0])
        
        yes_score, no_score = model_OV.get_scores(tweet)
        
        # Add our model's result (yes or no)
        if yes_score > no_score:
            row.append("yes")
            row.append(yes_score)
        else:
            row.append("no")
            row.append(no_score)
        
        # Add the correct class as indicated in the test file
        row.append(tweet[2])
        
        # Check if our model got the same result
        if row[1] == tweet[2]:
            row.append("correct")
        else:
            row.append("false")
        
        trace.append(row)
    
    util.output(util.output_OV_filename, trace)
    
    return trace
#end runOV

def runFV():
    # Setup Vocabulary
    FV = vocabulary.create_filtered_vocabulary(training_data)
    util.write_dictionary(FV, "FV")
    
    model_FV = MNB(FV, training_data)
    
    trace = []
    row = []
    
    for tweet in test_data:
        row = []
        
        # Add tweet ID
        row.append(tweet[0])
        
        yes_score, no_score = model_FV.get_scores(tweet)
        
        # Add our model's result (yes or no)
        if yes_score > no_score:
            row.append("yes")
            row.append(yes_score)
        else:
            row.append("no")
            row.append(no_score)
        
        # Add the correct class as indicated in the test file
        row.append(tweet[2])
        
        # Check if our model got the same result
        if row[1] == tweet[2]:
            row.append("correct")
        else:
            row.append("false")
        
        trace.append(row)
    
    util.output(util.output_FV_filename, trace)
    
    return trace
#end runFV

runOV()
runFV()