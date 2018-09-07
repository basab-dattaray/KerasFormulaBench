import numpy as np

def noise_mgr(noise_factor = .01):
    def fn_add_noise_to_array_of_char_strings(char_str_array):
        len_of_array = len(char_str_array)

        index_increment = round(len_of_array * noise_factor)
        string_size = len(char_str_array[0])
        for i in range(0, len_of_array, index_increment):
            random_str = ''
            for j in range(0, string_size):
                rnd_digit = np.random.randint(10)
                rnd_chr = str(rnd_digit)
                random_str=  random_str + rnd_chr
            char_str_array[i] = random_str
    return fn_add_noise_to_array_of_char_strings




