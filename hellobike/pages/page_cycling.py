# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 10:28 上午
# @Author  : wenqinzhu
# @File    : cycling.py
# @Software : PyCharm

from time import sleep
from appium.webdriver.common.mobileby import MobileBy as MB
from utils.basepage import BasePage
from hellobike.api.api_simulator_connection import ApiSimConnect
from hellobike.pages.locations import loc_cycling as LC
from hellobike.datas import bike_number as BIKENO


# 骑行流程：骑行中页面
class CyclingPage(BasePage):

    # 获得页面标题文本：骑行中
    def cycling_get_page_title(self):
        return self.get_text((MB.ID, LC.CYCLING_PAGE_TITLE))

    # 骑行中 - 点击我要还车
    def cycling_return_bike(self):
        self.click_ele((MB.ID, LC.RETURN_CAR))

    # # 骑行页面，当前车辆的骑行时间
    # def cycling_min(self):
    #     # 定位当前订单的骑行时间
    #     MIN_TIME = (MB.ID, "com.jingyao.easybike:id/tv_min")
    #     return self.get_text(MIN_TIME)
    #
    # # 通过app前端点击我要还车
    # def return_bike(self):
    #     # 定位-我要还车按钮
    #     MIN_TIME = (MB.ID, "com.jingyao.easybike:id/tv_return_biken")
    #     return self.get_text(MIN_TIME)
    #
    # # 曼哈顿前端还车的步骤
    # def continue_return_bike(self):
    #     # 定位-确认还车按钮
    #     MIN_TIME = (MB.ID, "com.jingyao.easybike:id/backTv")
    #     return self.get_text(MIN_TIME)
    #
    # # 有卡用户-免费信息 。 无卡用户-计价规则
    # def price_rule(self):
    #     # 是否是计价规则
    #     MIN_TIME = (MB.ID, "com.jingyao.easybike:id/tv_price_rule")
    #     print(self.get_text(MIN_TIME))
    #     print(type(self.get_text(MIN_TIME)))
    #     return self.get_text(MIN_TIME)
    #
    # # 针对测试环境，普通车关锁通过调用api接口  --- appium服务器超过60s会自动结束进程，所以此处不能强制等待2分钟以上 --- 方案pass
    # def judge_cycling_time(self):
    #     sleep(125)
    #     result = self.cycling_min()
    #     if int(result) >= 2:
    #         # 调用关锁api接口 - 关锁
    #         ApiSimConnect(BIKENO.uat_sh_ordinary_lock[0])
    #         return True
    #     else:
    #         # TODO 查看详情页
    #         sleep(3)
