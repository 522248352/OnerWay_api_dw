# coding=utf-8
import logging

# 5种打日志的方法： debug 、info 、warning 、error 、critical。默认的是WARNING，当在WARNING或之上时才被跟踪。

def loggingTest():
    'logging-- filename 指定日志存放文件，level 指定logging级别'
    logging.basicConfig(level=logging.INFO, filename=r"D:\eclipse-workspace\Tests\Api_TestCase\OnerWay_Api_DW\logs\logs.log")
    logging.debug("hi,debug")
    logging.info("hi,info")
    logging.warning("hi,warning")
    logging.error("hi,error")
    logging.critical("hi,critical")

def loggerTest():
    '''
    指定哪些输入到文件，哪些输入到控制台
    %(levelno)s: 打印日志级别的数值
    %(levelname)s: 打印日志级别名称
    %(pathname)s: 打印当前执行程序的路径，其实就是sys.argv[0]
    %(filename)s: 打印当前执行程序名
    %(funcName)s: 打印日志的当前函数
    %(lineno)d: 打印日志的当前行号
    %(asctime)s: 打印日志的时间
    %(thread)d: 打印线程ID
    %(threadName)s: 打印线程名称
    %(process)d: 打印进程ID
    %(message)s: 打印日志信息
    '''

    logger_name = logging.getLogger(__name__)
    logger_name.setLevel(level=logging.INFO)

    # 创建 handler 输出到文件 mode='a' 默认模式是append，日志会添加到文件不会覆盖而是追加，w会覆盖之前的日志信息
    handler = logging.FileHandler(filename=r"D:\eclipse-workspace\Tests\Api_TestCase\OnerWay_Api_DW\logs\loggername.log", mode='w')
    handler.setLevel(level=logging.INFO)

    # handler 输出到控制台
    ch = logging.StreamHandler()
    ch.setLevel(level=logging.DEBUG)

    # 创建 logging format
    formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s - %(lineno)d")
    handler.setFormatter(fmt=formatter)
    ch.setFormatter(fmt=formatter)

    # add the handlers to the logger_name
    logger_name.addHandler(handler)
    logger_name.addHandler(ch)

    logger_name.info("hello, INFO")
    logger_name.debug("print to DEBUG")
    logger_name.error("ERROR logging")
    logger_name.warning("WARNING logging")
    logger_name.critical("CRITICAL logging")

if __name__ == "__main__":
    loggerTest()