from common.generator.formula_helper.poly_mgt import *
from plugins.expr_calc.CONFIG import *
def generate(plugin_name):


    fn_generate_data = None
    fn_generate_data_given_input_strings = None

    abs_expr_file_path = get_abs_path('plugins/' + plugin_name + '/FORMULA.TXT')
    formulas = get_lines_from_file(abs_expr_file_path)
    expr = None
    if len(formulas) > 0:
        expr = formulas[0]
    else:
        raise Exception("FORMULA.TXT does not have expressions in it")

    fn_calc = eval('lambda ' + expr)

    def init():
        nonlocal  fn_generate_data, fn_generate_data_given_input_strings
        nonlocal  fn_calc
        fn_generate_data, fn_generate_data_given_input_strings = poly(plugin_name, fn_calc, INPUT_WIDTH, LABEL_WIDTH)

    def fn_get_data(num_samples):
        nonlocal fn_generate_data
        inputs, outputs = fn_generate_data(num_samples)
        return (inputs, outputs)

    def fn_generate_data_given_input_strings(string_of_inputs):
        nonlocal fn_generate_data_given_input_strings

        return fn_generate_data_given_input_strings(string_of_inputs)

    init()

    return (fn_get_data, fn_generate_data_given_input_strings)