# -*- coding: utf-8 -*-
# @Time    : 2020/10/16 7:24 下午
# @Author  : wenqinzhu
# @File    : get_verification_code.py
# @Software : PyCharm

import logging
from time import sleep
import re
from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage


# 封装实时获取线上环境登录app的短信验证码
class GetVerificationPage(BasePage):

    # 获取最新的短信验证码
    def get_ver_code(self):
        """
        # textMatches(String regex)   --- 正则表达式-匹配符合规则的文本
        # textContains(String text)   --- 包含文本
        :return:
        """
        # android.widget.TextView
        # text     验证码：3396，请勿泄露，点击查看详情。    --- 正则表达式获取数字
        CODE_TEXT = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().textContains("验证码").className("android.widget.TextView")')
        pattern = self.get_text(CODE_TEXT)
        print(pattern)
        # code_text = re.match('^\d{4}$', pattern)
        # print(code_text.group())
        # return code_text.group()

    # 清空通知栏信息
    def clear_notification_bar(self):
        NOT_BTN = (MB.ID, "com.android.systemui:id/im_clear_all")
        self.click_ele(NOT_BTN)

    # 下拉通知栏
    def drop_down_notification_bar(self):
        # 登录短信成功接收
        sleep(10)
        # 调用封装方法 - 向下滑动手机到通知栏可见
        self.swipe_operation(0.5, 0.25, 0.5, 0.9, 200)

    # 上拉通知栏
    def on_pull_notification_bar(self):
        self.swipe_operation(0.5, 0.9, 0.5, 0.1, 200)
