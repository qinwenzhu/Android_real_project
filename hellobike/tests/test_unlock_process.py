# -*- coding: utf-8 -*-
# @Time    : 2020/10/30 3:04 下午
# @Author  : wenqinzhu
# @File    : test_pre.py
# @Software : PyCharm

import pytest
from time import sleep
from hellobike.pages.page_app_index import AppIndexPage
from hellobike.pages.page_scan_code import ScanCodePage
from hellobike.pages.page_confirm_unlock import ConfirmUnlockPage
from hellobike.pages.page_cycling import CyclingPage
from hellobike.datas import bike_number as BIKENO

"""
uat_simulator  模拟器车辆
uat_really   uat真锁
"""


# @pytest.mark.uat
# # @pytest.mark.usefixtures("uat_lock_bike")
# @pytest.mark.parametrize("data", BIKENO.uat_really)
# def test_uat_unlock_normal_for_app(uat_unlock_data, data):
#     AppIndexPage(uat_unlock_data).app_scan_the_code()
#     ScanCodePage(uat_unlock_data).scan_handle_unlock(data)
#     ConfirmUnlockPage(uat_unlock_data).confirm_click_confirm_btn()
#     sleep(2)
#     assert "骑行中" in CyclingPage(uat_unlock_data).cycling_get_page_title()


@pytest.mark.uat
@pytest.mark.parametrize("data", BIKENO.uat_really_normal)
def test_uat_real_normal_for_app(scenario_start_app, data):
    AppIndexPage(scenario_start_app).app_scan_the_code()
    ScanCodePage(scenario_start_app).scan_handle_unlock(data)
    ConfirmUnlockPage(scenario_start_app).confirm_click_confirm_btn()
    sleep(2)
    assert "骑行中" in CyclingPage(scenario_start_app).cycling_get_page_title()


@pytest.mark.uat
@pytest.mark.usefixtures("lock_manhd")
@pytest.mark.parametrize("data", BIKENO.uat_really_manhd)
def test_uat_real_manhd_for_app(scenario_start_app, data):
    _unlock_bike(scenario_start_app, data["bike_no"])
    assert _judge_unlock_success


class TestPreAuto:

    pytestmark = pytest.mark.pre_auto_lock

    @pytest.mark.usefixtures("auto_lock_normal")
    @pytest.mark.parametrize("data", BIKENO.pre_locks_normal)
    def test_pre_unlock_normal_for_app(self, scenario_start_app, data):
        _unlock_bike(scenario_start_app, data["bike_no"])
        sleep(2)
        assert _judge_unlock_success

    @pytest.mark.usefixtures("auto_lock_manhd")
    @pytest.mark.parametrize("data", BIKENO.pre_locks_manhd)
    def test_pre_unlock_manhd_for_app(self, scenario_start_app, data):
        _unlock_bike(scenario_start_app, data["bike_no"])
        sleep(2)
        assert _judge_unlock_success

    @pytest.mark.usefixtures("auto_lock_univercity")
    @pytest.mark.parametrize("data", BIKENO.pre_locks_university)
    def test_pre_unlock_university_for_app(self, scenario_start_app, data):
        _unlock_bike(scenario_start_app, data["bike_no"])
        sleep(2)
        assert _judge_unlock_success


# 开锁动作
def _unlock_bike(driver, bike_no):
    AppIndexPage(driver).app_scan_the_code()
    ScanCodePage(driver).scan_handle_unlock(bike_no)
    ConfirmUnlockPage(driver).confirm_click_confirm_btn()


# 校验是否开锁成功
def _judge_unlock_success(driver):
    result = CyclingPage(driver).cycling_get_page_title()
    if "骑行中" in result:
        return True
    else:
        return False
