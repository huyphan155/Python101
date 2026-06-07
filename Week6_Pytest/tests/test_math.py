import pytest

from apps.math_tool import divide


def test_divide_ok():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)