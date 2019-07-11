# coding=utf-8
import pytest
import json
import requests
# from requests_html import HTMLSession
import string
from string import Template
import types
import csv

lis = ["a","b","c","d","e","f"]
for i in range(len(lis)):
    print(lis[i],i)

for i,j in enumerate(lis):
    print(i,j)

a = 1
b = 2
print(cmp(a,b))
print(types.IntType)
print(isinstance(1,(int,str,float)))

print(lis[:None])
print(range(-1,-6,-1))


# print(max(4,9,6,key='3'))

print(reversed(lis))
test_lis = Template("python ${key1} very ${key2},is num ${key3}")
print(test_lis.substitute(key1="is",key2="good",key3=1))
s1,s2,s3 = "ab111","do222","euitf"
print(zip(s1,s2,s3))
print("ab:"+unicode(1))
print("a" in "adc")

# lsi = []
# for i in range(5):
#     shu = raw_input("请输入数字：")
#     lsi.append(shu)
#     print(type(lsi[i]))

# dict_test = {"a":1,"b":2}
#
# print(dict_test.setdefault("c",3))
# print(dict_test)
# for isss in dict_test.keys():
#     print(isss)


list_1 = [6,10,9,1,8]
for a in range(5):
    for i in range(len(list_1)):
        if i+1>=5:
            break
        if list_1[i] > list_1[i+1]:
            list_1[i],list_1[i+1] = list_1[i+1],list_1[i]


print(list_1)

print(zip((1,2,3),("a","b","c")))

