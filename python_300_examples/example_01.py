#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/3 22:09
# @Author  : ywb
# @Site    : 反转一个3位整数
# @File    : example_01.py
# @Software: PyCharm


def reverse_three_int_number(num: int) -> int:
    """
    反转一个3位整数
    :param num: 3位整数
    :return: 3位整数反转后的结果
    """
    return int("".join(list(reversed(str(num)))))


if __name__ == "__main__":
    print(reverse_three_int_number(123))
    print(reverse_three_int_number(900))
