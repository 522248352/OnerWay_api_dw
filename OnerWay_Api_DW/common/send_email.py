# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
import time
import logging

'''
发送邮件（QQ邮件）
'''

def send_email(filename):

    #   打开报告文件读取文件内容
    f= open(filename,"r")
    file_msg = f.read()
    f.close()

    #   邮件服务器
    smtpserver = 'smtp.qq.com'

    #   发件人用户名和密码 不是登录密码，是授权码
    user = "522248352@qq.com"
    password = "jagmcfcgkebubgbf"

    #   发件人
    sender = "522248352@qq.com"

    #   收件人
    receiver = '872230912@qq.com'

    #   邮件主题
    subject = "主题测试:Python test send email"

    #   邮件设置
    msg = MIMEText(file_msg,'plain','utf-8')
    msg['subject'] = Header(subject,'utf-8')
    msg['from'] = sender

    #   连接服务器，登录服务器，发送邮件
    # smtp = smtplib.SMTP()
    smtp = smtplib.SMTP_SSL() # 用SMTP报错：Connection unexpectedly closed ，用SSL加密的然后换成SMTP_SSL
    smtp.connect(smtpserver,465)
    smtp.login(user,password)

    try:
        smtp.sendmail(sender,receiver,msg.as_string())
        # logging.log("aaa")

    except Exception as a:
        print("send fail:",a )
    else:
        print("send success")

    # 结束SMTP会话
    smtp.quit()
    print('send email success!')

if __name__ == "__main__":
    print("55555")
    send_email(filename=r"D:\eclipse-workspace\Tests\Api_TestCase\auto_test\test_case_data\csv.csv")