import pytest
@pytest.yield_fixture()
def setUp():
    print("before")
    yield
    print("Once after")
def test_Method1(setUp):
    print("this is method 1")
def test_method2(setUp):
    print("2")
