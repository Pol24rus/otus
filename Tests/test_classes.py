from src.Rectangle import Rectangle


def test_positive():
    r = Rectangle(3, 4)
    assert r.get_area() == 13
