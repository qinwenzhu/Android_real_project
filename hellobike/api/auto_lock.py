# -*- coding: utf-8 -*-
# @Time    : 2021/2/5 5:12 下午
# @Author  : wenqinzhu
# @File    : auto_lock.py
# @Software : PyCharm


import requests


# 调永凡的接口进行自动关锁操作
def lock_bike(num=1):
    url = "http://172.17.212.83:8980/"
    json_data = {"operation": "closeLock", "num": "1"}
    json_data["num"] = num
    res = requests.post(url=url, json=json_data)
    print(res)


if __name__ == '__main__':
    lock_bike()
    # lock_bike(2)
    # lock_bike(3)
