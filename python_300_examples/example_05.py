#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 15:06
# @Author  : ywb
# @Site    : 二分查找
# @File    : example_05.py
# @Software: PyCharm


def binary_search(arrays: list, start: int, end: int, target: int) -> int:
    """
    二分查找
    :param arrays: 待查找序列
    :param start: 查找范围起点
    :param end:  查找范围终点
    :param target: 待查找的目标元素
    :return: 待查找的目标元素在待查找序列中第一次出现的位置
    """
    mid = (start + end) // 2
    if arrays[mid] == target:
        return mid
    if arrays[mid] < target:
        return binary_search(arrays, mid, end, target)
    return binary_search(arrays, start, mid, target)


def get_target_offset_in_arrays(arrays, target):
    """
    给定一个排序的整数数组(升序)和一个要查找的目标整数target，查找到target第1次出现
    的下标.
    如果target不在数组中，返回-1
    :param arrays: 排序的整数数组
    :param target: 目标整数
    :return: target第1次出现的下标。如果target不在数组中，返回-1
    """
    if target not in arrays:
        return -1
    return binary_search(arrays, 0, len(arrays) - 1, target)


if __name__ == "__main__":
    print(get_target_offset_in_arrays([1, 4, 4, 5, 7, 7, 8, 9, 9, 10], 1))
    print(get_target_offset_in_arrays([1, 2, 3, 3, 4, 5, 10], 3))
    print(get_target_offset_in_arrays([1, 2, 3, 3, 4, 5, 10], 6))
