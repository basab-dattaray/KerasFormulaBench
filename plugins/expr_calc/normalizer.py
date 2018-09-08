from common.generator.data_bender import *
from common.misc.fileops import *

MAXLEN_INPUTS = 'maxlen_inputs'
MAXLEN_LABELS = 'maxlen_labels'

def normalize_sizes(inputs, maxlen_inputs, maxlen_labels, outputs):
    inputs = normalize_list_of_strings(inputs, maxlen_inputs)
    labels = normalize_list_of_strings(outputs, maxlen_labels)
    return inputs, labels


def save_sizes(abs_path_to_json_scratch_file, maxlen_inputs, maxlen_labels):
    size_dict = {}
    size_dict[MAXLEN_INPUTS] = maxlen_inputs
    size_dict[MAXLEN_LABELS] = maxlen_labels
    write_dict_to_file(abs_path_to_json_scratch_file, size_dict)

def get_sizes(abs_path_to_json_scratch_file):
    size_dict = get_dict_from_json_file(abs_path_to_json_scratch_file)
    maxlen_inputs = size_dict[MAXLEN_INPUTS]
    maxlen_labels = size_dict[MAXLEN_LABELS]
    return maxlen_inputs, maxlen_labels