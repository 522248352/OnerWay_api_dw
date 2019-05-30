# coding=utf-8
import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email import encoders
from email.mime.multipart import MIMEMultipart, MIMEBase
from getConfig import GetConfigVal
import logging

'发送邮件--附件，' \

'如果Email中要加上附件怎么办？带附件的邮件可以看做包含若干部分的邮件：文本和各个附件本身，' \
'所以，可以构造一个MIMEMultipart对象代表邮件本身，' \
'然后往里面加上一个MIMEText作为邮件正文，再继续往里面加上表示附件的MIMEBase对象即可：'

def send_Email_attac(filename):


    # 创建邮件对象
    msg = MIMEMultipart()

    #   发件人
    sender = "522248352@qq.com"

    #   收件人
    receiver = ['872230912@qq.com', 'wan.du@onerway.com']

    subject = "主题测试-附件:Python test send email"
    msg["from"] = sender
    msg["subject"] = Header(subject,'utf-8')

    # 邮件正文是 MIMEText
    msg.attach(MIMEText("测试附件功能中邮件的正文",'plain','utf-8'))

    # 添加附件就是加上一个MIMEBase，从本地读取一个csv文件:
    with open(filename, "rb") as f:


        # 设置附件的MIME和文件名，这里是csv类型:
        mime = MIMEBase("CSV","csv",filename="csv.csv")
        # mime = MIMEBase('image', 'png', filename='test.png')

        # 加上头信息
        mime.add_header('Content-Disposition', 'attachment', filename='csv.csv')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')

        # 把附件的内容读进来:
        mime.set_payload(f.read())

        # 用Base64编码:
        encoders.encode_base64(mime)

        # 添加到MIMEMultipart:
        msg.attach(mime)


        #   发件人用户名和密码 不是登录密码，是授权码
        user = "522248352@qq.com"
        cf = GetConfigVal()
        password = cf.getVal("email", "keyNum")


        smtp = smtplib.SMTP_SSL() # 用SMTP报错：Connection unexpectedly closed ，用SSL加密的然后换成SMTP_SSL
        smtp.connect('smtp.qq.com',465)
        smtp.login(user, password)

        try:
            smtp.sendmail(sender,receiver,msg.as_string())
            # logging.log("aaa")

        except Exception as a:
            print("send fail:", a )
            logging.exception("发送失败", exc_info=True)
        else:
            print("send email success!")

        # 结束SMTP会话
        smtp.quit()


if __name__ == "__main__":
    print("55555")
    send_Email_attac(filename=r"D:\eclipse-workspace\Tests\Api_TestCase\auto_test\test_case_data\csv.csv")