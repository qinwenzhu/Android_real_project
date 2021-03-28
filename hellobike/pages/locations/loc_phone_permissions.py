# -*- coding: utf-8 -*-
# @Time    : 2021/1/22 7:33 下午
# @Author  : wenqinzhu
# @File    : loc_phone_permissions.py
# @Software : PyCharm

""" 哈啰出行-OPPO手机相机授权 """

# 相机权限1
PER_CAMERA1 = "com.jingyao.easybike:id/okView"
# 相机权限2 - 系统弹窗，点击允许
PER_CAMERA2 = '//*[@text="允许"]'

# app权限1 - 勾选同意
PER_APP1 = "com.jingyao.easybike:id/protocol_rl"
# app权限2 - 开启服务
PER_APP2 = "com.jingyao.easybike:id/tv_agree_privacy"
# app权限3 - 手机系统弹窗-确定按钮
PER_APP3 = '//*[@text="确定"]'
# app权限4 - 手机系统弹窗-取消按钮
PER_APP4 = '//*[@text="取消"]'

# app权限5 - 消息弹窗 - 去开启
PRE_APP5 = 'new UiSelector().text("去开启").className("android.widget.Button")'
# app权限6 - 消息弹窗 - 取消
PRE_APP6 = 'new UiSelector().text("取消").className("android.widget.Button")'

# 从手机上传照片
SELECT_CAMERA = '//*[@text="相册"]'
