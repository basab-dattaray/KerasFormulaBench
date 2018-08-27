from common.misc.data_bender import *

def generator_mgr(plugin_module, plugin_name):

    _fn_get_data = None # IN: size
    _fn_generate_data_given_input = None # IN: input_string, input_string_size; OUT: label_string

    def init():
        nonlocal _fn_get_data, _fn_generate_data_given_input
        _fn_get_data, _fn_generate_data_given_input = plugin_module.generate(plugin_name)


    init()
    return (_fn_get_data, _fn_generate_data_given_input)

