# -*- coding: utf-8 -*-
# @Time    : 2020/7/23 5:07 下午
# @Author  : wenqinzhu
# @File    : page_personal.py
# @Software : PyCharm

from appium.webdriver.common.mobileby import MobileBy as MB
from utils.basepage import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from hellobike.pages.locations import loc_personal as LP


# 个人信息页面
class PersonalPage(BasePage):

    # 点击当前登录用户的图标icon
    def personal_click_user_img(self):
        self.click_ele((MB.ID, LP.PERSONAL_ICON))

    # 点击点击设置icon
    def personal_enter_setting(self):
        self.click_ele((MB.ID, LP.PERSONAL_SETTING))

    # 点击右上角消息icon
    def personal_enter_message(self):
        self.click_ele((MB.ID, LP.PERSONAL_INFO))

    # 个人中心-退出登录
    def personal_logout(self):
        self.click_ele((MB.ID, LP.PERSONAL_LOGINOUT))

    # 个人中心 - 点击未认证
    def personal_per_unauthorized(self):
        self.click_ele((MB.ID, LP.PERSONAL_REALNAME_STATUS))

    # 个人中心 - 实名认证：获取实名认证状态文本
    def personal_get_unauthorized_text(self):
        return self.get_text((MB.ID, LP.PERSONAL_REALNAME_STATUS))

    # 个人中心 - 弹窗：设置安全密码提示弹窗
    def personal_set_security_code(self, default="ignore"):
        if default == "ignore":
            self.click_ele((MB.ANDROID_UIAUTOMATOR, LP.PERSONAL_BTN_IGNORE))
        else:
            self.click_ele((MB.ANDROID_UIAUTOMATOR, LP.PERSONAL_BTN_GO))

    # 个人中心(设置页) - 弹窗：确定退出登录
    def personal_popup_logout(self, default="confirm"):
        if default == "confirm":
            self.click_ele((MB.ID, LP.PERSONAL_LOGINOUT_AGREE))
        else:
            self.click_ele((MB.ID, LP.PERSONAL_LOGINOUT_CANCLE))

    # 个人信息页登录状态查看
    def personal_handle_operation(self):
        """ 进入个人信息页面 点击当前登录用户的icon  点击安全密码提示  查看当前用户的登录状态 """
        self.personal_click_user_img()
        self.personal_set_security_code()

    # check用户登录状态
    def personal_status(self):
        # 如果用户图标元素存在，则已登录
        if self.check_ele_exists((MB.ID, LP.PERSONAL_ICON)) is True:
            return True



    # # 点击我的订单 --- 进入订单列表页
    # def enter_my_order(self):
    #     # 定位我的按钮
    #     MY_BTN = (MB.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.jingyao.easybike:id/tv_tab_text").text("我的")')
    #     self.click_ele(MY_BTN)
    #
    # # 弹框操作
    # def bounced_operation(self, flag=True):
    #     # 确定按钮
    #     COMMIT_BTN = (MB.ID, "com.jingyao.easybike:id/confirm_btn")
    #     # 取消按钮
    #     CANCLE_BTN = (MB.ID, "com.jingyao.easybike:id/cancel_btn")
    #     if flag is True:
    #         self.click_ele(COMMIT_BTN)
    #     else:
    #         self.click_ele(CANCLE_BTN)
    #
    # # 从个人信息页的图标到个人页到点击实名操作链接跳转
    # def opera_account(self):
    #     self.click_user_img()
    #     pass
    #
    # # 判断用户是否登录成功
    # def judge_login_success(self):
    #     # 用户信息界面 - 查看到登录用户元素存在，则说明用户登录成功
    #     USER_INFO = (MB.ID, "com.jingyao.easybike:id/ll_user_info")
    #     try:
    #         # 如果登录操作执行之后还存在目标元素定位 --  则断言登录失败
    #         WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(USER_INFO))
    #         return True
    #     except:
    #         return False
