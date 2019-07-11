# coding=utf-8
import requests
import json
import sys,os
sys.path.append('D:\\eclipse-workspace\\Tests\\Api_TestCase')
sys.path.append('../')
from auto_test.config import global_parameter
from auto_test.public import public_request
import configparser
import time
import xlrd

# web接口登录不通，店铺查询通了
def test_login_web():
    paths = "https://sit-myaccount-onerway.ronhan.com/login.htm"
    param = {"loginType":2,"username":"new015@qq.com","password":"123456asd"}
    test_cook = requests.session()
    r_res = test_cook.post(url=paths,data=param,verify=False)
    print(r_res.text)
    print("9996")









def test_dianpu():
    url = "https://sandbox-myaccount-onerway.ronhan.com/shopinfo/index.htm"
    he = {"cookie": "agency_iuid=167871345898692608; webid=1a70023d-e629-419c-9fac-a3d9a1a29afe; JSESSIONID=3388C93D49BAEE3BDEC1FD9988A926A4.onerway_web-8081"}
    r = requests.get(url=url,headers=he,verify=False)

    print("dianpu"+r.text)

def test_sele_dianpu():
    url="https://sandbox-myaccount-onerway.ronhan.com/shopinfo/channellist.htm"
    pa = {"map['andChannelIdEqualTo']": "290735950877822976"}
    he = {"cookie": "agency_iuid=167871345898692608; JSESSIONID=F44B4B33542D65B888D2DEC05CB4BA46.onerway_web-8081; webid=bfcfb4e2-5817-425a-8768-de27e55d4323"}
    r = requests.post(url=url,data=pa,verify=False,headers=he)
    print("sele11111")
    # print(json.dumps(r.json(),indent=2,ensure_ascii=False,sort_keys=False))
    print(r.text)

# if __name__ == '__main__':
#
#
#     test_dianpu()