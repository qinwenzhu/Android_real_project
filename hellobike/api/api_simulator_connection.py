# -*- coding: utf-8 -*-
# @Time    : 2020/10/21 10:43 上午
# @Author  : wenqinzhu
# @File    : api_simulator_connection.py
# @Software : PyCharm

import logging
import requests


# 模拟器连接操作
class ApiSimConnect:

    header = {"token": "f0e363b77e68d2b0634adb8e91a147d0", "content-type": "application/json"}

    def __init__(self, bike_no):
        self.bike_no = bike_no

    """
    调用测试工具平台，通过车辆编号获取车辆key
    http://testtool.hellobike.cn/#/hellobike-app/bikeKey?token=fa0f9a5866d6ef5577f2d2570cff983f
    """
    def get_encrypt_key(self):
        url = "http://47.98.110.181:8099/api/getbikekeybyno"
        json_data = {"env": "uat", "bike_no": "2100202566", "bike_type": "hellobike"}
        json_data["bike_no"] = self.bike_no
        res = requests.post(url=url, json=json_data)
        result = res.json()["msg"]
        failure_result = "没有找到相应bikeKey,请输入正确的bikeNo!"
        # 如果通过车辆编号未获取到对应加密的key
        if failure_result in result:
            logging.info("获取车辆key失败！")
            print(result)
        else:
            logging.info("成功获取到车辆编号，并对车辆key进行截取")
            # 返回单车加密后的key
            return result[-16:]

    # 连接模拟器
    def connect_sim(self):
        url = "https://fat-bikesimulator-back.hellobike.cn/Bike/connectAndRegister"
        json_data = {"appVersion": 11, "bikeId": "2100202566", "bikeType": "bike", "encryptKey": "055C3DC0A8B2BA39",
                     "env": "uat", "isACK": 1, "isHeartBeat": 1, "lock": 0, "lockWorkMode": 0, "projectVersion": 1,
                     "replyOpenLockSuccess": 1,
                     "softwareVersion": 0}
        json_data["bikeId"] = self.bike_no
        json_data["encryptKey"] = self.get_encrypt_key()
        response = requests.post(url=url, json=json_data, headers=self.header)
        print("成功连接模拟器！")

    # 通过调用模拟器 - 关锁
    def close_lock(self):
        url = "https://fat-bikesimulator-back.hellobike.cn/Bike/closeLock"
        json_data = {"bikeId": "2100202566", "bikeType": "bike", "encryptKey": "055C3DC0A8B2BA39",
                     "closeReason": 0, "env": "uat", "lng": "121.442649", "lat": "31.26848"}
        json_data["bikeId"] = self.bike_no
        json_data["encryptKey"] = self.get_encrypt_key()
        response = requests.post(url=url, json=json_data, headers=self.header)
        print("---成功关锁---")


    # 断开模拟器
    def disconnect_sim(self):
        url = "https://fat-bikesimulator-back.hellobike.cn/Bike/close"
        json_data = {"env": "uat", "bikeType": "bike", "bikeId": "2100202566", "encryptKey": "055C3DC0A8B2BA39"}
        json_data["bikeId"] = self.bike_no
        json_data["encryptKey"] = self.get_encrypt_key()
        response = requests.post(url=url, json=json_data, headers=self.header)
        print("成功断开模拟器!")


if __name__ == '__main__':
    api_name = ApiSimConnect("2100130708")
    # 模拟器连接
    api_name.connect_sim()
