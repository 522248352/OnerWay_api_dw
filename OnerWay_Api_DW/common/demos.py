# coding=utf-8
import pytest
import json
# json.dumps() json.loads() json.dump() json.load()
a = 1
print("%04d"%a)
print(2**3)
for i in range(100,1000):
    str_1 = str(i)
    a = 0
    for j in str_1:
        a = a+int(j)**3
    if i == a:
        print(i)

test_lis = [1,8,15,9,62,52]
for j in range(len(test_lis)):
    for i in range(len(test_lis)):
        if i+1 > 5:
            break
        if test_lis[i] > test_lis[i+1]:
            test_lis[i],test_lis[i+1] = test_lis[i+1],test_lis[i]

print(test_lis)

sg = 1
for i in range(1,4):
    sg = sg*i
print(sg)

def jiec(n):
    if n ==1:
        return 1
    if n > 1:
        return n*jiec(n-1)

def mic(x,n):
    if n == 0:
        return 1
    else:
        return x*mic(x,n-1)



