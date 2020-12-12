# -*- coding: utf-8 -*-
import util
import vocabulary
from MNB import MNB

# TESTING INPUT
training_data = util.load_tsv(util.train_filepath)
test_data = util.load_tsv(util.test_filepath)

# print(training_data)
util.output(util.output_OV_filename, training_data)

# TESTING DICT
OV = vocabulary.create_original_vocabulary(training_data)
FV = vocabulary.create_filtered_vocabulary(training_data)

util.write_dictionary(OV, "OV")
util.write_dictionary(FV, "FV")

classifier = MNB(OV, training_data)