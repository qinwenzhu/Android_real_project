# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:34 下午
# @Author  : wenqinzhu
# @File    : file_path.py
# @Software : PyCharm

import os


# 项目文件路径处理
class FilePath:

    # 获取当前文件的绝对路径
    current_path = os.path.abspath(__file__)
    """ 通过 os.path.split() 对路径进行逐级分割直至获取到项目的根目录 """
    PRO_PATH = os.path.split(os.path.split(os.path.abspath(__file__))[0])[0]
    # print(PRO_PATH)

    # 定位到 configs 目录
    CONFIG_FOLDER = f"{PRO_PATH}/hellobike/configs/"

    # 定位到 datas 目录
    DATA_FOLDER = f"{PRO_PATH}/hellobike/datas"

    # 定位到 logs 目录
    LOG_FOLDER = f"{PRO_PATH}/outputs/logs"

    # 定位到屏幕截图 <screenshots> 目录
    SCREENSHOT_FOLDER = f"{PRO_PATH}/outputs/screenshots"

    @staticmethod
    def read_specified_file(parent_file, current_file):
        """
        封装文件拼接：读取指定文件夹下的指定文件
        :param parent_file: 文件夹的前置路径
        :param current_file: 当前文件名
        :return: 完成文件路径
        """
        file_path = os.path.join(parent_file, current_file)
        return file_path
