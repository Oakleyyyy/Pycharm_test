"""
作者:lxy
日期:2022年04月28日
"""
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

#
# #启动浏览器驱动,创建webDriver实例对象
# s = webdriver.Chrome()
#
# # WebDriver 实例对象的get方法 可以让浏览器打开指定网址
# s.get('https://www.baidu.com/more/')
#
# #浏览器返回webelement对象 控制定位元素
# element = s.find_elements(By.TAG_NAME,'span')
# # element = s.find_element(By.ID,'su').click()
# for elements in element:
#     print(elements.text)
# pass
wd = webdriver.Chrome()


wd.get('https://home.qyjmed.com/login')
s1 = wd.find_element(By.ID,'name').send_keys('18860828409')
s2 = wd.find_element(By.ID,'pwd').send_keys(',')





