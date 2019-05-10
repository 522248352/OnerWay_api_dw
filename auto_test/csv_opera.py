# coding=utf-8
import csv
import os
import pytest
csv_file = csv.reader(open(r"D:\eclipse-workspace\Tests\Api_TestCase\auto_test\test_case_data\csv.csv", "r"))
# csv_file_dic = csv.DictReader(fieldnames="D:\csv.csv")

with open(r"D:\eclipse-workspace\Tests\Api_TestCase\auto_test\test_case_data\csv.csv", "r") as filename:
    csv_re = csv.DictReader(filename)
    print(csv_re)
    print(type(csv_re))
    a = []
    for row in csv_re:
        print(row)
        a.append(row)

