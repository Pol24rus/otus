#import sys
from src.Rectangle import Rectangle
import pytest
from datetime import datetime


#print(sys.path)
def test_positive_int():
    r = Rectangle(3, 4)
    assert r.get_area() == 12


#@pytest.mark.skipif(condition=datetime.now().month == 1, reason="Bug")
@pytest.mark.smoke
def test_positive_float():
    r = Rectangle(3.5, 4.5)
    assert r.get_area() == 15.75
