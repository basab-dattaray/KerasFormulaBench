from __future__ import print_function

from common.model.model_storage import *
from common.model.model_validation_mgr import *

# _fn_get_data = None  # IN: size; OUT: inputs, outputs
# _fn_generate_data_given_input_strings = None  # IN: input_string, input_string_size, output_string_size; OUT: input_string, label_string
#
# _fn_setup_model = None  # IN: input_string_size, output_string_size; SIDE_EFFECT: save model
# _fn_train_model = None  # IN: inputs, labels, num_of_iterations, num_of_epochs, num_of_batches  SIDE_EFFECT: save and load model
# _fn_stop_training = None  #
# _fn_predict = None  # IN: in_str; OUT: out_str

def validate_with_random_data():
    plugin_name, fn_get_data, fn_generate_data_given_input_strings, fn_setup_model, fn_compile_model, fn_predict = mediation_mgr()

    inputs, labels = fn_get_data(num_samples=20)

    fn_validate = create_model_validator(inputs, labels)
    model = load_compiled_model()

    fn_validate(model)


if __name__ == '__main__':
    validate_with_random_data()
