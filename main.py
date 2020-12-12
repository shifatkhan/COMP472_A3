# -*- coding: utf-8 -*-
import util
import vocabulary

# TESTING INPUT
output = util.load_tsv(util.train_filepath)
# print(output)
util.output(util.output_OV_filename, output)

# TESTING DICT
OV = vocabulary.create_original_vocabulary(output)
FV = vocabulary.create_filtered_vocabulary(output)

util.write_dictionary(OV, "OV")
util.write_dictionary(FV, "FV")