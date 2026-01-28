import pytest
def test_addition():
    assert 2+2==4
@pytest.mark.skip(reason="Feature not implemented yet")
def test_payment():
    assert True
