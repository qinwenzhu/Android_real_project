# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 9:37 下午
# @Author  : wenqinzhu
# @File    : test_login.py
# @Software : PyCharm

import pytest
from hellobike.pages.page_login import LoginPage
from hellobike.pages.common.page_popup import PopupPage
from hellobike.pages.page_app_index import AppIndexPage
from hellobike.pages.page_nav import NavPage
from hellobike.datas import common_data as CD


@pytest.mark.login
@pytest.mark.usefixtures("logout_from_app_index")
def test_success_login(start_app):
    # 登录app
    NavPage(start_app).nav_my()
    LoginPage(start_app).login_handle_operation(CD.user_phone)
    # PopupPage(start_app).popup_heave_red_envelope()     # 测试平台首页-天降红包弹窗
    assert "消息" in AppIndexPage(start_app).app_get_info()
