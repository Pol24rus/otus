from src.Circle import Circle
import pytest
from datetime import datetime


@pytest.mark.parametrize(("side_a", "area"),
                         [(5, 19.634954084936208),
                          (3.5, 9.62112750161874),
                          (12, 113.09733552923255)],
                         ids=["d=5", "d=3.5", "d=12"])
def test_positive_int(side_a, area):
    c = Circle(side_a)
    assert c.get_area() == area


@pytest.mark.skipif(condition=datetime.now().hour > 22, reason="Too late")
@pytest.mark.skipif(condition=datetime.now().hour < 7, reason="Too early")
def test_positive_float():
    c = Circle(3.5)
    assert c.get_area() == 9.62112750161874
