#coding=utf8

from HTMLTestRunner import HTMLTestRunner
import unittest,os
from setting.send_email import *

base_dir = os.path.dirname(os.path.abspath(__file__)) # 返回当前文件所在目录的上级目录
foot= base_dir + "\\number\\foot.txt"  #找到excel数据配置文件

discover=unittest.defaultTestLoader.discover("./case",pattern="foot*.py")
if __name__=="__main__":
    runner = unittest.TextTestRunner()
    runner.run(discover)
    sed_mail(foot)  # 发送邮件









