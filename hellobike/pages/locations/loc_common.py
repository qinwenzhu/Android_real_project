# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 5:20 下午
# @Author  : wenqinzhu
# @File    : loc_common.py
# @Software : PyCharm

""" 哈啰出行-共用-底部banner-页面元素定位 """
# app底部 - 首页
NAV_INDEX = 'new UiSelector().resourceId("com.jingyao.easybike:id/tv_tab_text").text("首页")'

# app底部 - 车主
NAV_CAR = 'new UiSelector().resourceId("com.jingyao.easybike:id/tv_tab_text").text("车主")'

# app底部 - 驿站
NAV_POST = 'new UiSelector().resourceId("com.jingyao.easybike:id/tv_tab_text").text("驿站")'

# app底部 - 钱包
NAV_WALLET = 'new UiSelector().resourceId("com.jingyao.easybike:id/tv_tab_text").text("钱包")'

# app底部 - 我的
NAV_MY = 'new UiSelector().resourceId("com.jingyao.easybike:id/tv_tab_text").text("我的")'
