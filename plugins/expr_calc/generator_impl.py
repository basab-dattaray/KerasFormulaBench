from plugins.expr_calc.expr import *

def generate(plugin_name):


    fn_generate_data = None
    fn_generate_data_given_input_strings = None

    def init():
        nonlocal  fn_generate_data, fn_generate_data_given_input_strings
        fn_generate_data, fn_generate_data_given_input_strings = poly(plugin_name)

    def fn_get_data(num_samples):
        nonlocal fn_generate_data
        inputs, outputs = fn_generate_data(num_samples)
        return (inputs, outputs)

    def fn_generate_data_given_input_strings(string_of_inputs):
        nonlocal fn_generate_data_given_input_strings

        return fn_generate_data_given_input_strings(string_of_inputs)

    init()

    return (fn_get_data, fn_generate_data_given_input_strings)