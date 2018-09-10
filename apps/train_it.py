from __future__ import print_function

from common.model.training_mgt import *

from framework.mediation_mgt import *
from apps.RUN_CONSTANTS import *
from common.generator.noise_mgt import *

import atexit


@atexit.register
def goodbye():
    print ("You are now leaving KerasFormulaBench.")

plugin_name, fn_get_data, fn_generate_data_given_input_strings,fn_setup_model, fn_compile_model, fn_predict \
    = mediation_mgr()

fn_train_model = training_mgr(plugin_name, NUM_ITERATIONS_FOR_SAVING_MODEL)


def create_noisy_data():
    inputs, labels = fn_get_data(num_samples=TRAINING_SIZE)
    fn_add_noise_to_array_of_char_strings = noise_mgr(NOISE_FACTOR)
    fn_add_noise_to_array_of_char_strings(labels)
    return inputs, labels

inputs, labels = create_noisy_data()
abs_model_path = get_abs_path('plugins/' + plugin_name + '/model_data/model')
iteration_num = 1
loop_count = 1
while iteration_num  < NUM_OF_ITERATIONS and loop_count <= MAX_LOOP_COUNT:
    loop_count += 1
    model = None

    if is_model_usable(abs_model_path) and USE_EXISTING_MODEL:
        model = load_model(abs_model_path)
        fn_compile_model(model)
    else:
        model = fn_setup_model(inputs, labels)

    iteration_num = fn_train_model(model, inputs, labels, NUM_OF_ITERATIONS, iteration_num, BATCH_SIZE,  NUM_OF_EPOCHS)
    print('Interations: {}/{} completed'.format(iteration_num, NUM_OF_ITERATIONS ))
    print('===============================================================================')
    print()
    inputs, labels = create_noisy_data()




