
from common.misc.character_mgt import chars, ctable
import numpy as np

def get_maxlen_of_listitems(datalist):
    max_len = 0
    for data_item in datalist:
        if len(data_item) > max_len:
            max_len = len(data_item)
    return max_len

def normalize(datalist, maxsize):
    result = []
    for s in datalist:
        s_len = len(s)
        new_s = s
        if s_len < maxsize:
            new_s = s + ' ' * (maxsize - s_len)
        result.append(new_s)
    return result


def vectorize(questions, expected):
    print('Total addition questions:', len(questions))
    print('Vectorization...')

    question_length = None
    expected_length = None
    if (len(questions) > 0): # same len as labels
        question_length = len(questions[0])
        expected_length = len(expected[0])

    x = np.zeros((len(questions), question_length, len(chars)), dtype=np.bool)
    y = np.zeros((len(questions), expected_length, len(chars)), dtype=np.bool)
    for i, sentence in enumerate(questions):
        x[i] = ctable.encode(sentence, question_length)
    for i, sentence in enumerate(expected):
        y[i] = ctable.encode(sentence, expected_length)

    return x, y

def data_breaker(inputs, labels):

    x, y = vectorize(inputs, labels)
    # Shuffle (x, y) in unison as the later parts of x will almost all be larger
    # digits.
    indices = np.arange(len(y))
    np.random.shuffle(indices)
    x = x[indices]
    y = y[indices]
    # Explicitly set apart 10% for validation data that we never train over.
    split_at = len(x) - len(x) // 10
    (x_train, x_val) = x[:split_at], x[split_at:]
    (y_train, y_val) = y[:split_at], y[split_at:]
    print('Training Data:')
    print(x_train.shape)
    print(y_train.shape)
    print('Validation Data:')
    print(x_val.shape)
    print(y_val.shape)
    return (x_train, x_val, y_train, y_val)

