#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 22:30
# @Author  : ywb
# @Site    : 旋转字符串
# @File    : example_03.py
# @Software: PyCharm
import collections


def rotate_str(obj_str: str, offset: int) -> str:
    """
    给定一个字符串（以字符数组的形式）和一个偏移量，根据偏移量原地从左向右旋转字符串。
    :param obj_str: 目标字符串
    :param offset: 偏移量
    :return: 字符串按照给定偏移量从左向右旋转后的新字符串
    """
    q = collections.deque(list(obj_str))
    q.rotate(offset)
    return "".join(q)


if __name__ == "__main__":
    print(rotate_str("abcdefg", 3))
    print(rotate_str("abcdefg", 0))
    print(rotate_str("abcdefg", 1))
    print(rotate_str("abcdefg", 2))
