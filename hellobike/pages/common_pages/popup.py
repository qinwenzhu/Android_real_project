# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 9:06 下午
# @Author  : wenqinzhu
# @File    : popup.py
# @Software : PyCharm

import logging
from time import sleep
import re
from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage


# 弹窗
class PopPage(BasePage):

    # 个人信息页面 - 安全密码弹窗
    def personal_safe_pop(self):
        POP_LOC = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("忽略").className("android.widget.Button")')
        self.click_ele(POP_LOC)

    # 确认开锁页面 - 干预公告弹窗
    def intervention_pop(self):
        POP_LOC = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("忽略").className("android.widget.Button")')
        self.click_ele(POP_LOC)

    # 单车首页-连续包月续费失败弹窗
    def i_know_pop(self):
        # 查看详情元素定位
        DETAIL_LOC = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("知道了").className("android.widget.Button")')
        self.click_ele(DETAIL_LOC)

    # 单车首页-任务体系弹窗
    def task_pop(self):
        # 查看详情元素定位
        DETAIL_LOC = (MB.ID, "com.jingyao.easybike:id/b_submit")
        self.click_ele(DETAIL_LOC)

        # 获取任务弹窗是页面尺寸
        POP_LOC = (MB.ID, "android:id/content")
        # 获取当前弹窗的整体尺寸
        # self.getPage()
        # 点击关闭按钮
        # POP_LOC = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("忽略").className("android.widget.Button")')
        # self.click_ele(POP_LOC)
