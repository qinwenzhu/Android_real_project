# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 9:20 下午
# @Author  : wenqinzhu
# @File    : scan_code.py
# @Software : PyCharm

import os
from appium.webdriver.common.mobileby import MobileBy as MB
from utils.basepage import BasePage
from hellobike.pages.locations import loc_scan as LC


# 输入车辆编号开锁流程
class ScanCodePage(BasePage):

    # 扫码 - 点击输入车辆编号
    def scan_click_number_btn(self):
        self.click_ele((MB.ID, LC.SCAN_INPUT))

    # 扫码 - 获取输入车辆编号文本
    def scan_get_scan_text(self):
        return self.get_text((MB.ID, LC.SCAN_TEXI))

    # 扫码 - 输入车辆编号并开锁
    def scan_input_bike_number(self, bike_no):
        """
        :param bike_no: 车辆编号
        """
        self.click_ele((MB.ID, LC.SCAN_NO))
        """ 存在的问题：输入车辆编号页面存在动态交互，模拟手机键盘的输入，才会动态出现开锁按钮
         使用adb命令 - 输入指定的字符串   --- adb shell input text 9170014703
         """
        adb = 'adb shell input text %s' % bike_no
        os.system(adb)
        self.click_ele((MB.ID, LC.SCAN_UNLOCK))

    def scan_handle_unlock(self, bike_no):
        self.scan_click_number_btn()
        self.scan_input_bike_number(bike_no)

    # # 首次使用，需要对弹框 - 申请相机权限 - 进行授权
    # def is_authorization_camera(self):
    #     # 定位-申请相机权限- 中的确定
    #     CAMERA_BTN = (MB.ID, "com.jingyao.easybike:id/okView")
    #     # 定位-申请允许权限
    #     ALLOW_BTN = (MB.ID, "com.android.packageinstaller:id/permission_allow_button")
    #     ele = self.get_ele_locator(CAMERA_BTN)
    #     if ele.is_displayed():
    #         self.click_ele(CAMERA_BTN)
    #         ele = self.get_ele_locator(ALLOW_BTN)
    #         # 如果元素可见，点击允许按钮
    #         if ele.is_displayed():
    #             self.click_ele(ALLOW_BTN)
    #
    # # 输入车辆编号进行扫码开锁
    # def scan_code_lock(self, bike_code):
    #     # 点击-车辆编号-按钮
    #     self.click_number_btn()
    #     # 输入车辆编号
    #     self.input_bike_number(bike_code)
    #     # 点击开锁

    # 弹框 - 需要使用相机权限 -禁止/始终允许
    # com.android.packageinstaller:id/permission_allow_button    始终允许
    # com.android.packageinstaller:id/permission_deny_button     禁止
    # com.android.packageinstaller:id/do_not_ask_checkbox        禁止后不再询问

    # # 判断页面是否存在 - "输入编号" - 文本
    # def judge_scan_text(self):
    #     # 定位-输入编号
    #     NUMBER_BTN = (MB.ID, "com.jingyao.easybike:id/input_code_tv")
    #     con_text = self.get_text(NUMBER_BTN)
    #     if con_text == "输入编号":
    #         return True
    #     else:
    #         return False
