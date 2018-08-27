from __future__ import print_function

from apps.mediation_mgt import *
from apps.RUN_CONSTANTS import *

import atexit

@atexit.register
def goodbye():
    print ("You are now leaving the Python sector.")




plugin_name, fn_get_data, fn_generate_data_given_input_strings,fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict = mediation_mgr()

inputs, labels = fn_get_data(num_samples=50000)

fn_setup_model(inputs, labels)

fn_train_model(plugin_name, BATCH_SIZE, NUM_OF_ITERATIONS, NUM_OF_EPOCHS)




