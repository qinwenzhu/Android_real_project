# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 10:31 上午
# @Author  : wenqinzhu
# @File    : common_page_operation.py
# @Software : PyCharm


from time import sleep
from appium.webdriver.common.mobileby import MobileBy as MB
from utils.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

"""
页面共用操作
get_page_title      获取页面标题

页面操作

"""


# 获得页面标题
def get_page_title(self):
    # 定位页面标题
    PAGE_TIL = (MB.ID, "com.jingyao.easybike:id/title")
    return self.get_text(PAGE_TIL)
