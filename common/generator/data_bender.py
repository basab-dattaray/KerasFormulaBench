
# from common.misc.character_mgt import chars, ctable

from common.misc.chr_mgt import *


import numpy as np

def get_maxlen_of_listitems(datalist):
    max_len = 0
    for data_item in datalist:
        if len(data_item) > max_len:
            max_len = len(data_item)
    return max_len

def normalize_list_of_strings(datalist, maxsize):
    result = []
    for s in datalist:
        new_s = normalize_string( s, maxsize)
        result.append(new_s)
    return result


def normalize_string(s, maxsize):
    s_len = len(s)
    new_s = s
    if s_len < maxsize:
        new_s = s + ' ' * (maxsize - s_len)
    return new_s


def vectorize(input_strings, label_strings):
    
    fn_encode_chr, _, character_array = chr_mgr()

    input_width = None
    label_width = None
    if (len(input_strings) > 0): # same len as labels
        input_width = len(input_strings[0])
        label_width = len(label_strings[0])

    one_hot_inp_strings = np.zeros((len(input_strings), input_width, len(character_array)), dtype=np.bool)
    one_hot_labels = np.zeros((len(input_strings), label_width, len(character_array)), dtype=np.bool)
    for i, str in enumerate(input_strings):
        one_hot_inp_strings[i] = fn_encode_chr(str, input_width)
    for i, str in enumerate(label_strings):
        one_hot_labels[i] = fn_encode_chr(str, label_width)

    return one_hot_inp_strings, one_hot_labels

def data_breaker(inputs, labels):

    one_hot_inputs, one_hot_labels = vectorize(inputs, labels)

    indices = np.arange(len(one_hot_labels))
    np.random.shuffle(indices)
    one_hot_inputs = one_hot_inputs[indices]
    one_hot_labels = one_hot_labels[indices]

    split_at = len(one_hot_inputs) - len(one_hot_inputs) // 10
    (inputs_train, inputs_val) = one_hot_inputs[:split_at], one_hot_inputs[split_at:]
    (labels_train, labels_val) = one_hot_labels[:split_at], one_hot_labels[split_at:]
    print('Training Data:')
    print(inputs_train.shape)
    print(labels_train.shape)
    print('Validation Data:')
    print(inputs_val.shape)
    print(labels_val.shape)
    return (inputs_train, inputs_val, labels_train, labels_val)

