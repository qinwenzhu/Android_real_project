# -*- coding: utf-8 -*-
# @Time    : 2020/8/23 1:17 下午
# @Author  : wenqinzhu
# @File    : user_info.py
# @Software : PyCharm


class UserInfo(object):

    def __init__(self, name, cer_id, national):
        """
        实名认证参数化
        :param name: 姓名
        :param cer_id: 证件号
        :param national: 国籍/地区
        """
        self.__name = name
        self.__cer_id = cer_id
        self.__national = national

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def cer_id(self):
        return self.__cer_id

    @cer_id.setter
    def cer_id(self, value):
        self.__cer_id = value

    @property
    def national(self):
        return self.__national

    @national.setter
    def national(self, value):
        self.__national = value
