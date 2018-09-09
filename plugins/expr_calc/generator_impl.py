from common.generator.formula_helper.poly_mgt import *

def generate(plugin_name):


    fn_generate_data = None
    fn_generate_data_given_input_strings = None
    expr = 'x: -300 - 15 * x + 12.5 * (x **+2)'
    fn_calc = eval("lambda " + expr)

    def init():
        nonlocal  fn_generate_data, fn_generate_data_given_input_strings
        nonlocal  fn_calc
        fn_generate_data, fn_generate_data_given_input_strings = poly(plugin_name, fn_calc)

    def fn_get_data(num_samples):
        nonlocal fn_generate_data
        inputs, outputs = fn_generate_data(num_samples)
        return (inputs, outputs)

    def fn_generate_data_given_input_strings(string_of_inputs):
        nonlocal fn_generate_data_given_input_strings

        return fn_generate_data_given_input_strings(string_of_inputs)

    init()

    return (fn_get_data, fn_generate_data_given_input_strings)