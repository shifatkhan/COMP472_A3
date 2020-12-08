# -*- coding: utf-8 -*-
import util
import vocabulary

# TESTING INPUT
output = util.load_tsv(util.train_filepath)
print(output)
util.output(util.output_OV_filename, output)

# TESTING DICT
my_dict = vocabulary.create_dictionary(output)
