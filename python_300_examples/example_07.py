#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/4 22:36
# @Author  : ywb
# @Site    : 字符串中的单词数
# @File    : example_07.py
# @Software: PyCharm
import re


def calculate_words(word_str: str) -> int:
    """
    计算字符串中的单词数，其中一个单词定义为不含空格的连续字符串。
    :param word_str:字符串中
    :return:符串中的单词数
    """
    return len(re.findall(r'\w+', word_str))


if __name__ == "__main__":
    print(calculate_words("Hello, my name is John"))
