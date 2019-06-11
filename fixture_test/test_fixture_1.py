# coding=utf-8
import pytest

# 实现场景：用例1需要先登录，用例2不需要登录，用例3需要先登录
# 不带参数时默认scope="function"
# 如果@pytest.fixture()里面没有参数，那么默认scope="function"，也就是此时的级别的function，针对函数有效
@pytest.fixture()
def login():
    print("输入账号密码，登录")


def test_s1(login):
    print("用例1登录，然后其他操作")


def test_s2():
    print("用例2不需要登录")


def test_s3(login):
    print("用例3登录，然后其他操作")