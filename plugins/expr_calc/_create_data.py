import  numpy as np

PLUS = '+'
MINUS = '-'

def calculate(input):
    stack = []
    for a in input:
        if type(a) is int:
            stack.append(a)
            continue

        op1, op2 = stack.pop(), stack.pop()

        if a == PLUS:
            stack.append(op2 + op1)
        elif a == MINUS:
            stack.append(op2 - op1)
    return stack.pop()

def manage_data(num_of_items):
    _operator_dict = {
        0: PLUS,
        1: MINUS
    }

    def get_next():
        n = np.random.randint(10)
        opcode = np.random.randint(_operator_dict.__len__())
        operator = _operator_dict[opcode]
        while True:
            yield (operator, n)
            n = np.random.randint(10)
            opcode = np.random.randint(_operator_dict.__len__())
            operator = _operator_dict[opcode]

    def generate_data():
        input_list = [np.random.randint(10)]
        i = 0
        for operator, n in get_next():
            input_list.append(n)
            input_list.append(operator)
            i = i + 1
            if i > num_of_items:
                break
        return input_list

    def get_input_string(input_list):
        input_str = ''
        for x in input_list:
            if type(x) != 'str':
                input_str = input_str + str(x)
            else:
                input_str = input_str + x
        return input_str

    def fn_get_input_and_label():
        input_list = generate_data()
        answer = calculate(input_list)
        input = get_input_string(input_list)
        label = str(answer)
        return input, label

    return fn_get_input_and_label


if __name__ == '__main__':
    fn_get_input_and_label = manage_data(3)

    inp, lab = fn_get_input_and_label()
    inp2, lab2 = fn_get_input_and_label()

    input = None


