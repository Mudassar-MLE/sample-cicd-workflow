from src.math_operations import *

def test_add():
    assert add(1,1)==2
    assert add(2,2)==4
    assert add(4,5)==9

def test_sub():
    assert sub(2,1)==1
    assert sub(5,5)==0