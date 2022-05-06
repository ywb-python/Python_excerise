#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/7/4 14:52
# @Author  : ywb
# @Site    : 相对排名
# @File    : example_04.py
# @Software: PyCharm


def relative_ranking(scores: list) -> list:
    """
    根据N名运动员得分，找到相对等级和最高分前3名的人名，其余的输出分数
    :param scores: 运动员得分列表
    :return: 相对等级和最高分前3名的人名，其它人的分数
    """
    scores.sort()
    person_scores = {0: "Gold Medal", 1: "Sliver Medal", 2: "Bronze Medal"}
    for num in range(len(scores)):
        if num < 3:
            scores[num] = person_scores[num]
        else:
            scores[num] = str(scores[num])
    return scores


if __name__ == "__main__":
    print(relative_ranking([5, 4, 3, 2, 1]))
