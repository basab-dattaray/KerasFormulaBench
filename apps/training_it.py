from __future__ import print_function

from common.model.training_mgt import *

from apps.mediation_mgt import *
from apps.RUN_CONSTANTS import *

import atexit

@atexit.register
def goodbye():
    print ("You are now leaving the Python sector.")

plugin_name, fn_get_data, fn_generate_data_given_input_strings,fn_setup_model, fn_train_model, fn_stop_training, fn_compile_model, fn_predict \
    = mediation_mgr()

fn_train_model = training_mgr(plugin_name, NUM_OF_ITERATIONS)

inputs, labels = fn_get_data(num_samples=TRAINING_SIZE)

iteration_num = 1
while iteration_num  < NUM_OF_ITERATIONS:
    model = fn_setup_model(inputs, labels)
    # iteration_num = fn_train_model(model, inputs, labels, NUM_OF_ITERATIONS, iteration_num, BATCH_SIZE,  NUM_OF_EPOCHS)

    # def fn_train_model(model, inputs, labels, total_num_of_iterations, current_iteration, batch_size, num_of_epochs):

    iteration_num = fn_train_model(model, inputs, labels, NUM_OF_ITERATIONS, iteration_num, BATCH_SIZE,  NUM_OF_EPOCHS)
    print('Interations: {}/{} completed'.format(iteration_num, NUM_OF_ITERATIONS ))
    print('===============================================================================')
    print()

x = 8


