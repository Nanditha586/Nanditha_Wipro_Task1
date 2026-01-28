import pytest
def divide(num1,num2):
    return num1/num2
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1,0)

