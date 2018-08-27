def test_set_plug():
    plugname_old = get_plugname()
    set_plugname("abc")
    assert get_plugname() == "abc"
    set_plugname(plugname_old)
    assert get_plugname() == plugname_old