# -*- coding: utf-8 -*-
# @Time    : 2021/2/3 7:52 下午
# @Author  : wenqinzhu
# @File    : page_confirm_unlock.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB
from utils.basepage import BasePage
from hellobike.pages.locations import loc_confirm_unlock as LCU


# 骑行流程：确认开锁页
class ConfirmUnlockPage(BasePage):

    # 点击"确认开锁"按钮
    def confirm_click_confirm_btn(self):
        self.click_ele((MB.ID, LCU.CONFIRM_CONFIRM_BTN))

    # 点击"继续开锁"按钮
    def confirm_the_lock(self):
        self.click_ele(((MB.ID, LCU.CONTINUE_UNLOCK)))
