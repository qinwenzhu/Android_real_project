# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 3:11 下午
# @Author  : wenqinzhu
# @File    : conftest.py.py
# @Software : PyCharm

import pytest
import random
import logging
from time import sleep
from appium import webdriver

from hellobike.pages.page_nav import NavPage
from hellobike.pages.page_login import LoginPage
from hellobike.pages.page_personal import PersonalPage
from hellobike.pages.classess.user_info import UserInfo
from hellobike.pages.common.android_for_app import AndroidPage
from hellobike.pages.page_cycling import CyclingPage
from hellobike.datas import common_data as CD
from hellobike.datas import bike_number as BIKENO
from utils.file_path import FilePath
from utils import adb_operation as ADB
from utils.handle_config import HandleConfig
from hellobike.api.api_simulator_connection import ApiSimConnect
from hellobike.api.auto_lock import lock_bike


# 启动app、检查登录状态
@pytest.fixture(scope="module")
def start_app_and_check_login():
    driver = _base_driver()
    # check登录状态
    _is_login(driver)
    yield driver
    _is_logout(driver)
    # driver.close_app()


# 重置app
@pytest.fixture
def init_app():
    # 启动参数 - noReset=False，默认重置手机缓存
    driver = _base_driver(noReset=False)
    yield driver
    driver.close_app()


# 启动app到平台首页
@pytest.fixture
def start_app():
    # 启动app
    driver = _base_driver()
    yield driver
    sleep(5)
    driver.close_app()


# 场景化启动
@pytest.fixture(scope="class")
def scenario_start_app():
    # 启动app
    driver = _base_driver()
    yield driver
    # driver.close_app()


# 后置 - 曼哈顿关锁
@pytest.fixture
def lock_manhd(scenario_start_app):
    yield scenario_start_app
    sleep(3)
    cyc = CyclingPage(scenario_start_app)
    if "骑行中" in cyc.cycling_get_page_title():
        # 点击我要还车
        CyclingPage(scenario_start_app).cycling_return_bike()
    else:
        print("曼哈顿开锁失败！")


# 后置 - pre环境 - 普通锁关锁
@pytest.fixture
def auto_lock_normal():
    yield
    sleep(2)
    lock_bike(num=1)


# 后置 - pre环境(进入骑行中，点击我要还车，通过锁具自动关锁 = 加调用接口：lock_bike) - 曼哈顿关锁
@pytest.fixture
def auto_lock_manhd(scenario_start_app):
    yield scenario_start_app
    sleep(2)
    cyc = CyclingPage(scenario_start_app)
    if "骑行中" in cyc.cycling_get_page_title():
        # 点击我要还车
        sleep(2)
        CyclingPage(scenario_start_app).cycling_return_bike()
        lock_bike(num=2)
    else:
        print("锁具上的曼哈顿开锁失败！")


# 后置 - pre环境 - 高校车-西子国际高校区
@pytest.fixture
def auto_lock_univercity(scenario_start_app):
    yield scenario_start_app
    sleep(2)
    cyc = CyclingPage(scenario_start_app)
    if "骑行中" in cyc.cycling_get_page_title():
        sleep(2)
        CyclingPage(scenario_start_app).cycling_return_bike()
        lock_bike(num=3)
    else:
        print("锁具上的高校曼哈顿开锁失败！")


# uat测试环境连接模拟器并开锁
@pytest.fixture
def uat_unlock_data(scenario_start_app):
    # 通过模拟器连接车辆
    ApiSimConnect(BIKENO.uat_simulator[0]).connect_sim()
    yield scenario_start_app


# uat测试环境关锁并断开模拟器
@pytest.fixture
def uat_lock_bike():
    yield
    sleep(3)
    api = ApiSimConnect(BIKENO.uat_simulator[0])
    # 关锁
    # api.close_lock()
    # 断开模拟器连接
    api.disconnect_sim()


