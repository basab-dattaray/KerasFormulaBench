from __future__ import print_function
from keras.models import Sequential
from keras import layers
from six.moves import range


from common.model.training_effort_management import *
from common.model.model_storage import *

from common.generator.data_bender import *
from common.misc.fileops import *

def model(plugin_name, save_after_n_iterations, num_of_iteration_degradations_for_overfitting):

    _model = None
    _stop_running = None
    _x_train = None
    _y_train = None
    _x_val = None
    _y_val = None

    _batch_size = None
    _num_of_epochs = None

    _abs_model_path = get_abs_path('plugins/' + plugin_name + '/model_data/model')

    def fn_setup_model(inputs, labels):

        nonlocal _model
        nonlocal _x_train, _y_train,  _x_val, _y_val
        _x_train, _x_val, _y_train, _y_val = data_breaker(inputs, labels)

        if is_model_usable(_abs_model_path):
            _model = load_model(_abs_model_path)

            fn_compile_model(_model)

        else:

            input_size = len(inputs[0])
            label_size = len(labels[0])

            HIDDEN_SIZE = 128
            # BATCH_SIZE = 128
            NUM_OF_HIDDEN_LAYERS = 1
            print('Build _model...')
            _model = Sequential()
            # "Encode" the input sequence using an RNN, producing an output of HIDDEN_SIZE.
            # Note: In a situation where your input sequences have a variable length,
            # use input_shape=(None, num_feature).
            _model.add(layers.LSTM(HIDDEN_SIZE, input_shape=(input_size, len(chars))))
            # As the decoder RNN's input, repeatedly provide with the last hidden state of
            # RNN for each time step. Repeat 'NUM_OF_DIGITS_IN_OPERAND + 1' times as that's the maximum
            # length of output, e.g., when NUM_OF_DIGITS_IN_OPERAND=3, max output is 999+999=1998.
            # _model.add(layers.RepeatVector(data_gen_dict['operand_size'] + 1))
            _model.add(layers.RepeatVector(label_size))
            # The decoder RNN could be multiple layers stacked or a single layer.
            for _ in range(NUM_OF_HIDDEN_LAYERS):
                # By setting return_sequences to True, return not only the last output but
                # all the outputs so far in the form of (num_samples, timesteps,
                # output_dim). This is necessary as TimeDistributed in the below expects
                # the first dimension to be the timesteps.
                _model.add(layers.LSTM(HIDDEN_SIZE, return_sequences=True))
            # Apply a dense layer to the every temporal slice of an input. For each of step
            # of the output sequence, decide which character should be chosen.
            _model.add(layers.TimeDistributed(layers.Dense(len(chars))))
            _model.add(layers.Activation('softmax'))
            fn_compile_model(_model)
            _model.summary()


    def fn_train_model(num_of_iterations, batch_size, num_of_epochs):
        nonlocal _batch_size, _num_of_epochs
        nonlocal _model, _abs_model_path
        nonlocal _stop_running
        nonlocal  _x_train, _y_train,  _x_val, _y_val

        _batch_size = batch_size
        _num_of_epochs = num_of_epochs

        early_stopping_call_back = TrainingContinuationCallback(fn_stop_training, _model, plugin_name)

        for iteration in range(0, num_of_iterations - 1):

            if (_stop_running):
                _stop_running = False
                break
                # pass
            print()
            print('-' * 50)
            print('Iteration', iteration)
            _model.fit(_x_train, _y_train,
                       batch_size=batch_size,
                       epochs=num_of_epochs,
                       validation_data=( _x_val, _y_val),
                       callbacks=[early_stopping_call_back],
                       verbose=2)
            if iteration > 0 and iteration % save_after_n_iterations == 0:
                save_model(_abs_model_path, _model)
                print ('saved model after {} iterations'.format(iteration))

        if not _stop_running:
            save_model(_abs_model_path, _model)
            print('saved model on forced stop')

        return num_of_iterations - iteration

    def fn_train_on():
        nonlocal _batch_size, _num_of_epochs
        pass

    def fn_stop_training():
        nonlocal _stop_running
        _stop_running = True

    def fn_compile_model(model):
        model.compile(loss='categorical_crossentropy',
                      optimizer='adam',
                      metrics=['accuracy'])

    def fn_predict(in_str):
        out_str = None
        return out_str

    return (fn_setup_model, fn_train_model, fn_train_on, fn_stop_training, fn_compile_model, fn_predict)