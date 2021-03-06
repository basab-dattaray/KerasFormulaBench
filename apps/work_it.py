from __future__ import print_function

from common.model.model_storage import *
from common.model.model_validation_mgr import *


def validate():
    plugin_name, fn_get_data, fn_generate_data_given_input_strings, fn_stop_training, fn_compile_model, fn_predict = mediation_mgr()

    model = load_compiled_model()

    abs_input_file_path = get_abs_path('plugins/' + plugin_name + '/config' + '/WORK_IT.TXT')
    string_of_inputs = get_lines_from_file(abs_input_file_path)

    inp_str_arr, out_str_arr = fn_generate_data_given_input_strings(string_of_inputs)

    fn_validate = create_model_validator(inp_str_arr, out_str_arr)
    fn_validate(model)


if __name__ == '__main__':

    validate()
