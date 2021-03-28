# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 2:33 下午
# @Author  : wenqinzhu
# @File    : forbid_area.py
# @Software : PyCharm

import logging
from utils.basepage import BasePage
from selenium.webdriver.common.by import By


# 客服管理后台 - 配置管理 - 单车禁停区(内部页面操作)
class AdminForbidArea(BasePage):

    # 配置禁停区城市，如：上海
    def forbid_confirm_city(self, city):
        """ 输入操作城市，选择，搜索相关配置 """
        self.click_ele((By.XPATH, '//div[@class="el-form-item__content"]//input'))
        self.update_input_text((By.XPATH, '//div[@class="el-form-item__content"]//input'), city)
        self.click_ele((By.XPATH, f'//span[contains(text(), "{city}")]//parent::li'))
        self.click_ele((By.XPATH, '//span[contains(text(), "搜索")]'))

    # 查看/编辑禁停区，如：上海
    def view_or_edit_designates_city(self, default="edit"):
        """ 编辑 """
        if default == "edit":
            self.click_ele((By.XPATH, '//span[contains(text(), "编辑")]'))
        else:
            self.click_ele((By.XPATH, '//span[contains(text(), "查看")]'))

    # 开启/关闭禁停区
    def open_or_close_forbid(self, flag, default="确认"):
        if flag == "开启":
            self.click_ele((By.XPATH, '//span[contains(text(), "是")]//parent::label[contains(@class, "el-radio")]'))
        elif flag == "关闭":
            self.click_ele((By.XPATH, '//span[contains(text(), "否")]//parent::label[contains(@class, "el-radio")]'))
        else:
            logging.info("输入错误，请确认开启还是关闭禁停区！")
        if default == "确认":
            self.click_ele((By.XPATH, '//div[@class="el-dialog__footer"]//span[contains(text(), "确")]'))
        else:
            self.click_ele((By.XPATH, '//div[@class="el-dialog__footer"]//span[contains(text(), "关")]'))
