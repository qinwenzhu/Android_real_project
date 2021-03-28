# -*- coding: utf-8 -*-
# @Time    : 2020/7/19 9:26 下午
# @Author  : wenqinzhu
# @File    : main.py
# @Software : PyCharm


import pytest


if __name__ == '__main__':
    # pytest.main(["-s", "-v", "--html=outputs/reports/report.html", "./hellobike/tests/test_register.py"])
    # pytest.main(["-s", "-v", "--html=outputs/reports/report.html", "-m", "test"])
    # pytest.main(["-s", "-v", "-m first", "--html=outputs/reports/report.html"])
    # pytest.main(["-s", "-v", "-m register", "--html=outputs/reports/report.html"])
    # pytest.main(["-s", "-v", "-m login", "--html=outputs/reports/report.html"])
    # pytest.main(["-s", "-v", "-m uat", "--html=outputs/reports/report.html"])
    # pytest.main(["-s", "-v", "-m pre", "--html=outputs/reports/report.html"])
    # pytest.main(["-s", "-v", "-m smoke", "--html=outputs/reports/report.html"])
    pytest.main(["-s", "-v", "-m test", "--html=outputs/reports/report.html"])
    # pytest.main()
    # pytest.main(["-s", "-v", "--reruns", "2", "--reruns-delay", "5"])
    # pytest.main(["-s", "-v", "-m", "test"])
    # pytest.main(["-s", "-v", "-m", "test", "--html=outputs/reports/report.html", "--alluredir=outputs/reports"])
