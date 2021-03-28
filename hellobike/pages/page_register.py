# -*- coding: utf-8 -*-
# @Time    : 2020/10/22 4:00 下午
# @Author  : wenqinzhu
# @File    : real_name_operation.py
# @Software : PyCharm


from time import sleep
from utils.basepage import BasePage
from appium.webdriver.common.mobileby import MobileBy as MB
from appium.webdriver.common.touch_action import TouchAction
from hellobike.pages.locations import loc_register as LR
from hellobike.pages.locations import loc_phone_permissions as LPP
from hellobike.pages.classess.user_info import UserInfo


# 注册 - 实名认证操作
class RegisterPage(BasePage):

    # 实名认证 - 选择身份证认证
    def register_real_choose_identity_cer(self):
        self.click_ele((MB.ID, LR.REAL_ID))

    # 实名认证 - 点击这里
    def register_real_click_here(self):
        self.click_ele((MB.ID, LR.REAL_CLICK_HERE))

    # 国外身份认证页面操作
    def register_real_foreign_identity_authentication(self, name, id, national):
        # 定义UserInfo的三个属性
        self.update_input_text((MB.ID, LR.REAL_NAME), name)
        self.update_input_text((MB.ID, LR.REAL_CERTIFICATE), id)
        self.update_input_text((MB.ID, LR.REAL_ADDRESS), national)
        self.click_ele((MB.ID, LR.REAL_NEXT))

    # 上次图片 - 封装 - 身份证正反面-操作相同-进行方法封装
    def upload_img(self):
        """
        通过 content-desc 定位手机中的相册
        1、创建 TouchAction 对象
        2、通过 - tap()方法点击手机中的相册
        3、tap() - 相同的方法选中当前相册中的图片
        """
        # 选中相册 - 进入相册选中照片
        # self.click_ele((MB.ACCESSIBILITY_ID, "相册"))     # 定位 content-desc
        self.click_ele((MB.XPATH, LPP.SELECT_CAMERA))
        sleep(2)
        # 创建 TouchAction对象
        # 通过tap()，设置坐标位置进行点击。通过perform() 和 release() 使tap()操作生效
        # 选择相册
        TouchAction(self.driver).wait(1).tap(x=270, y=290).wait(3).perform().wait(1).release()
        sleep(3)
        # 选择图片
        TouchAction(self.driver).wait(1).tap(x=200, y=300).wait(3).perform().wait(1).release()
        sleep(1)
        self.click_ele((MB.ID, LR.REAL_UPLOAD))

    # 上传证件照
    def register_real_upload_profile_picture(self):
        # 身份证正面上传
        self.click_ele((MB.ID, LR.REAL_CLICK_IMG1))
        # 手机app选择相册选择图片操作
        self.upload_img()
        # 身份证反面上传
        self.click_ele((MB.ID, LR.REAL_CLICK_IMG2))
        self.upload_img()
        # TODO 等待当前操作完成
        self.driver.wait_activity(self.driver.current_activity, 10)
        sleep(2)
        # 点击认证
        self.click_ele((MB.ID, LR.REAL_CERTIFICATE_BTN))

    # 获取实名认证流程后的跳转文本：审核中
    def register_get_real_text(self):
        return self.get_text((MB.ID, LR.REAL_REVIEW))

    # 实名认证 - 通过身份证认证方式
    def register_real_name_handle_certification(self, user_info):
        # 实名认证页面 - 选择身份证认证
        self.register_real_choose_identity_cer()
        # "点击这里" - 按钮 - 进行页面跳转到国外身份证注册操作页
        self.register_real_click_here()
        # 测试虚拟身份证 - 实名认证 - 下一步进行页面跳转
        if isinstance(user_info, UserInfo):
            self.register_real_foreign_identity_authentication(user_info.name, user_info.cer_id, user_info.national)
        # 身份证 - 照片上传页面 - 点击认证按钮，实名操作完成
        self.register_real_upload_profile_picture()
