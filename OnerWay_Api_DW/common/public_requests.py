# coding=utf-8
import requests
from OnerWay_Api_DW.common.getConfig import GetConfigVal

class PublicRequest(object):

    def get_resu(self,paths,data,file =None):

        gcfv = GetConfigVal()
        hosts = gcfv.getVal("API", "HOSTS")
        url = hosts + paths
        r = requests.post(url= url,data=data,files=file)
        return r