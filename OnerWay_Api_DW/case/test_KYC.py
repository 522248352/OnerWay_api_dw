# coding=utf-8
import requests
import sys
sys.path.append("D:\\eclipse-workspace\\Tests\\Api_TestCase\\OnerWay_Api_DW")
sys.path.append("D:\\eclipse-workspace\\Tests\\Api_TestCase")
from OnerWay_Api_DW.common.getConfig import GetConfigVal
from OnerWay_Api_DW.common.public_requests import PublicRequest
from OnerWay_Api_DW.common.data_base_conn import Data_Base_Conn
import random
import json
import pytest

def test_kyc_open_business():

    '''商户开户KYC-企业-正常开户'''

    s_b = "-"*20
    print(s_b+"商户开户KYC-企业"+s_b)
    path = "/merchant/kyc.htm"
    gcfv = GetConfigVal()
    hosts = gcfv.getVal("API", "HOSTS")
    partnerid = gcfv.getVal("API", "PARTNERID")
    merno = gcfv.getVal("API", "MERNO_NO_USERID")
    ranword = random.choice("python")

    params = {"partnerId": partnerid,
               "accountType": 1,
               "area": "中国",
               "country": "中国",
               "province": "上海",
               "address": "上海市上海",
               "city": "上海",
               "name": "企业法人",
               "idCard": 588596854788889652,
               "idCardImg1": 241354094869118976,
               "idCardImg2": 241354094869118976,
               "merName": "api开户"+ranword,
               "businessNumber": 45821,
               "business": 241354094869118976}

    req = PublicRequest()
    r = req.get_resu(paths=path, data=params)
    print(r.text)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False, sort_keys=False))
    assert r.json()["status"] == 1
    assert r.json()["code"] == 10021
    mernos = r.json()["data"]["merNo"]

    dbc = Data_Base_Conn()
    sql = "SELECT * FROM m_merchant WHERE MER_NO =" + mernos
    rows = dbc.sql(sql)
    for row in rows:
        print(row)
    assert len(rows) == 1

def test_kyc_open_personal():

    '''商户开户KYC-个人-正常开户'''
    s_b = "-"*20
    print(s_b+"商户开户KYC-个人"+s_b)
    path = "/merchant/kyc.htm"

    gcfv = GetConfigVal()
    hosts = gcfv.getVal("API", "HOSTS")
    partnerid = gcfv.getVal("API", "PARTNERID")
    merno = gcfv.getVal("API", "MERNO_NO_USERID")
    ranword = random.choice("python")

    params = {"partnerId": partnerid,
              "accountType": 0,
              "area": "中国",
              "country": "中国",
              "province": "上海",
              "address": "上海市上海",
              "city": "上海",
              "name": "个人用户",
              "idCard": 588596854788889652,
              "idCardImg1": 241354094869118976,
              "idCardImg2": 241354094869118976,
              "idCardHandheld": 241354094869118976
              }

    req = PublicRequest()
    r = req.get_resu(paths=path, data=params)
    print(json.dumps(r.json(),indent=2,ensure_ascii=False,sort_keys=False))
    assert r.json()["status"] == 1
    assert r.json()["code"] == 10021
    mernos = r.json()["data"]["merNo"]

    dbc = Data_Base_Conn()
    sql = "SELECT * FROM m_merchant WHERE MER_NO =" + mernos
    rows = dbc.sql(sql=sql)
    for row in rows:
        print(row)
        print(unicode(row[0]))
    assert len(rows) == 1 and unicode(row[0]) == mernos

def test_kyc_open_hongkong():

    '''商户开户KYC-香港-正常开户'''
    s_b = "-"*20
    print(s_b+"商户开户KYC-香港"+s_b)
    path = "/merchant/kyc.htm"

    gcfv = GetConfigVal()
    hosts = gcfv.getVal("API", "HOSTS")
    partnerid = gcfv.getVal("API", "PARTNERID")
    merno = gcfv.getVal("API", "MERNO_NO_USERID")
    ranword = random.choice("python")

    params = {"partnerId": partnerid,
              "accountType": 1,
              "area": "中国香港",
              "country": "中国",
              "province": "上海",
              "address": "上海市上海",
              "city": "上海",
              "name": "企业香港用户",
              "idCard": 588596854788889652,
              "idCardImg1": 241354094869118976,
              "idCardImg2": 241354094869118976,
              "merName": "香港企业名称",
              "businessNumber": "YYZZ001112",
              "business": 241354094869118976,
              }

    req = PublicRequest()
    r = req.get_resu(paths=path, data=params)

    print(json.dumps(r.json(),indent=2,ensure_ascii=False,sort_keys=False))
    assert r.json()["status"] == 1
    assert r.json()["code"] == 10021
    mernos = r.json()["data"]["merNo"]

    dbc = Data_Base_Conn()
    sql = "SELECT * FROM m_merchant WHERE MER_NO =" + mernos
    rows = dbc.sql(sql=sql)
    for row in rows:
        print(row)
        print(unicode(row[0]))
    assert len(rows) == 1 and unicode(row[0]) == mernos