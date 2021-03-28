# -*- coding: utf-8 -*-
# @Time    : 2021/1/20 2:10 下午
# @Author  : wenqinzhu
# @File    : loc_app_index.py
# @Software : PyCharm

""" 哈啰出行-平台首页-页面元素定位 """

# 平台首页 - 扫一扫
# APP_SCAN = 'new UiSelector().text("扫一扫").className("android.widget.TextView")'
APP_SCAN = 'new UiSelector().resourceId("com.jingyao.easybike:id/scanLayout")'

# 平台首页 - 单车
APP_BIKE = 'new UiSelector().text("红包车").resourceId("com.jingyao.easybike:id/topTv")'

# 平台首页 - 消息
APP_INFO = "com.jingyao.easybike:id/messageTv"
