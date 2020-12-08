# -*- coding: utf-8 -*-
import util
import vocabulary

# TESTING INPUT
output = util.load_tsv(util.train_filepath)
my_dict = vocabulary.create_dictionary(output)