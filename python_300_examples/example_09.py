#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 22:58
# @Author  : ywb
# @Site    :不重复的两个数
# @File    : example_09.py
# @Software: PyCharm


def search_no_repeat_number(array: list) -> list:
    """
    给定一个数组a[]，其中除了2个数，其他均出现2次，请找到不重复的2个数并返回。
    :param array:数组
    :return:数组中不重复的2个数的列表
    """
    return [i for i in array if array.count(i) == 1]


if __name__ == "__main__":
    print(search_no_repeat_number([1, 2, 5, 5, 6, 6]))
    print(search_no_repeat_number([3, 2, 7, 5, 5, 7]))
    print(search_no_repeat_number([1, 2, 5, 1]))
