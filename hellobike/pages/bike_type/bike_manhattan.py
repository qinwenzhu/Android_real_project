# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 7:40 下午
# @Author  : wenqinzhu
# @File    : bike_manhattan.py
# @Software : PyCharm

import logging
from time import sleep
from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage

"""
车辆类型之曼哈顿特殊前端页面操作
enter_login           点击立即登录，进入登录页 

页面操作
get_user_login_status   通过首页的文本 - 判断当前用户是否已经登陆app
"""


# 不同车型的不同前端操作
class BikeTypePage(BasePage):

    # 确认开锁页 - 曼哈顿车型 - 继续开锁
    def confirm_the_lock(self):
        # 定位 - 继续开锁 - 按钮
        RETURN_BTN = (MB.ID, "com.jingyao.easybike:id/knowTv")
        self.click_ele(RETURN_BTN)

    # 骑行中页面 - 曼哈顿车型 - 我要还车
    def cyc_return_car(self):
        # 定位 - 我要还车 - 按钮
        RETURN_BTN = (MB.ID, "com.jingyao.easybike:id/tv_return_bike")
        self.click_ele(RETURN_BTN)

    # 骑行中页面 - 曼哈顿车型 - 确认还车
    def confirm_the_car(self):
        # 定位 - 我要还车 - 按钮
        RETURN_BTN = (MB.ID, "com.jingyao.easybike:id/backTv")
        self.click_ele(RETURN_BTN)


