# coding=utf-8
import json
import time
import logging
'''list 操作
        append
        count
        extend
        index
        pop
        remove
        reverse
        sort
        sorted
    string 操作
        find
        join
        lower
        replace
        split
        strip
        translate
'''


list_str = ["a","b","c"]

list_str.append("f")    #添加元素到末尾
print(list_str)

list_str.insert(1,"g")    #添加元素到指定索引位置
print(list_str)

list_str.pop(1)
print(list_str)

dic_str = {"xiaoming":75,"xiaohua":82,"xiaocai":60}
print(dic_str)
dic_str["xiaoqing"] = 89
print(dic_str)
print("xiao" in dic_str)
print(dic_str.get("ss"))
print(dic_str.get("xiaohua"))

