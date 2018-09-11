from common.render.color_ref import *

def print_prediction(is_correct, input, label, prediction):
    str1 = 'input {}, label {}, '.format(input, label)
    str2 = 'predict {}.'.format(prediction)
    # print(str, end = ' ')
    print(colors.black + str1 + colors.close, end=' ')
    if is_correct.strip() == prediction.strip():
        print(colors.green + str2 + colors.close, end=' ')
    else:
        print(colors.red + str2 + colors.close, end=' ')
    print()