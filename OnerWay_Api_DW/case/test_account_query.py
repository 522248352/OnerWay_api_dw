# coding=utf-8
from OnerWay_Api_DW.common.getConfig import GetConfigVal
from OnerWay_Api_DW.common.public_requests import PublicRequest
import json
'账号查询'

def test_account_query():

    s_b = "-"*20
    print(s_b+"账号查询"+s_b)
    path = "/merchant/show.htm"
    gcfv = GetConfigVal()
    hosts = gcfv.getVal("API", "HOSTS")
    partnerid = gcfv.getVal("API", "PARTNERID")
    merno = gcfv.getVal("API", "MERNO_NO_USERID")

    params = {'partnerId':partnerid, 'merNo':merno}

    req = PublicRequest()
    r = req.get_resu(paths=path, data=params)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False, sort_keys=False))
    status = r.json()["status"]
    code = r.json()["code"]
    assert status == 1 and code == 101111111

