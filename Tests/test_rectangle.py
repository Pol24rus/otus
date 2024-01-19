from src.Rectangle import Rectangle
import pytest


def test_positive_int():
    r = Rectangle(3, 4)
    assert r.get_area() == 12, f"Площадь прямоугольника со сторонами {r.side_a} и {r.side_b} неверная"


def test_positive_float():
    r = Rectangle(3.3, 4.5)
    assert r.get_area() == 14.85, f"Площадь прямоугольника со сторонами {r.side_a} и {r.side_b} неверная"
