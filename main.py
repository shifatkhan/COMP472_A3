# -*- coding: utf-8 -*-
import util
import vocabulary
from MNB import MNB

# INPUT
training_data = util.load_tsv(util.train_filepath)
test_data = util.load_tsv(util.test_filepath)

def run():
    # Setup Vocabulary
    OV = vocabulary.create_original_vocabulary(training_data)
    util.write_dictionary(OV, "OV")
    model_OV = MNB(OV, training_data)
    
    FV = vocabulary.create_filtered_vocabulary(training_data)
    util.write_dictionary(FV, "FV")
    model_FV = MNB(FV, training_data)
    
    # ========== Variables ========== #
    # Vars for the output
    trace_OV = []
    row_OV = []
    
    trace_FV = []
    row_FV = []
    
    # Vars for evaluation OV
    correct_answers_OV = 0
    correct_yes_OV = 0
    correct_no_OV = 0
    
    precision_yes_total_OV = 0
    precision_no_total_OV = 0
    recall_yes_total_OV = 0
    recall_no_total_OV = 0
    
    # Vars for evaluation FV
    correct_answers_FV = 0
    correct_yes_FV = 0
    correct_no_FV = 0
    
    precision_yes_total_FV = 0
    precision_no_total_FV = 0
    recall_yes_total_FV = 0
    recall_no_total_FV = 0
    
    # ========== Run for each tweet ========== #
    for tweet in test_data:
        row_OV = []
        row_FV = []
        
        # Get total frequency of yes/no from test_data
        if tweet[2] == "yes":
            recall_yes_total_OV += 1
            recall_yes_total_FV += 1
        else:
            recall_no_total_OV += 1
            recall_no_total_FV += 1
        
        # Add tweet ID
        row_OV.append(tweet[0])
        row_FV.append(tweet[1])
        
        yes_score_OV, no_score_OV = model_OV.get_scores(tweet)
        yes_score_FV, no_score_FV = model_FV.get_scores(tweet)
        
        # Add our model's result (yes or no)
        if yes_score_OV > no_score_OV:
            row_OV.append("yes")
            row_OV.append(yes_score_OV)
            
            # Total num of yes for precision (denominator)
            precision_yes_total_OV += 1
        else:
            row_OV.append("no")
            row_OV.append(no_score_OV)
            
            # Total num of no for precision (denominator)
            precision_no_total_OV += 1
        
        # Add our model's result (yes or no)
        if yes_score_FV > no_score_FV:
            row_FV.append("yes")
            row_FV.append(yes_score_FV)
            
            # Total num of yes for precision (denominator)
            precision_yes_total_FV += 1
        else:
            row_FV.append("no")
            row_FV.append(no_score_FV)
            
            # Total num of no for precision (denominator)
            precision_no_total_FV += 1
        
        # Add the correct class as indicated in the test file
        row_OV.append(tweet[2])
        row_FV.append(tweet[2])
        
        # Check if our model got the same result
        if row_OV[1] == tweet[2]:
            row_OV.append("correct")
            correct_answers_OV += 1
            
            # Get precision numerator
            if row_OV[1] == "yes":
                correct_yes_OV += 1
            else:
                correct_no_OV += 1
        else:
            row_OV.append("false")
            
        # Check if our model got the same result
        if row_FV[1] == tweet[2]:
            row_FV.append("correct")
            correct_answers_FV += 1
            
            # Get precision numerator
            if row_FV[1] == "yes":
                correct_yes_FV += 1
            else:
                correct_no_FV += 1
        else:
            row_FV.append("false")
        
        trace_OV.append(row_OV)
        trace_FV.append(row_FV)
    
    # ========== Output trace ========== #
    util.output(util.output_OV_filename, trace_OV)
    
    # ========== Calculate evaluations for OV ========== #
    eval_arr = []
    eval_arr.append([correct_answers_OV / len(trace_OV)])
    
    precision_yes = correct_yes_OV / precision_yes_total_OV
    precision_no = correct_no_OV / precision_no_total_OV
    
    recall_yes = correct_yes_OV / recall_yes_total_OV
    recall_no = correct_no_OV / recall_no_total_OV
    
    eval_arr.append([precision_yes, precision_no])
    eval_arr.append([recall_yes, recall_no])
    eval_arr.append([(2 * precision_yes * recall_yes) / (precision_yes + recall_yes), (2 * precision_no * recall_no) / (precision_no + recall_no)])
    
    util.output(util.eval_OV_filename, eval_arr)
    
    # ========== Calculate evaluations for FV ========== #
    eval_arr = []
    eval_arr.append([correct_answers_FV / len(trace_FV)])
    
    precision_yes = correct_yes_FV / precision_yes_total_FV
    precision_no = correct_no_FV / precision_no_total_FV
    
    recall_yes = correct_yes_FV / recall_yes_total_FV
    recall_no = correct_no_FV / recall_no_total_FV
    
    eval_arr.append([precision_yes, precision_no])
    eval_arr.append([recall_yes, recall_no])
    eval_arr.append([(2 * precision_yes * recall_yes) / (precision_yes + recall_yes), (2 * precision_no * recall_no) / (precision_no + recall_no)])
    
    util.output(util.eval_FV_filename, eval_arr)
#end run


run()
