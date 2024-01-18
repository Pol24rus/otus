from src.Rectangle import Rectangle
import pytest
# from datetime import datetime


def test_positive(get_rectangle):
    a, b, area = get_rectangle
    r = Rectangle(a, b)
    assert r.get_area() == area
