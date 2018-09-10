import numpy as np

def chr_mgr():
    chars = '0123456789+-&| '
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))


    def fn_encode_chr(in_str, num_rows):

        one_hot_encoding = np.zeros((num_rows, len(chars)))

        # y = list(map) [zip(i, c) for i, c in enumerate(in_str)]

        for i, chr in enumerate(in_str):
            try:
                chr_index = char_indices[chr]
                one_hot_encoding[i, chr_index] = 1
            except Exception as e:
                raise Exception("char encoding error", e)

        return one_hot_encoding

    def fn_decode_chr( one_hot_vector, calc_argmax=True):
        result = None
        try:
            if calc_argmax:
                one_hot_vector = one_hot_vector.argmax(axis=-1)
            result = ''.join(indices_char[x] for x in one_hot_vector)
            return result
        except Exception as e:
            print(e)

# ctable = CharacterTable(chars)

    return fn_encode_chr, fn_decode_chr