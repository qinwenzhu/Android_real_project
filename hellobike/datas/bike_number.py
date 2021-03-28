# -*- coding: utf-8 -*-
# @Time    : 2020/10/20 7:59 下午
# @Author  : wenqinzhu
# @File    : bike_number.py
# @Software : PyCharm

# uat环境通过模拟器操作   ---- 普通车
uat_simulator = ["2100130708"]

""" uat环境模拟器
uat模拟器 - 曼哈顿   软件版本 22  锁版本 12
 2100096162 2100128841
uat模拟器 - P10     软件版本 2 锁版本 32
    * 2100146865
"""
# uat环境通过模拟器操作   ---- 曼哈顿
uat_manhd_lock = ["2100096162"]

# uat环境通过模拟器操作   ---- 轮毂锁P10
uat_lungs_lock = ["2100146865"]

""" uat环境真锁
锁编号	     环境
2100200345   uat(测试锁)  高校车 - 南翔古镇
2100029484   uat(测试锁)  高校车 - 南翔古镇
2100202225   uat(本人)
2100205462   uat(熊丽)
"""
# uat环境真锁 - 普通车
uat_really_normal = ["2100202225"]
# uat_really_normal = [{"bike_no": "2100205462"}, {"bike_no": "2100202225"}]
# uat环境真锁 - 曼哈顿
uat_really_manhd = [{"bike_no": "2100205462"}]
# uat环境真锁 - 高校车/普通锁
uat_sh_university = [{"bike_no": "2100200345"}]
# uat环境真锁 - 高校车/曼哈顿
uat_sh_university_mhd = {"bike_no": "2100029484"}

"""  pre 环境真锁
锁编号	     环境
9120207735   pre(本人)
9170011055   pre(熊丽)



"""


# pre_really_normal = [
#     {"bike_no": "9120207761"}, {"bike_no": "9170011055"}
# ]
# TODO 关锁流程

"""
负责人	锁编号	    版本	环境	可用状态
熊丽	    2700005030	3代	PRO	可用      3代
张焱	    3790689506	4代	PRO	可用      4代
郭从波	2700188046	3代	PRO	可用
罗秀英	9130109793	C55	PRO	可用
王艳茹	5190527411	3代	PRO	可用
赵宗丽	3510235296	4代	PRO	可用
黄佳欢	9170010581	C50	PRO	可用
郝亮	    9190403977	C55	PRO	可用
戈晓鹏	9170005351	C50	PRO	可用
祝文琴	9170014703	C50	PRO	可用      C50
王珠强	3790574322	4代	PRO	可用
蒋鹏鑫	9190403993	C55	PRO	可用
尹坤鹏	3510240118	4代	PRO	可用
"""

# 生产环境 - 曼哈顿车辆 - 城市(上海)
pro_sh_normal = [
    {"bike_no": "9190403977"}
]
# 生产环境 - 普通车车辆 - 城市(上海)
pro_sh_manhd = [
    {"bike_no": "2700005030"},
    {"bike_no": "3790689506"},
    {"bike_no": "2700188046"},
    {"bike_no": "5190527411"},
    {"bike_no": "3510235296"},
    {"bike_no": "9170010581"},
    {"bike_no": "9170005351"},
    {"bike_no": "9170014703"},
    {"bike_no": "3790574322"},
    {"bike_no": "9190403993"},
    {"bike_no": "3510240118"}
]


"""           -------  pre 真锁  锁具上的固定车辆  -------
pre环境 锁具上的车辆编号
普通车：9120207761
曼哈顿：9190477598
高校车：2500225235  --- 西子国际
"""
pre_locks_normal = [
    {"bike_no": "9120207761"}
]
pre_locks_manhd = [
    {"bike_no": "9190477598"}
]
pre_locks_university = [
    {"bike_no": "2500225235"}
]
