from common.generator.data_bender import *
from common.misc.fileops import *

INPUT_WIDTH = 'INPUT_WIDTH'
LABEL_WIDTH = 'LABEL_WIDTH'

def normalize_sizes(inputs, input_width, label_width, outputs):
    inputs = normalize_list_of_strings(inputs, input_width)
    labels = normalize_list_of_strings(outputs, label_width)
    return inputs, labels


def save_char_widths(abs_path_to_json_scratch_file, input_width, label_width):
    size_dict = {}
    size_dict[INPUT_WIDTH] = input_width
    size_dict[LABEL_WIDTH] = label_width
    write_dict_to_file(abs_path_to_json_scratch_file, size_dict)

def load_char_widths(abs_path_to_json_scratch_file):
    size_dict = get_dict_from_json_file(abs_path_to_json_scratch_file)
    input_width = size_dict[INPUT_WIDTH]
    label_width = size_dict[LABEL_WIDTH]
    return input_width, label_width