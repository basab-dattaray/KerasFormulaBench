NUM_OF_INPUT_PARTS = 8

from common.generator.normalizer import *

def poly(plugin_name, fn_calc, max_input_width, max_label_width):
    abs_path_to_json_scratch_file = None


    def fn_generate_data_given_input_strings_impl(string_of_inputs):
        maxlen_inputs, maxlen_labels = load_char_widths(abs_path_to_json_scratch_file)

        trimmed_input_strings = list( map(lambda s: s.strip(), string_of_inputs))
        fn_iterate = workit_file_generator_mgr(trimmed_input_strings)

        inp_str_arr, out_str_arr = create_set_of_inpstr_outstr_pairs(fn_iterate)

        norm_inp_str_arr = normalize_list_of_strings(inp_str_arr, maxlen_inputs)
        norm_out_str_arr = normalize_list_of_strings(out_str_arr, maxlen_labels)

        return (norm_inp_str_arr, norm_out_str_arr)

    def fn_generate_data_impl(num_samples):
        nonlocal  abs_path_to_json_scratch_file
        inputs, outputs = generate_data_from_random_numbers(num_samples)

        input_width = get_max_width_of_list_items(inputs)
        if max_input_width > 0:
            input_width = max_input_width

        label_width = get_max_width_of_list_items(outputs)
        if max_label_width > 0:
            label_width = max_label_width

        inputs, labels = normalize_sizes(inputs, input_width, label_width, outputs)

        save_char_widths(abs_path_to_json_scratch_file, input_width, label_width)

        return (inputs, labels)

    def generate_data_from_random_numbers(num_samples):

        fn_iterate = random_number_generator_mgr(num_samples)
        inp_str_arr, out_str_arr = create_set_of_inpstr_outstr_pairs(fn_iterate)
        return inp_str_arr, out_str_arr

    def random_number_generator_mgr(num_of_samples):
        def random_number_generator():
            count = 0
            while count < num_of_samples:
                inp_arr = []
                for i in range(NUM_OF_INPUT_PARTS):
                    inp_digit = np.random.randint(10)
                    inp_arr.append(inp_digit)

                out_num = convert_inp_str_to_out_str(inp_arr)
                out_str = str(out_num)
                inp_str = ''
                for digit in inp_arr:
                    d_str = str(digit)
                    inp_str = inp_str + d_str

                yield inp_str, out_str

                count = count + 1

        return random_number_generator

    def workit_file_generator_mgr(inp_strings):
        def workit_file_generator():
            i = 0
            while i < len(inp_strings):
                inp_str = inp_strings[i]
                out_str = convert_inp_str_to_out_str(inp_str)
                yield inp_str, out_str
                i += 1
        return workit_file_generator

    def convert_inp_str_to_out_str(inp_str):
        out_num = 0
        for chr in inp_str:
            digit = int(chr)
            out_num = out_num + fn_calc(digit)
        out_str = str(round(out_num))
        return out_str



    def create_set_of_inpstr_outstr_pairs(fn_iterate):
        inp_str_arr = []
        out_str_arr = []
        for inp_str, out_str in fn_iterate():
            inp_str_arr.append(inp_str)
            out_str_arr.append(out_str)

        return inp_str_arr, out_str_arr

    abs_path_to_json_scratch_file = get_abs_path('plugins/' + plugin_name + '/model_data/sizes.json')

    return  fn_generate_data_impl, fn_generate_data_given_input_strings_impl


# if __name__ == '__main__':
#     # abs_coeffs_file_path = get_abs_path('common/plugins/' + 'expr_calc' + 'model_data/COEFFS.TXT')
#     # inputs = get_lines_from_file(abs_coeffs_file_path)
#
#     fn_calc, fn_generate_one_sample, fn_generate_data = poly([40.75])
#     input, label = fn_generate_one_sample(NUM_OF_INPUT_PARTS)
#     print(input, label)
#
#     inputs, outputs = fn_generate_data(3)
#
#     print(inputs, outputs)