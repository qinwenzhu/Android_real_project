# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:42 下午
# @Author  : wenqinzhu
# @File    : page_login.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage
from hellobike.pages.locations import loc_login as LL


# 登录操作
class LoginPage(BasePage):

    # 登录页 - 输入手机号操作
    def login_input_mobile_phone(self, phone_no):
        self.update_input_text((MB.ID, LL.LOGIN_PHONE), phone_no)
        self.click_ele((MB.ID, LL.LOGIN_AGREE))
        self.click_ele((MB.ID, LL.LOGIN_START))

    # 验证码页 - 输入验证码
    def login_get_mobile_verification_code(self, param: list = None):
        # 测试环境-万能验证码(1234)
        if param is None:
            param = [1, 2, 3, 4]
        else:
            # TODO 实时获取线上验证码
            param = ""
        self.update_input_text((MB.ID, LL.CODE_N1), param[0])
        self.update_input_text((MB.ID, LL.CODE_N2), param[1])
        self.update_input_text((MB.ID, LL.CODE_N3), param[2])
        self.update_input_text((MB.ID, LL.CODE_N4), param[3])

    # 登录操作
    def login_handle_operation(self, phone_no, ver_code=None):
        self.login_input_mobile_phone(phone_no)
        self.login_get_mobile_verification_code(ver_code)

    # check用户是否已登录
    def login_title(self):
        # 如果存在要查找的元素信息，则需要进行登录
        if self.check_ele_exists((MB.ANDROID_UIAUTOMATOR, LL.LOGIN_TITLE)) is True:
            return self.get_text((MB.ANDROID_UIAUTOMATOR, LL.LOGIN_TITLE))
