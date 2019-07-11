# coding=utf-8
import requests
import cookielib
import json
# admin系统登录接口
url = "https://sit-manage-onerway.ronhan.com/login.htm"
headers ={"Connection": "keep-alive",
          "Content-Length": "33",
          "Cache-Control": "max-age=0",
          "Origin": "https://sandbox-manage-onerway.ronhan.com",
          "Upgrade-Insecure-Requests": "1",
          "Content-Type": "application/x-www-form-urlencoded",
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
          "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
          "Referer": "https://sandbox-manage-onerway.ronhan.com/login.htm",
          "Accept-Encoding": "gzip, deflate, br",
          "Accept-Language": "zh-CN,zh;q=0.9"
}

par = {"username":"admin","password":"123123zxc"}

seson = requests.session()  # 用session保持登录

r_resu = seson.post(url=url, headers=headers,verify=False,data=par)
print("------------------------------adcd")
print(r_resu.text)
print(seson.cookies)
print(r_resu.cookies)
print(r_resu.status_code)
print("---------------------------------------123456")


# admin系统 店铺查询请求
url1 = "https://sit-manage-onerway.ronhan.com/sysMerchant/queryMerchant.htm"
headers1 = {"Connection": "keep-alive",
           "Upgrade-Insecure-Requests": "1",
           "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
           "Referer": "https://sandbox-manage-onerway.ronhan.com/index.htm",
           "Accept-Encoding": "gzip, deflate, br",
           "Accept-Language": "zh-CN,zh;q=0.9"

}

r_resu1 = seson.request(method="GET", url=url1, headers=headers1, verify=False)
print(r_resu1.text)


# url = "https://www.baidu.com/"
# r = requests.get(url, verify=False)
#
# #将RequestsCookieJar转换成字典
# c = requests.utils.dict_from_cookiejar(r.cookies)
#
# print(r.cookies)
# print(type(r.cookies))
#
# print(c)
# print(type(c))
#
#
# for a in r.cookies:
#     print(a.value)
# admin系统 商户调账申请

url2 = "https://sit-manage-onerway.ronhan.com/merchantAccountRecord/insertAccountRecord.htm"
pam = {"accountType":"2","accountMoney":"40","merNo":"290746918668214272","merName":"张厚荣","remark": "入账40","currencyCode": "EUR"}
r_resu2 = seson.post(url=url2,data=pam,verify=False)
# print(json.dumps(r_resu2.json(),indent=2,sort_keys=False,ensure_ascii=False))

