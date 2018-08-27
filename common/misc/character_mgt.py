import numpy as np

# All the numbers, plus sign and space for padding.
chars = '0123456789+-&| '

class CharacterTable(object):
    """Given a set of characters:
    + Encode them to a one hot integer representation
    + Decode the one hot integer representation to their character output
    + Decode a vector of probabilities to their character output
    """
    def __init__(self, chars):
        """Initialize character table.

        # Arguments
            chars: Characters that can appear in the input.
        """
        self.chars = sorted(set(chars))
        self.char_indices = dict((c, i) for i, c in enumerate(self.chars))
        self.indices_char = dict((i, c) for i, c in enumerate(self.chars))

    def encode(self, C, num_rows):
        """One hot encode given string C.

        # Arguments
            num_rows: Number of rows in the returned one hot encoding. This is
                used to keep the # of rows for each data the same.
        """
        x = np.zeros((num_rows, len(self.chars)))
        for i, c in enumerate(C):
            try:
                çind = self.char_indices[c]
                x[i, çind] = 1
            except Exception as e:
                print(e)

        return x

    def decode(self, x, calc_argmax=True):
        result = None
        try:
            if calc_argmax:
                x = x.argmax(axis=-1)
            result = ''.join(self.indices_char[x] for x in x)
            return result
        except Exception as e:
            print(e)

ctable = CharacterTable(chars)