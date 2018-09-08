from __future__ import print_function
from keras.models import Sequential
from keras import layers
from six.moves import range


from common.model.training_callback_mgt import *
from common.model.model_storage import *

from common.generator.data_bender import *
from common.misc.fileops import *

def model(plugin_name):

    _model = None
    _stop_running = None
    # _x_train = None
    # _y_train = None
    # _x_val = None
    # _y_val = None

    _batch_size = None
    _num_of_epochs = None

    _abs_model_path = get_abs_path('plugins/' + plugin_name + '/model_data/model')

    def fn_setup_model(inputs, labels):

        # nonlocal _model
        # nonlocal _x_train, _y_train,  _x_val, _y_val
        # _x_train, _x_val, _y_train, _y_val = data_breaker(inputs, labels)
        model = None
        if is_model_usable(_abs_model_path):
            model = load_model(_abs_model_path)

            fn_compile_model(model)

        else:

            input_size = len(inputs[0])
            label_size = len(labels[0])

            HIDDEN_SIZE = 256
            # BATCH_SIZE = 128
            NUM_OF_HIDDEN_LAYERS = 1
            print('Build _model...')
            model = Sequential()
            # "Encode" the input sequence using an RNN, producing an output of HIDDEN_SIZE.
            # Note: In a situation where your input sequences have a variable length,
            # use input_shape=(None, num_feature).
            model.add(layers.LSTM(HIDDEN_SIZE, input_shape=(input_size, len(chars))))
            # As the decoder RNN's input, repeatedly provide with the last hidden state of
            # RNN for each time step. Repeat 'NUM_OF_DIGITS_IN_OPERAND + 1' times as that's the maximum
            # length of output, e.g., when NUM_OF_DIGITS_IN_OPERAND=3, max output is 999+999=1998.
            # _model.add(layers.RepeatVector(data_gen_dict['operand_size'] + 1))
            model.add(layers.RepeatVector(label_size))
            # The decoder RNN could be multiple layers stacked or a single layer.
            for _ in range(NUM_OF_HIDDEN_LAYERS):
                # By setting return_sequences to True, return not only the last output but
                # all the outputs so far in the form of (num_samples, timesteps,
                # output_dim). This is necessary as TimeDistributed in the below expects
                # the first dimension to be the timesteps.
                model.add(layers.LSTM(HIDDEN_SIZE, return_sequences=True))
            # Apply a dense layer to the every temporal slice of an input. For each of step
            # of the output sequence, decide which character should be chosen.
            model.add(layers.TimeDistributed(layers.Dense(len(chars))))
            model.add(layers.Activation('softmax'))
            fn_compile_model(model)
            model.summary()
        return model


    def fn_compile_model(model):
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

    def fn_predict(in_str):
        out_str = None
        return out_str

    return (fn_setup_model, fn_compile_model, fn_predict)