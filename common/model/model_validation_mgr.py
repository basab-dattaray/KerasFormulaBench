from common.generator.data_bender import *
from common.misc.character_mgt import ctable

class colors:
    ok = '\033[92m'
    fail = '\033[91m'
    close = '\033[0m'

DIGITS_ARE_REVERSE = False

def create_model_validator(questions, labels):

    def fn_validate(model):
        size = len(questions)
        for i in range(size):
            # ind = np.random.randint(0, len(x_val))
            rowx, rowy = x_val[np.array([i])], y_val[np.array([i])]
            preds = model.predict_classes(rowx, verbose=0)
            q = ctable.decode(rowx[0])
            correct = ctable.decode(rowy[0])
            guess = ctable.decode(preds[0], calc_argmax=False)
            # print('Q', q[::-1] if DIGITS_ARE_REVERSE else q, end=' ')
            # print('T', correct, end=' ')

            str = '{} {} predict {}'.format(questions[i], labels[i], guess)

            print(str, end = ' ')

            if correct.strip() == guess.strip():
                print(colors.ok + '☑' + colors.close, end=' ')
            else:
                print(colors.fail + '☒' + colors.close, end=' ')
            # print(guess)
            print()

    # questionss, labels, question_length = get_data(num_of_samples_to_generate)
    x_val, y_val = vectorize(questions, labels)

    return fn_validate

