
from keras.models import Sequential
from keras import layers

from common.misc.chr_mgt import *

def model(plugin_name):

    _model = None
    _stop_running = None

    _batch_size = None
    _num_of_epochs = None

    _ , _, char_array = chr_mgr()

    rnn = layers.LSTM

    def fn_setup_model(inputs, labels):
        input_size = len(inputs[0])
        label_size = len(labels[0])

        HIDDEN_SIZE = 128
        # BATCH_SIZE = 128
        NUM_OF_HIDDEN_LAYERS = 1

        model = Sequential()

        model.add(rnn(HIDDEN_SIZE, input_shape=(input_size, len(char_array))))

        model.add(layers.RepeatVector(label_size))

        model.add(rnn(HIDDEN_SIZE, return_sequences=True))

        model.add(rnn(HIDDEN_SIZE, return_sequences=True))

        model.add(layers.TimeDistributed(layers.Dense(len(char_array))))

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