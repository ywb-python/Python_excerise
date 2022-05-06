#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 23:19
# @Author  : ywb
# @Site    :最接近target的值
# @File    : example_11.py
# @Software: PyCharm


def almost_target_value(target: int, array: list) -> int:
    """
    给出一个数组，在数组中找到2个数，使得它们的和最接近但不超过目标值，返回它们的和。
    :param target:目标值
    :param array:数组
    :return:在数组中找到2个数的和
    """
    sum_list = [
        el1 + el2 for i, el1 in enumerate(array) for j, el2 in enumerate(array)
        if i < j
    ]
    return max([i for i in sum_list if target - i >= 0])


if __name__ == "__main__":
    print(almost_target_value(15, [1, 3, 5, 11, 7]))
    print(almost_target_value(16, [1, 3, 5, 11, 7]))
