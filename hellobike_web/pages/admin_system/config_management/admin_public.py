# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 7:04 下午
# @Author  : wenqinzhu
# @File    : admin_public.py
# @Software : PyCharm


from utils.basepage import BasePage
from selenium.webdriver.common.by import By


# 公共部分 - 客服管理后台 - 左侧导航
class AdminLeftNav(BasePage):

    # nav：一级标题
    def first_nav_title(self, til_name):
        """
        admin后台管理系统
        :param til_name: 一级标题 - 如：配置管理
        :return:
        """
        self.click_ele((By.XPATH, f'//div[@class="item-body"]//i[contains(@class, "fa-cogs")]//following-sibling::p[contains(text(),"{til_name}")]'))

    # nav：二级标题
    def two_nav_title(self, til_name):
        """
        admin后台管理系统
        :param til_name: 二级标题 - 如：单车禁停区配置
        :return:
        """
        self.click_ele((By.XPATH, f'//div[contains(@class, "active")]//p[contains(text(), "{til_name}")]//parent::a'))
