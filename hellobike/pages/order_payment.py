# -*- coding: utf-8 -*-
# @Time    : 2020/10/29 7:47 下午
# @Author  : wenqinzhu
# @File    : order_payment.py
# @Software : PyCharm


from utils.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MB

"""
订单待支付页
click_payment_btn       点击立即支付按钮

页面操作
judge_is_adv        判断当前页是否出现广告弹窗
"""


# 订单待支付页
class OrderPaymentPage(BasePage):

    # 点击待支付页的立即支付按钮
    def click_payment_btn(self):
        PAY_BTN = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.Button").textContains("立即支付")')
        self.click_ele(PAY_BTN)

    # 勾选搭售卡 - 点击选中骑行卡
    def get_order_page_text(self):
        SELECT_OPTION = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").text("骑行卡")')
        self.click_ele(SELECT_OPTION)

    # TODO 存在搭售卡调起收银台组件 - 多一个阻断弹窗
    """ 
    没有搭售
        点击-立即支付 - 调起收银台
    命中搭售卡
        未勾选 - 出现弹窗(继续支付/购买并支付)
        勾选 - 直接调起收银台
    """
    # 收银台 - 购买并支付
    def buy_and_payment(self):
        SELECT_OPTION = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").text("购买并支付")')
        self.click_ele(SELECT_OPTION)

    # 收银台 - 继续支付
    def continue_payment(self):
        SELECT_OPTION = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.View").text("继续支付")')
        self.click_ele(SELECT_OPTION)

    # 调起收银台，选择支付方式
    def payment_way(self, flag):
        SELECT_OPTION1 = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("余额")')
        SELECT_OPTION2 = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.widget.TextView").text("支付宝")')
        if flag == "余额":
            self.click_ele(SELECT_OPTION1)
        elif flag == "支付宝":
            self.click_ele(SELECT_OPTION2)

    # 点击收银台组件中的去支付按钮
    def to_payment(self):
        SELECT_OPTION = (MB.ID, "com.jingyao.easybike:id/pay_btn")
        self.click_ele(SELECT_OPTION)