# 实名认证测试数据
@pytest.fixture
def real_name_data():
    user_data = _random_str()
    user_info = UserInfo(name=user_data, cer_id=user_data,national=user_data)
    yield user_info


# 前置：从平台首页进行登录
@pytest.fixture
def login_from_app_index(start_app):
    sleep(1)
    _login_app(start_app)
    yield
def _login_app(driver):
    """从平台首页进行登录操作
    我的 调用封装的登录操作 登录成功会自动跳转到平台首页
    """
    NavPage(driver).nav_my()
    LoginPage(driver).login_handle_operation(CD.user_phone)


# 前置：生成随机手机号并注册app
@pytest.fixture(scope="class")
def register_account(scenario_start_app):
    sleep(1)
    new_phone = _register_account(scenario_start_app)
    yield scenario_start_app, new_phone
def _register_account(driver):
    """ 从平台首页进行注册操作 """
    new_phone = _create_phone()
    NavPage(driver).nav_my()
    LoginPage(driver).login_handle_operation(new_phone)
    return new_phone


# 后置：从扫码页退出登录
@pytest.fixture
def logout_from_scan(start_app):
    yield start_app
    sleep(2)
    _logout_scan(start_app)
def _logout_scan(driver):
    """Android端授权相机权限后进行退出登录操作
    点击扫码页叉号 导航点击"我的" 设置 退出登录   确认退出登录
    """
    personal_p = PersonalPage(driver)
    AndroidPage(driver).android_app_left_back()
    NavPage(driver).nav_my()
    personal_p.personal_enter_setting()
    personal_p.personal_logout()
    personal_p.personal_popup_logout()


# 后置：从个人信息页(个人信息展示页)退出登录
@pytest.fixture
def logout_from_personal(start_app):
    yield start_app
    sleep(2)
    _logout_personal(start_app)
def _logout_personal(driver):
    """ 从个人信息页面进行退出登录操作
    点击个人信息页左上角"返回上一页"  设置icon   退出登录   确认退出登录
    """
    personal_p = PersonalPage(driver)
    AndroidPage(driver).android_app_left_back()
    personal_p.personal_enter_settingg()
    personal_p.personal_logout()
    personal_p.personal_popup_logout()

# 后置：从平台首页退出登录
@pytest.fixture
def logout_from_app_index(start_app):
    yield start_app
    sleep(2)
    _logout_app_index(start_app)
def _logout_app_index(driver):
    """ app首页退出登录操作
    导航点击"我的" 设置 退出登录   确认退出登录
    """
    personal_p = PersonalPage(driver)
    NavPage(driver).nav_my()
    personal_p.personal_enter_settingg()
    personal_p.personal_logout()
    personal_p.personal_popup_logout()


# 数据
# 随机生成手机号
def _create_phone():
    phone_rules = ["185", "139", "186", "131"]
    # random.choice()的方法返回一个列表，元组或字符串的随机项
    start_phone = random.choice(phone_rules)
    # random.sample()的用法，多用于截取列表的中指定长度的随机数，但不会改变列表本身的排序
    random_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    end_phone = ''.join(random.sample(random_list, 8))
    logging.info(f"当前随机生成的case为：{start_phone+end_phone}")
    return start_phone + end_phone


# 随机生成不超过20位的字符串
def _random_str():
    random_list = ["a", "b", "c", "d", "4", "5", "6", "7", "8", "9"]
    return ''.join(random.sample(random_list, 9))


# 检查app的登录状态
def _is_login(driver):
    """ 从app首页点击我的，只要跳转页面不是登录页，则说明用户的状态为：已登录 """
    nav_p, login_p = NavPage(driver), LoginPage(driver)
    nav_p.nav_my()
    if "欢迎使用哈啰出行" in login_p.login_title():
        # 用户登录操作
        login_p.login_handle_operation(CD.user_phone)
    else:
        # 返回首页进行后续流程操作
        nav_p.nav_index()


