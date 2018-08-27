import numpy as np

# All the numbers, plus sign and space for padding.


def onehotchar_mgr():

    def init(chars):
        chars = '0123456789+-&| '

        # self.chars = sorted(set(chars))
        _char_index_dict = dict((c, i) for i, c in chars)
        _idex_char_dict = dict((i, c) for i, c in chars)

    def encode(data_str):
        onehotvetor = np.zeros((num_rows, chars))
        for i, c in C:
            try:
                x[i, self.char_indices[c]] = 1
            except Exception as e:
                print(e)

        return x

    def decode(self, x, calc_argmax=True):
        try:
            if calc_argmax:
                x = x.argmax(axis=-1)
            return ''.join(self.indices_char[x] for x in x)
        except Exception as e:
            print(e)

ctable = CharacterTable(chars)