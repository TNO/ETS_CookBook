# Type hinting here seems to create issues
# Either with MyPy complaining about imports mising attributes
# or MyPy not working
import ETS_CookBook as cook


def test_basic():
    test_list = [1, 2, 10.8]
    test_scale = [1, 20]
    assert cook.reference_scale(test_list) == test_scale


def test_zero():
    test_list = [0, 1, 10.8]
    test_scale = [0, 20]
    assert cook.reference_scale(test_list) == test_scale
