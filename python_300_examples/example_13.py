#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 23:34
# @Author  : ywb
# @Site    :函数运行时间
# @File    : example_13.py
# @Software: PyCharm


def get_func_time(arr: list) -> list:
    """
    输入s=["F1Enter10"，"F2Enter18"，"F2Exit19"，"F1Exit20"]，则输出
    ["F1|10"，"F2|1"]，即F1从10时刻进入，20时刻退出，运行时长为10，F2从18时刻进入，
    19时刻退出，运行时长为1。
    输入s=["F1Enter10"，"F1Exit18"，"F1Enter19"，"F1Exit20"]，则输出["F1|9"]，
    即F1从10时刻进入，18时刻退出；又从19时刻进入，20时刻退出，总运行时长为9。
    :param arr:描述函数进入和退出的时间列表
    :return:每个函数的运行时间列表
    """
    enter_time_list = sorted([i.split("Enter") for i in arr if "Enter" in i])
    exit_time_list = sorted([i.split("Exit") for i in arr if "Exit" in i])
    res = {}
    for enter, exit in zip(enter_time_list, exit_time_list):
        if enter[0] in res:
            res[enter[0]] += int(exit[-1]) - int(enter[-1])
        else:
            res[enter[0]] = int(exit[-1]) - int(enter[-1])
    return [f"{key}|{value}" for key, value in res.items()]


if __name__ == "__main__":
    print(get_func_time(["F1Enter10", "F2Enter18", "F2Exit19", "F1Exit20"]))
    print(get_func_time(["F1Enter10", "F1Enter19", "F1Exit18", "F1Exit20"]))
