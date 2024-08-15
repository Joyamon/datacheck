# encoding: utf-8
# @Time    : 2020/5/6 10:42
# @function  : 装饰器，计算函数执行时间
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : compare_row_plus.py
# @Software: PyCharm
import time


def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print("function{}costs：{}s".format(func.__name__, round(end - start, 2)))
        return result

    return wrapper
