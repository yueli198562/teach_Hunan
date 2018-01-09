#coding:utf-8

from selenium import webdriver
from setting.r_excel import *
import time
def chrome_log():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver.get(B1)
    driver.find_element_by_name("j_username").clear()
    driver.find_element_by_name("j_username").send_keys(B2)
    driver.find_element_by_name("j_password").clear()
    driver.find_element_by_name("j_password").send_keys(B3)
    driver.find_element_by_xpath('//*[@href="#"  and  @tabindex="3"]/img').click()
    # 点击左侧菜单云南省教育保险-在线投保-云南省校园视频安全责任
    driver.switch_to_frame("nav")  # 先切换frame表单
    driver.find_element_by_xpath("//*[@id='menu']/li[8]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[1]/a").click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[1]/ul/div/li[2]/a").click()
    driver.switch_to_default_content()  # 释放表单
    # 勾选须知
    time.sleep(2)
    driver.switch_to_frame("framecontent")  # 切换表单
    checkbox = driver.find_elements_by_xpath('//*[@name="checkbox"]')
    for i in checkbox:
        i.click()
    driver.find_element_by_xpath("//*[@id='step1_ok']").click()
    # 投保机构查询页面
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='selectOrg']").click()  # 点击查询按钮
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='result']/tr[1]/td[1]/input").click()  # 选择机构
    driver.find_element_by_xpath("//*[@id='ok']").click()  # 点击确定
    # 填写投保人信息页面
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='policyHolderInfo_email']").clear()  # 清空联系人邮箱
    driver.find_element_by_xpath("//*[@id='policyHolderInfo_email']").send_keys(B4)  # 清空联系人邮箱
    driver.find_element_by_id("step1_ok").click()  # 点击下一步
    return driver

def firefox_log():
    driver=webdriver.Firefox()
    driver.get(B1)
    driver.find_element_by_name("j_username").clear()
    driver.find_element_by_name("j_username").send_keys(B2)
    driver.find_element_by_name("j_password").clear()
    driver.find_element_by_name("j_password").send_keys(B3)
    driver.find_element_by_xpath('//*[@href="#"  and  @tabindex="3"]/img').click()
    driver.switch_to_frame("nav")  # 切换表单
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='menu']/li[8]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[@id='menu']/li[8]/ul/li[3]/a").click()
    time.sleep(1)
    driver.find_element_by_xpath(".//*[@id='menu']/li[8]/ul/li[3]/ul/li/a").click()
    # 投保单号查询页面
    driver.switch_to_default_content()  # 退出上个表单
    driver.switch_to_frame("framecontent")  # 切换表单

    return driver