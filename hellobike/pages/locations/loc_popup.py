# -*- coding: utf-8 -*-
# @Time    : 2021/1/28 7:32 下午
# @Author  : wenqinzhu
# @File    : loc_popup.py
# @Software : PyCharm


""" 哈啰出行-弹窗操作 """

# app首页
# 天降红包 - 忍痛离开
POPOP_LEAVE = "com.jingyao.easybike:id/refuseBtn"
# 天降红包 - 立即领取
POPUP_RECEIVE = "com.jingyao.easybike:id/receiveBtn"

# 消息通知 - 取消
POPOP_INFO_CANCLE = 'new UiSelector().text("取消").className("android.widget.Button")'
# 消息通知 - 去开启
POPUP_INFO_GO = 'new UiSelector().text("去开启").className("android.widget.Button")'
