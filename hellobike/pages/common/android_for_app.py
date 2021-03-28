# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 4:29 下午
# @Author  : wenqinzhu
# @File    : android_for_app.py
# @Software : PyCharm


from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage
from hellobike.pages.locations import loc_android_for_app as LAFA


# Android端app共用操作
class AndroidPage(BasePage):

    """Android - app左上角返回到上一页 "<" / "X"
    左上角返回"上一步"
    点击左上角"叉号"
    """
    def android_app_left_back(self):
        self.click_ele((MB.ID, LAFA.ANDROID_BACK))
