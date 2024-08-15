# -*- coding: utf-8 -*-
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : deduplicate.py
# @Software: PyCharm
from .read_table import get_data_from_file
from typing import List



def deduplicate(data, column_name: List = None):
    """
    去重
    :param data: 文件路径
    :param column_name: 列名(唯一值)
    :return:去重后的数据
    """
    try:
        df = get_data_from_file(data)
    except UnicodeDecodeError as e:
        df = get_data_from_file(data, encoding='utf-16')
    df.drop_duplicates(subset=column_name, inplace=True)
    return df


if __name__ == '__main__':
    # '../飞帆.csv'
    deduplicate('', ['商品名称'])
