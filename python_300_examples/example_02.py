#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 22:15
# @Author  : ywb
# @Site    : 合并排序数组
# @File    : example_02.py
# @Software: PyCharm


def combine_two_arrays_to_new_ordered_arrays(
    one_array: list, other_array: list
) -> list:
    """
    合并两个升序的整数数组A和B，形成一个新的数组，新数组也要有序。
    :param one_array: 第一个升序数组
    :param other_array: 第二个升序数组
    :return: 合并后的新的有序数组
    """
    one_array.extend(other_array)
    return sorted(one_array)


if __name__ == "__main__":
    print(combine_two_arrays_to_new_ordered_arrays([1], [1]))
    print(combine_two_arrays_to_new_ordered_arrays([1, 2, 3, 4], [2, 4, 5, 6]))
    print(combine_two_arrays_to_new_ordered_arrays([1, 4], [1, 2, 3]))
