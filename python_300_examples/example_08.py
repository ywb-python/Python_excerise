#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2022/5/6 22:48
# @Author  : ywb
# @Site    : 勒索信
# @File    : example_08.py
# @Software: PyCharm


def ransom_letter(note: str, adaline: str) -> bool:
    """
    给定一个表示勒索信内容的字符串和另一个表示杂志内容字符串，写一个方法判断能否通过
    剪下杂志中的内容构造出这封勒索信，若可以，返回True，否则返回False。
    注：杂志字符串中的每一个字符仅能在勒索信中使用一次
    :param note: 勒索信的内容
    :param adaline: 杂志的内容
    :return:通过剪下杂志中的内容构可以造出这封勒索信返回True，否则返回False
    """
    note_count_list = [note.count(i) for i in note]
    adaline_count_list = [adaline.count(i) for i in note]
    if note_count_list == adaline_count_list:
        return True
    return False


if __name__ == "__main__":
    print(ransom_letter("aa", "aab"))
