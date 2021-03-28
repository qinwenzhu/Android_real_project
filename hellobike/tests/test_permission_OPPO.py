# -*- coding: utf-8 -*-
# @Time    : 2020/10/18 9:20 下午
# @Author  : wenqinzhu
# @File    : test_Initialization_OPPO.py
# @Software : PyCharm

import pytest
from hellobike.pages.page_app_index import AppIndexPage
from hellobike.pages.page_scan_code import ScanCodePage
from hellobike.pages.common.page_popup import PopupPage
from hellobike.pages.page_permission import PermissionPage


class TestFirstOppo:

    pytestmark = pytest.mark.first

    def test_authorization_app(self, init_app):
        """
        OPPO手机首次打开app授权操作
        :param init_app: 启动服务
        :return:
        """
        PermissionPage(init_app).per_first_authorization_for_OPPO()
        # PopupPage(init_app).popup_info_alerts()   # 测试平台首页-开启消息弹窗
        # 断言：自动设置好OPPO手机打开app的系统权限授权
        assert "消息" in AppIndexPage(init_app).app_get_info()

    @pytest.mark.usefixtures("login_from_app_index", "logout_from_scan")
    def test_authorization_camera(self, start_app):
        """ OPPO手机首次使用相机功能的授权操作
        登录之后通过扫码给手机相机授权  点击app首页扫一扫按钮  给相机授权
        """
        AppIndexPage(start_app).app_scan_the_code()
        PermissionPage(start_app).per_camera()
        # 断言：页面文本信息-输入编号
        assert "输入编号" in ScanCodePage(start_app).scan_get_scan_text()
