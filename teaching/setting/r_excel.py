#coding:utf-8

import os, xlrd

# ======== Reading db_config.ini setting ===========

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 返回当前文件所在目录的上级目录
base_dir=base_dir.replace("/","\\")
foot = base_dir + "\\number\\foot.txt"  #找到excel数据配置文件
firefoxfile=base_dir+'\\photographa\\firefox.exe' #找到exe文件路径
photo_file=base_dir+'\\photographa\\p1.jpg'  #找到图片路径
file_path = base_dir + "/case_data.xlsx"  # 找到excel数据配置文件

file = xlrd.open_workbook(file_path)  # 打开一个xlsx文件
# 读取测试数据
sheet1 = file.sheets()[0]  # 获取第一个sheet1页面
B1 = sheet1.row(0)[1].value  # 读取url
B2 = sheet1.row(1)[1].value  # 读取用户名
B3= int(sheet1.row(2)[1].value)  # 读取用户密码
B4= sheet1.row(3)[1].value  # 读取用户密码
