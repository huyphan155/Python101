import pytest
from apps.math_tool import divide
from apps.math_tool import calculate
from unittest.mock import patch
from unittest.mock import MagicMock


def test_divide_ok():
    assert divide(10, 2) == 5


def test_divide_zero():
    with pytest.raises(ValueError):
        divide(10, 0)

def test_calculate_mock():
    with patch(
            "apps.math_tool.get_number",
            return_value=100
    ):
        result = calculate()
        assert result == 200

def test_calculate_magic_mock_og():
    with patch(
            "apps.math_tool.get_number",
            side_effect=[10, 20]
    ):
        result = calculate()
        assert result == 30

def test_calculate_magic_mock():
    mock_func = MagicMock(
        side_effect=[10, 20]
    )

    result = mock_func()
    assert result == 10
    result = mock_func()
    assert result == 20

