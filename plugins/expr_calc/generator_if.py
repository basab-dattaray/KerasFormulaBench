# from common.misc.fileops import get_dict_from_json_file

from plugins.expr_calc.expr import *


# fn_get_data = None  # IN: num_samples: in_str_array, out_str_array
# fn_generate_data_given_input = None  # IN: input_string, input_string_size; OUT: label_string

def generate(plugin_name):


    fn_generate_data = None
    fn_generate_data_given_input = None

    def init():
        nonlocal  fn_generate_data, fn_generate_data_given_input
        fn_generate_data, fn_generate_data_given_input = poly(plugin_name, [6, -.5, .25])

    def fn_get_data(num_samples):
        nonlocal fn_generate_data
        inputs, outputs = fn_generate_data(num_samples)
        return (inputs, outputs)

    def fn_generate_data_given_input(input_string):
        nonlocal fn_generate_data_given_input

        return fn_generate_data_given_input(input_string)

    init()

    return (fn_get_data, fn_generate_data_given_input)