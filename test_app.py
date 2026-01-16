# test_app.py
from app import area

def test_1():
    assert area(1) == 3.14

def test_2():
    assert area(0) == 0

def test_3():
    assert area(2) == 12.56
