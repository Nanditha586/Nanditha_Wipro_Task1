import pytest
from utilities.helper import add, subtract

def test_add_function():
    print("Testing add function")
    assert add(10, 5) == 15

def test_subtract_function():
    print("Testing subtract function")
    assert subtract(10, 5) == 5