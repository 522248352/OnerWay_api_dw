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

# # python2.7
# pwd = "xxx" + chr(163) + "fj"
# checkcode = hashlib.md5(pwd).hexdigest()
# print checkcode # ea25a328180680aab82b2ef8c456b4ce
#
# # python3.6
# pwd = "xxx" + chr(163) + "fj"
# checkcode = hashlib.md5(pwd.encode("utf-8")).hexdigest()
# print(checkcode) # b517e074034d1913b706829a1b9d1b67