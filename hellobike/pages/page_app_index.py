# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 2:26 下午
# @Author  : wenqinzhu
# @File    : page_app_index.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB
from utils.basepage import BasePage
from hellobike.pages.locations import loc_app_index as LAI


# 平台首页
class AppIndexPage(BasePage):

    # 平台首页-点击"扫一扫"按钮
    def app_scan_the_code(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LAI.APP_SCAN))

    # 平台首页-点击"单车icon"-跳转到单车首页
    def app_enter_bike(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LAI.APP_BIKE))

    # 平台首页-顶部"消息" - 获取文本
    def app_get_info(self):
        return self.get_text((MB.ID, LAI.APP_INFO))
