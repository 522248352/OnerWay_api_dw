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
    paths = "https://sandbox-manage-onerway.ronhan.com/login.htm"
    params = {"loginType":"1","username":"15236325412","password":"123456asd"}
    # headers = {"accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    #             "accept-encoding": "gzip, deflate, br",
    #             "accept-language": "zh-CN,zh;q=0.9",
    #             "cache-control": "max-age=0",
    #             "content-length": "62",
    #             "content-type": "application/x-www-form-urlencoded",
    #             "Cookie": "agency_iuid=167871345898692608; webid=19d5e279-fde4-49b4-be38-07a929b89ce3; JSESSIONID=F44B4B33542D65B888D2DEC05CB4BA46.onerway_web-8081",
    #             "origin": "https://sandbox-myaccount-onerway.ronhan.com",
    #             "referer": "https://sandbox-myaccount-onerway.ronhan.com/login.htm",
    #             "upgrade-insecure-requests": "1",
    #             "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36"}
    headers = {"Cookie": "agency_iuid=167871345898692608; webid=19d5e279-fde4-49b4-be38-07a929b89ce3; JSESSIONID=F44B4B33542D65B888D2DEC05CB4BA46.onerway_web-8081"}
    cook = {"agency_iuid":"167871345898692608", "webid":"19d5e279-fde4-49b4-be38-07a929b89ce3", "JSESSIONID":"F44B4B33542D65B888D2DEC05CB4BA46.onerway_web-8081"}

    s = requests.session()
    # c = requests.cookie
    r = s.post(url=paths,data=params,headers=headers,verify=False)
    print("login_web")
    print(r.text)

def test_dianpu():
    url = "https://sandbox-myaccount-onerway.ronhan.com/shopinfo/index.htm"
    he = {"cookie": "agency_iuid=167871345898692608; JSESSIONID=F44B4B33542D65B888D2DEC05CB4BA46.onerway_web-8081; webid=bfcfb4e2-5817-425a-8768-de27e55d4323"}
    r = requests.get(url=url,headers=he,verify=False)

    print("dianpu"+r.text)

def test_sele_dianpu():
    url="https://sandbox-myaccount-onerway.ronhan.com/shopinfo/channellist.htm"
    pa = {"map['andChannelIdEqualTo']": "290735950877822976"}
    he = {"cookie": "agency_iuid=167871345898692608; JSESSIONID=F44B4B33542D65B888D2DEC05CB4BA46.onerway_web-8081; webid=bfcfb4e2-5817-425a-8768-de27e55d4323"}
    r = requests.post(url=url,data=pa,verify=False,headers=he)
    print("sele11111")
    print(json.dumps(r.json(),indent=2,ensure_ascii=False,sort_keys=False))

if __name__ == '__main__':


    test_dianpu()