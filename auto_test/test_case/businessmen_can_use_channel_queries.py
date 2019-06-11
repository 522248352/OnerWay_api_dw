
# coding=utf-8
import requests
from auto_test.config.global_parameter import *
#商户可用通道查询
def test_businessmen_can_use_channel():
    hosts = "https://sandbox-api-onerway.ronhan.com"

    url = hosts + "/channel/showMerchantChannelType.htm"

    parameter = {"partnerId":PARTNERID,"merNo":MERNO_NO_USERID}

    r = requests.post(url,data=parameter)
    print(r.text)
