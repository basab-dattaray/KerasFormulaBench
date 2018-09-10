from common.generator.data_bender import *
from common.misc.chr_mgt import *

from common.render.print_colors import *

DIGITS_ARE_REVERSE = False

def create_model_validator(questions, labels):

    def fn_validate(model):
        size = len(questions)
        for i in range(size):

            rowx, rowy = x_val[np.array([i])], y_val[np.array([i])]
            preds = model.predict_classes(rowx, verbose=0)

            correct = fn_decode_chr(rowy[0])
            guess = fn_decode_chr(preds[0], calc_argmax=False)

            str = '{} {} predict {}'.format(questions[i], labels[i], guess)

            print(str, end = ' ')

            if correct.strip() == guess.strip():
                print(colors.ok + '☑' + colors.close, end=' ')
            else:
                print(colors.fail + '☒' + colors.close, end=' ')
            # print(guess)
            print()

    fn_encode_chr, fn_decode_chr = chr_mgr()

    x_val, y_val = vectorize(questions, labels)

    return fn_validate

