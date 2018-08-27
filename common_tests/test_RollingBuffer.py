from common.misc.RollingBuffer import *

def test_creation_buffer_size_1():
    rb = RollingBuffer(1)
    rb.add(101)
    list = rb.get_last_n(1)
    assert list[0] == 101
    rb.add(102)
    list2 = rb.get_last_n(1)
    assert list2[0] == 102

def test_creation_buffer_size_2_return_1():
    rb = RollingBuffer(2)
    rb.add(101)
    list = rb.get_last_n(1)
    assert list[0] == 101
    assert list.__len__() == 1
    rb.add(102)
    list2 = rb.get_last_n(1)
    assert list2[0] == 102
    assert list2.__len__() == 1


def test_creation_buffer_size_2_add_2__return_2():
    rb = RollingBuffer(2)
    rb.add(101)
    rb.add(102)
    list2 = rb.get_last_n(2)
    assert list2[0] == 102
    assert list2[1] == 101
    assert list2.__len__() == 2

def test_creation_buffer_size_3_add_3_return_2():
    rb = RollingBuffer(3)
    rb.add(101)
    rb.add(102)
    rb.add(103)
    list2 = rb.get_last_n(2)
    assert list2[0] == 103
    assert list2[1] == 102
    assert list2.__len__() == 2

def test_creation_buffer_size_3_add_5_return_2():
    rb = RollingBuffer(3)
    rb.add(101)
    rb.add(102)
    rb.add(103)
    rb.add(104)
    rb.add(105)
    rb.add(106)
    list2 = rb.get_last_n(2)
    assert list2[0] == 106
    assert list2[1] == 105
    assert list2.__len__() == 2