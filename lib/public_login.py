"""
作者:lxy
日期:2022年05月10日
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from soupsieve.css_types import Selector


def login(name,password):
    s = webdriver.Chrome()
    s.get('https://home.qyjmed.com/login')   #打开演示系统登录页

    if name is not None:
        s.find_element(By.ID,'name').send_keys('18860828409')   #输入账号密码
    if password is not None:
        s.find_element(By.ID,'pwd').send_keys(',')

    s.find_element(By.CSS_Selector,'.login_pwd_box[button="checkInput();"]').click()   #点击登录按钮
    sleep(2)
