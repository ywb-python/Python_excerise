#!/usr/bin/env python
#-*-coding:utf-8-*-


import profile

# 1.13
def reverse_input_1(obj_list):
    """
    逆置列表
    :param obj_list: 接收的列表
    :return:
    """
    for num in range(-1, -len(obj_list)):
        print(obj_list[len(obj_list) - num -1])


def reverse_input_2(obj_list):
    """

    逆置列表
    :param obj_list: 接收的列表
    :return:
    """
    obj_list.reverse()
    for element in obj_list:
        print(element)


def test_13():
    """
    :return:
    """
    obj_list = [3, 43, 32, 3, 3, 'wq', 'wq']
    t1 = profile.run('reverse_input_1(%s)' % obj_list)
    t2 = profile.run('reverse_input_2(%s)' % obj_list)
    print('================================')
    print(t1)
    print('==========================')
    print(t2)
    print('=========================')


#1.14
def check_int_sequence_exist_two_different_number_and_product_is_odd(sequence):
    """
    接收一个整数序列，判断该序列是否存在两个互不相同且他们的积为奇数的数
    :param sequence:
    :return:
    """
    set_sequence = set(sequence)
    if len(set_sequence) < 2:
        return False
    for one in set_sequence:
        for other in set_sequence:
            if (one != other) and ((one * other) % 2 == 1):
                return True
    return False


def test_14():
    obj_list = [3, 43, 32, 3, 3]
    a = check_int_sequence_exist_two_different_number_and_product_is_odd(obj_list)
    if a:
        print('该序列存在两个互不相同且他们的积为奇数的数')
    else:
        print('该序列不存在两个互不相同且他们的积为奇数的数')

def check_whether_has_same_element(obj_sequence):
    """
    1.15
    判断序列所有元素是否各不相同
    :param sequence:
    :return:
    """
    if len(obj_sequence) == len(set(obj_sequence)):
        print('该序列所有元素互不相同')
    else:
        print('该序列有相同元素')


def list_analysis_generate_obj_list():
    """
    1.18
    利用列表解析语法产生[0,2,6,12,20,30,42,56,72,90]
    :return:
    """
    return [i * (i + 1) for i in range(10)]


def list_analysis_generate_letter():
    """
    1.19
    利用列表解析语法在不输入所有英文字母的情况下产生包含所有小写英文字母的列表
    :return:
    """
    import string
    print([i for i in string.ascii_lowercase])

def main():
    test_13()
    test_14()
    test_15([1,3,2,4,23,42,32,43,5])
    print(test_18())
    test_19()


if __name__ == '__main__':
    main()




