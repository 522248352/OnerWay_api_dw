# coding=utf-8
import configparser

class GetConfigVal(object):

    def getVal(self,sess, options):

        cf = configparser.ConfigParser()
        cf.read("D:\eclipse-workspace\Tests\Api_TestCase\OnerWay_Api_DW\config\config.ini")
        val = cf.get(sess,options)
        return val

if __name__ == '__main__':
    pass