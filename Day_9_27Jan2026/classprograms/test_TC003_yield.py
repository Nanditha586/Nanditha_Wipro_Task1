import pytest
@pytest.fixture()
def setup_teardown():
    print("setup")
    yield
    print("teardown")