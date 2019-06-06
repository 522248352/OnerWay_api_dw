# coding=utf-8
import hashlib

#'加密'
def md5(str1):
    md = hashlib.md5()
    md.update(str1)
    md_5 = md.hexdigest()
    return md_5

def hash_1(str1):
    sh = hashlib.sha1()
    sh.update(str1)
    sha_1 = sh.hexdigest()
    return sha_1

strtest = "admin123123zxc"
print(md5(strtest))
print(hash_1(strtest))