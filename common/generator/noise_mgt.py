import numpy as np

from common.generator.data_bender import *

def noise_mgr(noise_factor = .01):
    def fn_add_noise_to_array_of_char_strings(char_str_array):
        len_of_array = len(char_str_array)
        string_size = len(char_str_array[0])

        num_steps = round(len_of_array * noise_factor)
        index_increment = round(len_of_array / num_steps)
        for i in range(0, len_of_array, index_increment):
            random_str = get_random_number_as_string(string_size)
            char_str_array[i] = random_str

    return fn_add_noise_to_array_of_char_strings


def get_random_number_as_string(string_size):
    max_number = 10 ** (string_size - 1) - 1

    rnd_number = np.random.randint(max_number)

    random_str = str(rnd_number).strip(' ')

    random_bool = np.random.randint(2)
    sign = '-'
    if random_bool == 0:
        sign = ''

    random_str = sign + random_str

    normalized_random_str = normalize_string(random_str, string_size)

    return normalized_random_str





