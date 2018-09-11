from common.generator.data_bender import *
from common.misc.chr_mgt import *

from common.render.print_prediction import *

DIGITS_ARE_REVERSE = False

def create_model_validator(inputs, labels):

    def fn_validate(model):
        size = len(inputs)
        for i in range(size):

            rowx, rowy = x_val[np.array([i])], y_val[np.array([i])]
            preds = model.predict_classes(rowx, verbose=0)

            correct = fn_decode_chr(rowy[0])
            prediction = fn_decode_chr(preds[0], calc_argmax=False)

            print_prediction(correct, inputs[i], labels[i], prediction)



    _, fn_decode_chr, _ = chr_mgr()

    x_val, y_val = vectorize(inputs, labels)

    return fn_validate

