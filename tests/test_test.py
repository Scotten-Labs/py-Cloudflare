from src import *

def test_test():
    assert 1+1 == 2

def test_app():
    p = app()
    x = p.add(1,1)
    assert x == 2
