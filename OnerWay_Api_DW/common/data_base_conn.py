# coding=utf-8
import psycopg2
from getConfig import GetConfigVal

class Data_Base_Conn(object):


    def conn(self):

        gcfv = GetConfigVal()
        database = gcfv.getVal("database_sandbox", "database")
        user = gcfv.getVal("database_sandbox", "user")
        password = gcfv.getVal("database_sandbox", "password")
        host = gcfv.getVal("database_sandbox", "host")
        port = gcfv.getVal("database_sandbox", "port")

        try:
            conn = psycopg2.connect(database=database, user=user, password=password, host=host, port=port)
        except:
            print("conn异常")

        return conn

    def sql(self,sql):

        conns = self.conn()
        course = conns.cursor()

        try:
            course.execute(sql)
            conns.commit()
        except Exception as e:
            print("执行异常")

        else:
            rows = course.fetchall()
            return rows
        course.close()
        conns.close()