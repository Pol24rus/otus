from src.Square import Square
import pytest


def test_positive_square():
    s = Square(6)
    assert s.get_area() == 36
    assert s.get_perimetr() == 24


def test_negative_square():
    with pytest.raises(ValueError):
        Square(-25)
