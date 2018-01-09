#coding:utf-8
'''云南省校园食品安全
前期准备数据：职业院校  800万  100人  12个月'''
from setting.driver import *
from selenium.webdriver.support.ui import Select
import time
import os

driver=chrome_log()
#上传被保险人信息页面
#选择职业院校
time.sleep(1)
driver.find_element_by_xpath('//*[@id="bxrType" and @value="31"]').click()
time.sleep(1)
s=driver.find_element_by_xpath(".//*[@id='jichubaofei']")
Select(s).select_by_visible_text("800万元")
time.sleep(1)
driver.find_element_by_id('stuNum').send_keys(100)
time.sleep(1)
s1=driver.find_element_by_xpath("//*[@id='term']")
Select(s1).select_by_visible_text("12")
time.sleep(1)
driver.find_element_by_xpath('//*[@onclick="gotoStep3();return false;"]').click()
#保费计算页面 点击下一步
time.sleep(1)
driver.find_element_by_id('step3_ok').click()
#确认投保单页面
time.sleep(2)
driver.find_element_by_id('readAll').click()
driver.find_element_by_id('step4_ok').click()
#获取保单号
time.sleep(1)
Insure_single_number=driver.find_element_by_partial_link_text("NO").text
driver.quit()

#-------上传单证-------
driver=firefox_log()
time.sleep(1)
driver.find_element_by_id("applicationFormCode").send_keys(Insure_single_number[4:])
s2=driver.find_element_by_id("applicationType")
Select(s2).select_by_visible_text("校园食品安全责任险")
time.sleep(1)
driver.find_element_by_id("Search").click()
time.sleep(1)
driver.find_element_by_id("uploadCertification").click()
#上传单证页面
time.sleep(1)
driver.find_element_by_id("uploadFile").click()
time.sleep(1)
os.system(firefoxfile + " " + photo_file) #上传附件
time.sleep(1)
driver.find_element_by_xpath('//*[@onclick="uploadCertificate()"]').click()
driver.switch_to_alert().accept()  #弹出框点击确认
time.sleep(1)
driver.switch_to_alert().accept()  #弹出框点击确认

#-------审核单证------
time.sleep(1)
driver.switch_to_default_content() #退出上个表单
driver.switch_to_frame("nav") #切换表单
time.sleep(1)
driver.find_element_by_xpath(".//*[@id='menu']/li[8]/ul/li[3]/ul/li/a").click()
#投保单号查询页面
driver.switch_to_default_content() #退出上个表单
driver.switch_to_frame("framecontent") #切换表单
time.sleep(1)
driver.find_element_by_id("applicationFormCode").send_keys(Insure_single_number[4:])
s2=driver.find_element_by_id("applicationType")
Select(s2).select_by_visible_text("校园食品安全责任险")
time.sleep(1)
driver.find_element_by_id("Search").click()
time.sleep(1)
driver.find_element_by_id("checkCertification").click()
#审核页面点击 通过
driver.find_element_by_xpath('//*[@class="b4"]').click()
driver.switch_to_alert().accept()
driver.quit()
f=open(foot,"a+")
f.write("\n（职业院校  800万  100人  12个月）："+Insure_single_number[4:].encode('utf-8'))
f.close()

