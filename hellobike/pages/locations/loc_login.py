# -*- coding: utf-8 -*-
# @Time    : 2021/1/21 7:21 下午
# @Author  : wenqinzhu
# @File    : loc_login.py
# @Software : PyCharm

""" 哈啰出行-登录页元素定位 """
# 登录页 - 手机号输入框
LOGIN_PHONE = "com.jingyao.easybike:id/mobilePhoneEdt"
# 登录页 - 勾选条款
LOGIN_AGREE = "com.jingyao.easybike:id/protocolCheckIv"
# 登录页 - 勾选条款
LOGIN_START = "com.jingyao.easybike:id/loginTv"

# 登录页 - 页面主标题
LOGIN_TITLE = 'new UiSelector().className("android.widget.TextView").text("欢迎使用哈啰出行")'


""" 哈啰出行-登录验证码页元素定位 """
# 验证码 - 数字1
CODE_N1 = "com.jingyao.easybike:id/first_et"
# 验证码 - 数字2
CODE_N2 = "com.jingyao.easybike:id/second_et"
# 验证码 - 数字3
CODE_N3 = "com.jingyao.easybike:id/third_et"
# 验证码 - 数字4
CODE_N4 = "com.jingyao.easybike:id/forth_et"
