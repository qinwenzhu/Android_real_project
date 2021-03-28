# -*- coding: utf-8 -*-
# @Time    : 2020/7/25 8:46 下午
# @Author  : wenqinzhu
# @File    : handle_config.py
# @Software : PyCharm

import yaml
import os


class HandleConfig(object):

    # 封装读取yaml文件
    def load_config(self, file_name):
        if os.path.exists(file_name):
            with open(file_name, mode='r', encoding='utf-8') as file:
                configs = yaml.safe_load(file)
        else:
            print("抱歉！文件不存在！")
            raise FileNotFoundError("文件不存在！")
        return configs
