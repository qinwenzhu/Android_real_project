# -*- coding: utf-8 -*-
# @Time    : 2021/3/10 5:06 下午
# @Author  : wenqinzhu
# @File    : test_forbid_lock.py
# @Software : PyCharm


""" 禁停区关锁
对应位置存在禁停区经纬度
对应环境开启禁停区配置
人和车都位于禁停区内
禁停区关锁
"""

import pytest
import time


@pytest.mark.test
def test_forbid(start_app_and_check_login):
    # assert True
    time.sleep(100000)
    pass
