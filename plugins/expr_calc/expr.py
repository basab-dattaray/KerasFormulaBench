from common.generator.data_bender import *
from common.misc.fileops import *
NUM_OF_INPUT_PARTS = 8

from plugins.expr_calc.normalizer import *

def poly(plugin_name, coeff_arr):
    abs_path_to_json_scratch_file = None

    def fn_calc(in_int):
        out_int = -20 - .15 * in_int + .125 * (in_int ** 2)
        i = 0
        for c in coeff_arr:
            out_int += coeff_arr[i]
        return out_int * 100

    def fn_generate_one_sample(n):
        out_int = 0
        inp_array = []
        for i in range(n):
            randomInt = np.random.randint(10)
            inp_array.append(randomInt)
            out_int = out_int + fn_calc(randomInt)
        return (inp_array, out_int)

    def fn_generate_data(num_samples):
        nonlocal  abs_path_to_json_scratch_file
        inputs = []
        outputs = []

        for _ in range(num_samples):
            inp_array, out_int = fn_generate_one_sample(NUM_OF_INPUT_PARTS)
            inp_str = ''
            for inp_item in inp_array:
                s = str(inp_item)
                inp_str = inp_str + s
            inputs.append(inp_str)
            outputs.append(str(round(out_int)))

        maxlen_inputs = get_maxlen_of_listitems(inputs)
        maxlen_labels = get_maxlen_of_listitems(outputs)

        inputs, labels = normalize_sizes(inputs, maxlen_inputs, maxlen_labels, outputs)

        save_sizes(abs_path_to_json_scratch_file, maxlen_inputs, maxlen_labels)

        return (inputs, labels)



    def fn_generate_data_given_input_strings_local(string_of_inputs):
        nonlocal  abs_path_to_json_scratch_file
        maxlen_inputs, maxlen_labels = get_sizes(abs_path_to_json_scratch_file)

        trimmed_input_strings = map(lambda s: s.strip(), string_of_inputs)

        # trim_inp_str  = input_string.strip()

        inp_str_arr = []
        out_str_arr = []
        for inp_str in trimmed_input_strings:
            out_num = 0
            for chr in inp_str:
                digit = int(chr)
                out_num = out_num + fn_calc(digit)
            inp_str_arr.append(inp_str)
            out_str = str(round(out_num))
            out_str_arr.append(out_str)

        norm_inp_str_arr = normalize(inp_str_arr, maxlen_inputs)
        norm_out_str_arr = normalize(out_str_arr, maxlen_labels)


        return (norm_inp_str_arr, norm_out_str_arr)



    abs_path_to_json_scratch_file = get_abs_path('plugins/' + plugin_name + '/model_data/sizes.json')

    return  fn_generate_data, fn_generate_data_given_input_strings_local


if __name__ == '__main__':
    # abs_coeffs_file_path = get_abs_path('common/plugins/' + 'expr_calc' + 'model_data/COEFFS.TXT')
    # inputs = get_lines_from_file(abs_coeffs_file_path)

    fn_calc, fn_generate_one_sample, fn_generate_data = poly([6, -.5, .25])
    input, label = fn_generate_one_sample(NUM_OF_INPUT_PARTS)
    print(input, label)

    inputs, outputs = fn_generate_data(3)

    print(inputs, outputs)