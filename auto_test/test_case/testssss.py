# coding=utf-8
import requests
import json
import sys
sys.path.append('D:/eclipse-workspace/Tests/Api_TestCase/auto_test/config/')
from auto_test.config import global_parameter
from auto_test.public import public_request

def test_acc():
    paths = "/transaction/showWithdrawAccount.htm"
    pam = {"partnerId": global_parameter.PARTNERID, "merNo": global_parameter.MERNO_NO_USERID}

    r_obj = public_request.Public_Request()
    r_resu = r_obj.public_request(pas=paths, parameters=pam)

    print(json.dumps(r_resu.json(), indent=2, sort_keys=False, ensure_ascii=False))
    assert r_resu.json()["status"] == 1
    assert r_resu.json()["code"] == 101

if __name__ == '__main__':

    test_acc()