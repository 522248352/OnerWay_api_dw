# coding=utf-8
import pytest

@pytest.fixture()
def logins():
    print("登录")

@pytest.mark.parametrize("test_input,expected",
                         [ ("3+5", 8),
                           ("2+4", 6),
                           ("6 * 9", 42),
                           ])
def test_eval(test_input, expected):
    assert eval(test_input) == expected

def test_1():
    print("test_1")

def test_2(logins):
    print("test_2")

def test_3():
    print("test_3")

if __name__ == '__main__':
    pytest.main(['-s','pytest_test.py::test_eval'])
    # pytest.main()