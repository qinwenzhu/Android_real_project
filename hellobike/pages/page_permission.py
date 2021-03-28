# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 7:36 下午
# @Author  : wenqinzhu
# @File    : page_permission.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB

from utils.basepage import BasePage
from hellobike.pages.locations import loc_phone_permissions as LPP


# 公共 - 手机权限相关操作
class PermissionPage(BasePage):

    # 权限 - OPPO手机-勾选同意相关协议
    def pre_checked_agree(self):
        self.click_ele((MB.ID, LPP.PER_APP1))

    # 权限 - OPPO手机-同意并开启服务
    def pre_click_btn(self):
        self.click_ele((MB.ID, LPP.PER_APP2))

    # 权限 - OPPO手机-弹窗权限 -确定/取消
    def pre_agree_permission(self, default="confirm"):
        if default == "confirm":
            self.click_ele((MB.XPATH, LPP.PER_APP3))
        else:
            self.click_ele((MB.XPATH, LPP.PER_APP4))

    # 权限 - 消息通知弹窗 - 去开启/取消
    def pre_cancel_info_notice(self, default="cancel"):
        # 默认点击取消
        if default == "cancel":
            self.click_ele((MB.ANDROID_UIAUTOMATOR, LPP.PRE_APP6))
        else:
            self.click_ele((MB.ANDROID_UIAUTOMATOR, LPP.PRE_APP5))

    # 权限 - OPPO手机的相机权限
    def per_camera(self):
        self.click_ele((MB.ID, LPP.PER_CAMERA1))
        self.click_ele((MB.XPATH, LPP.PER_CAMERA2))

    # 首次打开app针对手机授权
    def per_first_authorization_for_OPPO(self):
        self.pre_checked_agree()
        self.pre_click_btn()
        self.pre_agree_permission()
        # self.pre_cancel_info_notice()
