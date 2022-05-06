#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 23:05
# @Author  : ywb
# @Site    : 孪生字符串
# @File    : example_10.py
# @Software: PyCharm


def twin_string(str1: str, str2: str) -> str:
    """
    给定两个字符串s和t，每次可以任意交换s的奇数位或偶数位上的字符，即奇数位上的字符能
    与其他奇数位的字符互换，偶数位上的字符也能与其他偶数位的字符互换，问能否经过若干
    次交换，使s变成t
    :param str1:字符串s
    :param str2:字符串t
    :return:s变成t返回Yes,不能返回No
    """
    str1_odd_list = sorted([el for index, el in enumerate(str1)
                            if index % 2 == 0])
    str1_even_list = sorted([el for index, el in enumerate(str1)
                             if index % 2 == 1])
    str2_odd_list = sorted([el for index, el in enumerate(str2)
                            if index % 2 == 0])
    str2_even_list = sorted([el for index, el in enumerate(str2)
                             if index % 2 == 1])
    if str1_odd_list == str2_odd_list and str1_even_list == str2_even_list:
        return 'Yes'
    return 'No'


if __name__ == '__main__':
    print(twin_string("abcd", "cdab"))
    print(twin_string("abcd", "bcda"))
    pass
