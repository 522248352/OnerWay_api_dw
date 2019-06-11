#coding=utf-8
import xlrd
import os
import csv

abspath = os.path.abspath(".")
print(abspath)
file_excel = xlrd.open_workbook("./test_case_data/test.xls")

print(file_excel.nsheets)
print(file_excel.sheet_names())
print(file_excel.sheet_by_name("Sheet1"))
print(type(file_excel.sheet_by_name("Sheet1")))
print(file_excel.sheet_by_name("Sheet1").nrows)
print(file_excel.sheet_by_name("Sheet1").ncols)
print(file_excel.sheet_by_name("Sheet1").row(0))
print(file_excel.sheet_by_name("Sheet1").row_values(0))
print(file_excel.sheet_by_name("Sheet1").cell(0,0).value)

print("-------------csv-------------")

with open("./test_case_data/csv.csv", "r") as filcsv:
    file_csv = csv.DictReader(filcsv)
    for row in file_csv:
        print(row)
        print(type(row))


print(open("./test_case_data/test.xml","r").read())
print("--------")
strs = str(123456)
for a in strs:
    print(a)

def test_daxiao():
    # 字符串 "axbyczdj"，如果得到结果“abcd”
    a = 'axbyczdj'
    print(a[::2])



if __name__ == '__main__':
    print(os.path.dirname('.'))
