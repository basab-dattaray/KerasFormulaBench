from framework.mediation_mgt import *
from plugins.expr_calc.config.RUN_CONSTANTS import *

plugin_name, fn_get_data, fn_generate_data_given_input_strings,fn_setup_model, fn_compile_model, fn_predict \
    = mediation_mgr()

inputs, labels = fn_get_data(num_samples=TRAINING_SIZE)
model = fn_setup_model(inputs, labels)