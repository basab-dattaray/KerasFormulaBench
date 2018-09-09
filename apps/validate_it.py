from __future__ import print_function

from common.model.model_storage import *
from common.model.model_validation_mgr import *

def validate_with_random_data():
    plugin_name, fn_get_data, fn_generate_data_given_input_strings, fn_setup_model, fn_compile_model, fn_predict = mediation_mgr()

    inputs, labels = fn_get_data(num_samples=20)

    fn_validate = create_model_validator(inputs, labels)
    model = load_compiled_model()

    fn_validate(model)

if __name__ == '__main__':
    validate_with_random_data()
