from __future__ import print_function

from common.model.training_mgt import *

from apps.mediation_mgt import *
from apps.RUN_CONSTANTS import *
from common.generator.noise_mgt import *

import atexit

MAX_LOOP_COUNT = 5
@atexit.register
def goodbye():
    print ("You are now leaving KerasFormulaBench.")

plugin_name, fn_get_data, fn_generate_data_given_input_strings,fn_setup_model, fn_compile_model, fn_predict \
    = mediation_mgr()

fn_train_model = training_mgr(plugin_name, NUM_OF_ITERATIONS)


def create_noisy_data():
    inputs, labels = fn_get_data(num_samples=TRAINING_SIZE)
    fn_add_noise_to_array_of_char_strings = noise_mgr(NOISE_FACTOR)
    fn_add_noise_to_array_of_char_strings(labels)
    return inputs, labels

inputs, labels = create_noisy_data()

iteration_num = 1
loop_count = 1
while iteration_num  < NUM_OF_ITERATIONS and loop_count <= MAX_LOOP_COUNT:
    model = fn_setup_model(inputs, labels)
    iteration_num = fn_train_model(model, inputs, labels, NUM_OF_ITERATIONS, iteration_num, BATCH_SIZE,  NUM_OF_EPOCHS)
    print('Interations: {}/{} completed'.format(iteration_num, NUM_OF_ITERATIONS ))
    print('===============================================================================')
    print()
    inputs, labels = create_noisy_data()

x = 8


