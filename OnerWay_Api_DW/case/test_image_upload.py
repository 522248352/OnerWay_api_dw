# coding=utf-8
import json
import pytest
import sys
sys.path.append("D:\eclipse-workspace\Tests\Api_TestCase")
from OnerWay_Api_DW.common.getConfig import GetConfigVal
from OnerWay_Api_DW.common.public_requests import PublicRequest
'图片上传'

def test_image_upload():

    '''图片上传'''

    s_b = "-"*20
    print(s_b+"图片上传"+s_b)
    path = "/upload/image.htm"
    gcfv = GetConfigVal()
    hosts = gcfv.getVal("API", "HOSTS")
    partnerid = gcfv.getVal("API", "PARTNERID")
    merno = gcfv.getVal("API", "MERNO_NO_USERID")

    params = {'partnerId': partnerid}
    files = {"image": ("278.png", open(r"D:\278.png", "rb"), "image/png", {})}

    req = PublicRequest()
    r = req.get_resu(paths=path, data=params, file=files)
    print(json.dumps(r.json(), indent=2, ensure_ascii=False, sort_keys=False))

    status = r.json()["status"]
    code = r.json()["code"]

    assert status == 1 and code == 10021


