def generator_mgr(plugin_module, plugin_name):

    fn_get_data = None # IN: size
    fn_generate_data_given_input_strings = None # IN: input_string, input_string_size; OUT: label_string

    def init():
        nonlocal fn_get_data, fn_generate_data_given_input_strings
        fn_get_data, fn_generate_data_given_input_strings = plugin_module.generate(plugin_name)


    init()
    return (fn_get_data, fn_generate_data_given_input_strings)

