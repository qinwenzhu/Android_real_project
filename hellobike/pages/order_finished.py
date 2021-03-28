# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 9:10 下午
# @Author  : wenqinzhu
# @File    : order_finished.py
# @Software : PyCharm

from utils.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MB

"""
订单完成页
close_bounced       关闭广告弹窗
open_adver          进入广告详情

页面操作
judge_is_adv        判断当前页是否出现广告弹窗
"""


# 订单完成页面
class OrderFinishedPage(BasePage):

    # 获取订单完成页文案
    def get_order_page_text(self):
        # containsText()
        PAGE_TEXT = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").textContains("已支付")')
        return self.get_text(PAGE_TEXT)
#       className()      textContains()
