from common.misc.plugin_mgt import *
from common.generator.generator_mgt_if import *
from common.model.model_mgt_if import *


def mediation_mgr():

    _plugin_module_GENERATOR_MGT = None
    _plugin_module_MODEL_MGT = None
    _plugin_name = None

    fn_get_data = None # IN: size; OUT: inputs, outputs
    fn_generate_data_given_input = None # IN: input_string, input_string_size, output_string_size; OUT: input_string, label_string

    fn_setup_model = None # IN: inputs, labels
    fn_train_model = None # IN:  num_of_iterations, num_of_epochs, num_of_batches  SIDE_EFFECT: save  model
    fn_train_on = None # IN: inputs, labels, num_of_iterations; SIDE_EFFECT: save and load model
    fn_stop_training = None #
    fn_compile_model = None #
    fn_predict = None # IN: in_str; OUT: out_str

    def init():
        nonlocal _plugin_module_GENERATOR_MGT, _plugin_module_MODEL_MGT, _plugin_name
        get_plugin_info = plugin_mgr()
        _plugin_name, _plugin_module_GENERATOR_MGT, _plugin_module_MODEL_MGT = get_plugin_info()

    def setup_for_training():
        nonlocal fn_get_data, fn_generate_data_given_input
        nonlocal fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict

        fn_get_data, fn_generate_data_given_input = generator_mgr(_plugin_module_GENERATOR_MGT, _plugin_name)
        fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict = model_mgr(_plugin_module_MODEL_MGT)

    init()
    setup_for_training()

    return (
        _plugin_name,
        fn_get_data,
        fn_generate_data_given_input,
        fn_setup_model,
        fn_train_model,
        fn_train_on,
        fn_stop_training,
        fn_compile_model,
        fn_predict
    )




