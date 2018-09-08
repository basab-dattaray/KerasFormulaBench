from __future__ import print_function

from common.model.training_mgt import *

from apps.mediation_mgt import *
from apps.RUN_CONSTANTS import *
from common.generator.noise_mgt import *

import atexit

MAX_ITERATIONS = 1
@atexit.register
def goodbye():
    print ("You are now leaving the Python sector.")

plugin_name, fn_get_data, fn_generate_data_given_input_strings,fn_setup_model, fn_train_model, fn_stop_training, fn_compile_model, fn_predict \
    = mediation_mgr()

fn_train_model = training_mgr(plugin_name, NUM_OF_ITERATIONS)

inputs, labels = fn_get_data(num_samples=TRAINING_SIZE)

fn_add_noise_to_array_of_char_strings = noise_mgr(.1)

fn_add_noise_to_array_of_char_strings(labels)
iteration_num = 1
# while iteration_num  < NUM_OF_ITERATIONS and iteration_num <= MAX_ITERATIONS:
model = fn_setup_model(inputs, labels)
iteration_num = fn_train_model(model, inputs, labels, NUM_OF_ITERATIONS, iteration_num, BATCH_SIZE,  NUM_OF_EPOCHS)
print('Interations: {}/{} completed'.format(iteration_num, NUM_OF_ITERATIONS ))
print('===============================================================================')
print()

x = 8


