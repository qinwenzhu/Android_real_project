# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 7:01 下午
# @Author  : wenqinzhu
# @File    : login_page.py
# @Software : PyCharm

import getpass
from utils.basepage import BasePage
from selenium.webdriver.common.by import By


class LoginPage(BasePage):

    # 登录操作
    def web_login(self, email):

        # 输入用户名
        self.update_input_text((By.CSS_SELECTOR, 'input[placeholder="邮箱"]'), email)
        # 输入密码
        """控制台密码加密处理   导入模块：getpass    调用方法：getpass.getpass()"""
        password = getpass.getpass("Password：")
        self.update_input_text((By.CSS_SELECTOR, 'input[placeholder="密码"]'), password)
        # 输入验证码
        code = input("Code：")
        # 输入验证码
        self.update_input_text((By.CSS_SELECTOR, 'input[placeholder="验证码"]'), code)
        # 输入动态口令
        dynamic_pwd = input("Dynamic：")
        self.update_input_text((By.CSS_SELECTOR, 'input[placeholder="二次认证动态口令"]'), dynamic_pwd)
        # 点击登录网站
        self.click_ele((By.XPATH, '//button[contains(text(), "登录")]'))
