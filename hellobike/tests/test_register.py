# -*- coding: utf-8 -*-
# @Time    : 2021/1/27 3:06 下午
# @Author  : wenqinzhu
# @File    : test_register.py
# @Software : PyCharm


import pytest
import random
import logging
from hellobike.pages.page_nav import NavPage
from hellobike.pages.page_personal import PersonalPage
from hellobike.pages.page_register import RegisterPage


class TestRegister:

    pytestmark = pytest.mark.register

    # @pytest.mark.usefixtures("logout_from_personal")
    # def test_success_register(self, register_account):
    #     NavPage(register_account[0]).nav_my()
    #     # 个人信息页：注册和断言
    #     personal_p = PersonalPage(register_account[0])
    #     personal_p.personal_handle_operation()
    #     assert "未认证" in personal_p.personal_get_unauthorized_text()

    def test_real_name_authentication(self, register_account, real_name_data):
        """
        个人信息页 - 点击:未实名认证 进行页面跳转
        对该用户进行虚拟身份证认证
        :return:
        """
        NavPage(register_account[0]).nav_my()
        p = PersonalPage(register_account[0])
        p.personal_click_user_img()
        p.personal_set_security_code()

        p.personal_per_unauthorized()

        # PersonalPage(register_account[0]).personal_per_unauthorized()
        RegisterPage(register_account[0]).register_real_name_handle_certification(real_name_data)
        assert "审核中" in RegisterPage(register_account[0]).register_get_real_text()
