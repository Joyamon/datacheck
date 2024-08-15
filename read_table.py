
# -*- coding: utf-8 -*-
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : read_table.py
# @Software: PyCharm

from typing import Any
import pandas as pd
from pandas import DataFrame


def get_data_from_file(file: Any, encoding='utf-8', errors='replace', header=None) -> DataFrame:
    """
    get datas from file(excel or csv)
    :param header:
    :param errors:
    :param encoding: file‘s encoding
    :param file: Excel objects
    :return: Excel datas

    """
    if file is None:
        raise ValueError("文件名不能为空")
    if file.split('.')[-1] in ['xlsx', 'xls']:
        data = pd.read_excel(file, header=header)
        data.dropna()
        return data
    elif file.split('.')[-1] == 'csv':
        if encoding == 'utf-16':
            data = pd.read_csv(file, sep='\t', index_col=False, encoding=encoding, low_memory=False, )
            if '\t' in data.columns:
                data[data.columns] = data[data.columns].str.strip('\t')  # 去掉结算ID尾部的tab键
            else:
                return data
        else:
            data = pd.read_csv(file, index_col=False, encoding=encoding, low_memory=False)
            return data
