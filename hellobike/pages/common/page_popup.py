# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 7:32 下午
# @Author  : wenqinzhu
# @File    : page_popup.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage
from hellobike.pages.locations import loc_popup as LP


# 弹窗固定操作
class PopupPage(BasePage):

    # 弹窗操作 - 天降红包
    def popup_heave_red_envelope(self, default="receive"):
        if default == "receive":
            self.click_ele((MB.ID, LP.POPOP_LEAVE))
        else:
            self.click_ele((MB.ID, LP.POPUP_RECEIVE))

    # 弹窗操作 - 开启消息通知
    def popup_info_alerts(self, default="cancle"):
        if default == "cancle":
            self.click_ele((MB.ANDROID_UIAUTOMATOR, LP.POPOP_INFO_CANCLE))
        else:
            self.click_ele((MB.ANDROID_UIAUTOMATOR, LP.POPUP_INFO_GO))
