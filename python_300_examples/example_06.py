#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 22:13
# @Author  : ywb
# @Site    :下一个更大的数
# @File    : example_06.py
# @Software: PyCharm


def search_next_big_number(one_list: list, other_list: list) -> list:
    """
    两个不重复的数组nums1和nums2，其中nums1是nums2的子集。在nums2的相应位
    置找到nums1所有元素的下一个更大数字。nums1中的数字x的下一个更大数字是nums2中x右边
    第1个更大的数字。如果它不存在，则为此数字输出-1。nums1和nums2中的所有数字都是唯一的
    nums1和nums2的长度不超过1000。
    :param one_list: 数组nums1
    :param other_list: 数组nums2
    :return: 查找结果列表
    """
    length = len(one_list)
    result = [None] * length
    for index1 in range(length):
        if other_list[index1 + 1] > one_list[index1]:
            result[index1] = other_list[index1]
        else:
            result[index1] = -1
    return result


if __name__ == "__main__":
    res = search_next_big_number([4, 1, 2], [1, 3, 4, 2])
    print(res)
