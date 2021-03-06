# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:40 下午
# @Author  : wenqinzhu
# @File    : handle_log.py
# @Software : PyCharm

import logging


""" 日志等级
'DEBUG': 打印全部的日志
'INFO': 打印info,warning,error,critical级别的日志
'WARNING': 打印warning,error,critical级别的日志
'ERROR': 打印error,critical级别的日志
'CRITICAL': 打印critical级别
"""


class HandleLog(object):
    """ 封装日志操作 """

    def __init__(self, file_name=None):
        """
        定义日志输出到文件的路径
        :param file_name: 文件路径
        """
        # 定义日志对象
        self.logger = logging.getLogger("")
        # 设置日志收集等级
        self.logger.setLevel(logging.DEBUG)
        # 设置日志输出格式，并添加到控制台和文件内部
        formatter = logging.Formatter('[%(asctime)s] - %(levelname)s - %(message)s')

        # TODO 当log文件不存在会自动创建的，所以注释
        # if not os.path.exists(file_name):
        #     with open(file_name, mode='w', encoding='utf-8') as file:
        #         log_file = logging.FileHandler(file_name, encoding='utf-8')

        # 如果文件路径为空，则只将日志输出到控制台
        if file_name is None:
            # 定义日志输出到控制台
            console = logging.StreamHandler()
            # 设置日志在控制台中的输出等级<ERROR>
            console.setLevel(logging.ERROR)
            # 设置日志在控制台中输出的格式
            console.setFormatter(formatter)
            # 添加日志句柄
            self.logger.addHandler(console)
        else:
            # 如果文件路径不为空的情况下，同时将日志输出到控制台和对应日志文件

            console = logging.StreamHandler()
            console.setLevel(logging.ERROR)
            console.setFormatter(formatter)
            self.logger.addHandler(console)

            # 定义日志输出到指定路径 <file_name>，并设置日志输出的等级<INFO>
            log_file = logging.FileHandler(file_name, encoding='utf-8')
            # log_file.setLevel(logging.DEBUG)
            log_file.setLevel(logging.INFO)
            log_file.setFormatter(formatter)
            # 添加日志句柄
            self.logger.addHandler(log_file)

    def info(self, message):
        # 定义日志的info方法，打印info等级的日志
        self.logger.info(message)

    def debug(self, message):
        self.logger.debug(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def get_logger(self):
        """ 通过调用方法得到日志对象 """
        return self.logger


if __name__ == '__main__':
    log = HandleLog("log.txt").get_logger()
    log.debug('debug')
    log.info('info')
    log.warning('warning')
    log.error('error')
    log.critical('严重')
