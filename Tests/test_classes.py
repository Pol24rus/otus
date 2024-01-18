# import sys
from src.Rectangle import Rectangle
import pytest
from datetime import datetime


# print(sys.path)
# @pytest.mark.parametrize(("side_a", "side_b", "area"),
#                          [(3, 5, 15),
#                           (3.5, 4.5, 15.75)],
#                          ids=["integer", "float"])
# def test_positive_int(side_a, side_b, area):
#     r = Rectangle(side_a, side_b)
#     assert r.get_area() == area


# @pytest.mark.skipif(condition=datetime.now().month == 1, reason="Bug")
# @pytest.mark.smoke
# def test_positive_float():
#     r = Rectangle(3.5, 4.5)
#     assert r.get_area() == 15.75


def test_negative_rectangle():
    with pytest.raises(ValueError):
        Rectangle(-3.5, -4.5)
