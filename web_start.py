# -*- coding: utf-8 -*-
# @Time    : 2021/2/7 11:34 上午
# @Author  : wenqinzhu
# @File    : web_start.py
# @Software : PyCharm


from time import sleep
from selenium import webdriver
from hellobike_web.pages.login_page import LoginPage
from hellobike_web.pages.admin_system.config_management.forbid_area import AdminForbidArea
from hellobike_web.pages.admin_system.config_management.admin_public import AdminLeftNav
from hellobike_web.datas import web_datas as LD


driver = webdriver.Chrome()
driver.maximize_window()

# 城市后台配置管理系统
driver.get("http://uat-admin.hellobike.cn")
LoginPage(driver).web_login(LD.login_info["email"])

# 后台配置单车禁停区配置
a = AdminLeftNav(driver)
a.first_nav_title("配置管理")
a.two_nav_title("单车禁停区配置")
b = AdminForbidArea(driver)
b.forbid_confirm_city("上海")
b.view_or_edit_designates_city()
b.open_or_close_forbid("开启")
