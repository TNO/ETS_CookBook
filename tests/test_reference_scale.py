import typing as ty

from ETS_CookBook import ETS_CookBook as cook


def test_basic() -> None:
    test_list: ty.List[float] = [1, 2, 10.8]
    test_scale: ty.List[float] = [1, 20]
    assert cook.reference_scale(test_list) == test_scale


def test_zero() -> None:
    test_list: ty.List[float] = [0, 1, 10.8]
    test_scale: ty.List[float] = [0, 20]
    assert cook.reference_scale(test_list) == test_scale
