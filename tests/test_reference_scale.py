from ETS_CookBook import reference_scale


def test_basic():
    test_list = [1, 2, 10.8]
    test_scale = [1, 20]
    assert reference_scale(test_list) == test_scale


def test_zero():
    test_list = [0, 1, 10.8]
    test_scale = [0, 20]
    assert reference_scale(test_list) == test_scale
