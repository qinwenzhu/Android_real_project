# -*- coding: utf-8 -*-
# @Time    : 2021/2/4 7:58 下午
# @Author  : wenqinzhu
# @File    : connection_simulator.py
# @Software : PyCharm

from utils.basepage import BasePage
from selenium.webdriver.common.by import By


# 模拟器操作
class ConnectionPage(BasePage):

    # 关闭浮层
    def close_alert(self):
        self.click_ele((By.XPATH, '//div[@class="el-dialog__header"]//button'))

    # 选择App环境 - 输入 fat / uat
    def select_env(self, env):
        self.update_input_text((By.XPATH, '//label[contains(text(), "APP环境")]//following-sibling::div//input'), env)

    # 通过指定车辆进行模拟器连接
    def con_specified_bike(self, bike_no):
        self.update_input_text((By.XPATH, '//span[contains(text(), "车辆编号")]//parent::span//following-sibling::div//input'), bike_no)

    # 获取可用车辆
    def get_available(self):
        self.click_ele((By.XPATH, '//button//span[contains(text(), "获取可用车辆")]'))

    # 连接 / 断开连接
    def connect_btn(self, default="conn"):
        # CONN = (By.XPATH, '//section[@class="app-main"]//button//span[contains(text(), "连接")]')
        CONN = (By.XPATH, '//button//span[contains(text(), "连接")]')
        # UN_CONN = (By.XPATH, '//section[@class="app-main"]//button//span[contains(text(), "断开连接")]')
        UN_CONN = (By.XPATH, '//button//span[contains(text(), "断开连接")]')
        if default == "conn":
            self.click_ele(CONN)
        else:
            self.click_ele(UN_CONN)

    # 车辆关锁
    def lock_bike(self):
        self.click_ele((By.XPATH, '//button//span[contains(text(), "关锁")]'))

    # 输入经纬度
    def input_lon_and_lat(self, lon, lat):
        self.update_input_text((By.XPATH, '//label[contains(text(), "经度")]//following-sibling::div//input'), lon)
        self.update_input_text((By.XPATH, '//label[contains(text(), "纬度")]//following-sibling::div//input'), lat)

    # 位置补报
    def position_again(self):
        self.click_ele((By.XPATH, '//button//span[contains(text(), "位置补报")]'))

    # 上报位置
    def position_report(self):
        self.click_ele((By.XPATH, '//button//span[contains(text(), "上报位置")]'))

    # 不同环境 - 模拟器连接 + 获取随机可用车辆
    def handle_sim_con_bike(self, env="uat"):
        self.select_env(env)
        self.get_available()

    # 不同环境 - 模拟器连接 + 连接指定车辆
    def handle_spe_con_bike(self, bike_no, env="uat"):
        self.select_env(env)
        self.con_specified_bike(bike_no)


if __name__ == '__main__':
    from selenium import webdriver
    driver = webdriver.Chrome()
    # driver.maximize_window()
    driver.get("http://carfee-utils.hellobike.cn/#/simulator/?token=22801aacbe0cc1c51932590c691bdea3")
    ConnectionPage(driver).handle_sim_con_bike()
