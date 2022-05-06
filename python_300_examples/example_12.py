#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 23:30
# @Author  : ywb
# @Site    :点积
# @File    : example_12.py
# @Software: PyCharm


def dot_product(arr1: list, arr2: list) -> int:
    """
    输入为A=[1，1，1]和B=[2，2，2]，输出为6，1*2+1*2+1*2=6。输入为A=[3，2]
    和B=[2，3，3]，输出为-1，没有点积。
    :param arr1:数组1
    :param arr2:数组2
    :return:存在点击则返回点积。没有点积，返回-1。
    """
    if len(arr1) != len(arr2):
        return -1
    return sum([arr1[i] * arr2[i] for i in range(len(arr1))])


if __name__ == "__main__":
    print(dot_product([1, 1, 1], [2, 2, 2]))
    print(dot_product([3, 2], [2, 3, 3]))
