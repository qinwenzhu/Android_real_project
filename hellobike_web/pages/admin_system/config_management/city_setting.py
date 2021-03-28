# -*- coding: utf-8 -*-
# @Time    : 2021/3/9 7:44 下午
# @Author  : wenqinzhu
# @File    : city_setting.py
# @Software : PyCharm


# from utils.basepage import BasePage
# from selenium.webdriver.common.by import By
#
#
# # 客服管理后台 - 配置管理 - 单车禁停区(内部页面操作)
# class AdminForbidArea(BasePage):
#
#     # 设置禁停区作用的城市配置，如：上海
#     def forbid_confirm_city(self, city):
#         """ 输入操作城市，选择，搜索相关配置 """
#         self.click_ele((By.XPATH, '//span[contains(text(),  "去旧版")]'))
#         self.click_ele((By.XPATH, '//div[contains(@ng-disabled, "vm.disabled")]'))
#         self.update_input_text((By.XPATH, '//input[contains(@placeholder, "搜索城市名称")]'), city)
#         self.click_ele((By.XPATH, '//span[@class="ui-select-choices-row-inner"]'))
#         self.click_ele((By.XPATH, '//i[contains(@class, "fa-search")]//parent::button'))
#
#     # 操作指定城市的禁停区配置，如：上海
#     def edit_designates_city(self):
#         """ 编辑 """
#         pass