# 检查app的登出状态
def _is_logout(driver):
    """ 从app首页点击我的，只要跳转页面不是登录页，则说明用户的状态为：已登录 """
    nav_p, personal_p = NavPage(driver), PersonalPage(driver)
    nav_p.nav_my()
    if personal_p.personal_status() is True:
        # 用户退出登录操作
        personal_p.personal_enter_setting()
        personal_p.personal_logout()
        personal_p.personal_popup_logout()


# 启动服务
def _base_driver(server_port=4723, **kwargs):
    # 读取手机默认配置
    desired_caps = HandleConfig().load_config(FilePath.read_specified_file(FilePath.CONFIG_FOLDER, "baseconfig.yaml"))
    # 通过adb命令动态获取当前设备的版本号，并更新到默认配置中
    devices = ADB.get_device_uuid()
    # 检测到1台设备，更新配置参数
    if len(devices) == 1:
        desired_caps["platformVersion"] = ADB.get_device_platVersion(devices[0])
    # 检测到多台，暂不支持多台，所以只将第1台的配置数据更新进来
    elif len(devices) > 1:
        logging.warning("目前识别到至少2台设备，无法确认使用哪个设备，默认使用第1台设备的平台版本号哦！")
        desired_caps["platformVersion"] = ADB.get_device_platVersion(devices[0])
    # 没有设备连接的时候，直接报错
    else:
        logging.error("没有可连接设备！")
        raise Exception("目前没有识别到可用设备，请确保至少1台设备可用！")
    # 循环定制化的配置项
    if kwargs:
        for key, value in kwargs.items():
            desired_caps[key] = value
    # 启动server会话
    driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(server_port), desired_caps)
    return driver
































#
# @pytest.fixture
# def register_app():
#     driver = _base_driver()
#     yield driver
#     # 注册成功之后，退出登录
#     _logout_from_register(driver)
#     sleep(2)
#     driver.close_app()
# # 退出登录
# def _logout_from_register(driver):
#     """Android端退出登录 个人中心页点击设置icon 点击退出登录 确认退出登录"""
#     android_p, personal_p = AndroidPage(driver), PersonalPage(driver)
#     android_p.android_app_left_back()
#     personal_p.personal_enter_settingg()
#     personal_p.personal_logout()
#     personal_p.personal_popup_logout()
#
#
# @pytest.fixture
# def start_app():
#     # 启动app
#     driver = _base_driver()
#     yield driver
#     sleep(5)
#     driver.close_app()
# # 退出登录
# def _logout_out(driver):
#     """Android端退出登录 个人中心页点击设置icon 点击退出登录 确认退出登录"""
#     android_p, personal_p = AndroidPage(driver), PersonalPage(driver)
#     android_p.android_app_left_back()
#     personal_p.personal_enter_settingg()
#     personal_p.personal_logout()
#     personal_p.personal_popup_logout()
#
#
# @pytest.fixture
# def logined(start_app):
#     _login_status(start_app)
#
#
# @pytest.fixture(scope="class")
# def is_login(start_app):
#     """
#     保持已登录
#     :param start_app: 服务driver
#     :return:
#     """
#     pass
#
#
# # 确保当前用户为登录状态
# def _login_status(driver):
#     """
#     进入个人信息页查看页面登录状态
#     :param driver:
#     :return:
#     """
#     pass
    
    # # 进入app首页
    # app_p, login_p, nav_p, per_p = AppIndexPage(driver), LoginPage(driver), NavPage(driver), PerInfoPage(driver)
    # # 底部导航，点击-我的，进入个人信息页面
    # nav_p.nav_my()
    # # 判断个人信息页面是否存在登录信息
    # if per_p.judge_login_success() is False:
    #     # TODO 登录   --- 分生产环境或者测试环境 - 分条件传入
    #     login_p.login(l_DATA.user_phone)
    # # 如果用户已经登录，则返回app首页
    # nav_p.nav_travel()


# appium服务器的启动参数，同时启动一个与appium server连接的会话
