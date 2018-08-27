
from common.generator.data_generator import get_data
from common.constants import *

NUM_OF_DIGITS_IN_OPERAND = 3
def test_generate_data():
    inputs, labels, generation_info, _, _ = get_data(20)
    assert len(inputs) == len(labels)
    assert generation_info[INPUT_SIZE] == 8
    assert len(inputs) == 20
