from src.Triangle import Triangle
import pytest


def test_positive(get_triangle):
    a, b, c, d, area, perimetr = get_triangle
    t = Triangle(a, b, c, d)
    assert t.get_area() == area
    assert t.get_perimetr() == perimetr


def test_negative_triangle():
    with pytest.raises(ValueError):
        Triangle(0, 1, 25, 0)

# 3, 4, 5, 0.3, 3.5999999999999996, 12