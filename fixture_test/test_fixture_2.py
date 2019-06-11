# coding=utf-8
import pytest
param = ["a","b","c"]
@pytest.fixture(scope="module",params=param)
def dem(request):
    print("开始")
    print(request.param)
    yield request.param
    print("结束")

def test_demo(dem):
    de = dem
    print(de)



if __name__ == "__main__":
    pytest.main("-s","test_fixture_2.py")