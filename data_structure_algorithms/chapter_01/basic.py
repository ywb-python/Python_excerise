#!/usr/bin/env python
# -*-coding:utf-8-*-
import random


def is_multiple(n: int, m: int) -> bool:
    """
    1.1
    用来接收两个整数n和m，如果n是m的倍数，返回True,否则返回False
    :param n: 第一个整数
    :param m: 第二个整数
    :return:如果n是m的倍数，返回True,否则返回False
    """
    if n % m == 0:
        return True
    else:
        return False


def is_even(k: int) -> bool:
    """
    1.2
    用来接收一个整数k，如果k是m偶数，返回True,否则返回False。不能使用乘法、除法、
    取余操作
    :param k: 接收的整数
    :return:如果k是m偶数，返回True,否则返回False
    """
    if k & 1:
        return False
    else:
        return True


def minmax(data: list) -> tuple:
    """
    1.3
    用来接收一个数的序列,在数的序列中找到最小数和最大数，并以一个长度为2的元组的形式返回
    :param data:接收的一个数的序列
    :return:序列中的最小数和最大数
    """
    for i in range(len(data)):
        for j in range(i, len(data)):
            if data[i] > data[j]:
                data[i], data[j] = data[j], data[i]
    return data[0], data[-1]


def sum_of_squares(n: int) -> int:
    """
    1.4
    用来接收一个正整数n，返回1到n的平方和
    :param n: 接收的正整数
    :return:1到n的平方和
    """
    total = 0
    for num in range(n):
        total += num * num
    return total


def sum_of_squares2(n: int) -> int:
    """
    1.5
    用python解析语法和内置函数sum用来接收一个正整数n，返回1到n的平方和
    :param n: 接收的正整数
    :return:1到n的平方和
    """
    return sum(num * num for num in range(n))


def sum_of_squares_all_old(n: int) -> int:
    """
    1.6
    用来接收一个正整数n，返回1到n中所有奇数的平方和
    :param n: 接收的正整数
    :return:1到n中所有奇数的平方和
    """
    total = 0
    for num in range(n):
        if num % 2 == 1:
            total += num * num
    return total


def sum_of_squares_all_old2(n: int) -> int:
    """
    1.7
    用python解析语法和内置函数sum用来接收一个正整数n，返回1到n中所有奇数的平方和
    :param n: 接收的正整数
    :return:1到n中所有奇数的平方和
    """
    return sum(i * i for i in list(range(n)) if i % 2 != 0)


def search_plus_index_make_plus_index_value_the_same_as_minus_index_value(
    s: str, k: int
) -> int:
    """
    1.8
    对一个长度为n的字符串,当索引值-n<=k<0时，求一个正整数索引j>=0，使得s[j]=s[k]
    :param s: 字符串
    :param k: 负索引
    :return:满足j>=0，使得s[j]=s[k]的正整数k
    """
    j = len(s) + k
    assert s[j] == s[k]
    return j


def generate_special_sequence(start: int, end: int, steps: int) -> list:
    """
    1.9,1.10
    生成指定排列
    :param start:起始值
    :param end: 结束值
    :param steps: 间隔
    :return:所生成的指定排列
    """
    return sorted(list(range(start, end, steps)), reverse=True)


def use_list_of_analytical_generate_list(n: int) -> list:
    """
    1.11
    利用列表解析语法产生列表
    :param n:指定值
    :return:列表
    """
    return [2**num for num in range(n + 1)]


def archive_choice_function(data: list) -> int:
    """
    1.12
    利用random模块的randrange实现random模块的choice
    :param data: 选择的序列
    :return:随即返回的数字
    """
    return data[random.randrange(0, len(data))]


def main():
    # print(is_multiple(6, -3))
    # print(is_even(4))
    # print(minmax([1, 2, 3, 4, 3, 2, 2, 3, -9, 8, 1.0]))
    print(sum_of_squares(10))
    print(sum_of_squares2(10))
    # print(sum_of_squares_all_old(10))
    # print(search_plus_index_make_plus_index_value_the_same_as_minus_index_value('shkasgad', -3))
    # print(generate_special_sequence(50,90,10))
    # print(generate_special_sequence(-8,10,2))
    # print(use_list_of_analytical_generate_list(8))
    # print(archive_choice_function([1, 2, 4, 8, 16, 32, 64, 128, 256]))


if __name__ == "__main__":
    main()
