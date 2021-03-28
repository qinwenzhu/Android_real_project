# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 5:01 下午
# @Author  : wenqinzhu
# @File    : page_nav.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage
from hellobike.pages.locations import loc_common as LC


# app底部导航
class NavPage(BasePage):

    # 底部导航 - 首页-跳转app首页
    def nav_index(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LC.NAV_INDEX))

    # 底部导航 - 车主-跳转顺风车首页
    def nav_post(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LC.NAV_CAR))

    # 底部导航 - 驿站-跳转帖子首页
    def nav_wallet(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LC.NAV_POST))

    # 底部导航 - 钱包-跳转钱包页
    def nav_life(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LC.NAV_WALLET))

    # 底部导航 - 我的-跳转个人信息页
    def nav_my(self):
        self.click_ele((MB.ANDROID_UIAUTOMATOR, LC.NAV_MY))
