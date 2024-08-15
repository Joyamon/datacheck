# encoding: utf-8
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : compare_row_plus.py
# @Software: PyCharm

import os
import pandas as pd
from .logger import log_decorator, logger
from .read_table import get_data_from_file


def _get_filename(path):
    # 获取文件名
    if os.path.exists(path):
        return os.path.splitext(path)[0]
    return os.path.basename(path)


@log_decorator
class CompareRowPlus:
    def __init__(self, file1, file2, save_path='result/result.xlsx', directory='result', fields1=[], fields2=[], flag=0,
                 encoding='utf-8', header=0):
        """
        :Description:  比较两个文件中指定字段是否相等，并输出对比结果到文件
        :flag=0,默认为0，比对输入相同结果，flag=1，比对输入不同结果，默认为0
        :param file1:  对比文件1
        :param file2:  对比文件1
        :param save_path: 对比后文件保存路径,默认result.xlsx，可自定义指定
        :param directory: 保存文件目录，默认为空，即当前目录
        :param encoding: 文件编码 默认utf-8
        :param header:   文件表头 默认0
        :param fields1:   需要对比的字段，默认为空，即对比所有字段,可自定义比较字段
        :param fields2:   需要对比的字段，默认为空，即对比所有字段,可自定义比较字段

        """
        self._flag = flag
        self._save_path = save_path
        self._directory = directory
        self._fields1 = fields1
        self._fields2 = fields2
        self._file1 = file1
        self._file2 = file2
        self._header = header
        self._encoding = encoding  # 文件编码
        self._file_name1 = _get_filename(file1)  # 获取文件1名称
        self._file_name2 = _get_filename(file2)  # 获取文件2名称

    def _create_directory(self, directory):
        # 创建目录
        if self._directory:
            directory = self._directory
        if not os.path.exists(directory):
            os.makedirs(directory)
            return True
        return False

    def _file1_path(self):  # 获取文件1路径
        return self._file1

    def _file2_path(self):  # 获取文件2路径
        return self._file2

    def _read_file(self, file_path):
        # 读取文件
        if self._encoding:
            return get_data_from_file(file_path, encoding=self._encoding, header=self._header)
        else:
            return get_data_from_file(file_path)

    @staticmethod
    def _highlight_all(s):
        # 创建一个样式函数，用于设置背景色
        return ['background-color: #d68b8b'] * len(s)

    def _set_background_color(self, common):
        # 标记背景颜色
        return common.style.apply(self._highlight_all, axis=1)

    def _save_file(self, common):
        # 另存为文件
        try:
            if self._save_path:
                self._save_path = self._save_path
            self._set_background_color(common).to_excel(self._save_path, index=False, engine='openpyxl')
            return True
        except PermissionError:
            logger.debug("file is open,please close it first")
            return False

    def _compare_data(self, df1, df2):
        if not self._fields1 and not self._fields2:
            # 如果没有指定字段，则比较所有字段
            self._fields1 = df1.columns.tolist()
            self._fields2 = df2.columns.tolist()
            conditions = [(df1[self._fields1[i]] == df2[self._fields2[i]]) for i in range(len(self._fields1))]
            # 将所有条件合并
            df1['is_equal'] = pd.DataFrame(conditions).all()
            common = df1[df1['is_equal']] if self._flag == 0 else df1[~df1['is_equal']]
            common = common.drop(columns=['is_equal'])
            if not self._save_file(common):  # 另存为文件
                return False
            else:
                self._save_file(common)
                logger.debug(
                    f"{self._file_name1} 和 {self._file_name2} compared done,same data save to {self._save_path}file")
            return common
        else:
            # 如果指定了字段，则只比较指定字段
            self._fields1 = self._fields1
            self._fields2 = self._fields2
            conditions = [(df1[self._fields1[i]] == df2[self._fields2[i]]) for i in range(len(self._fields1))]
            # 将所有条件合并
            df1['is_equal'] = pd.DataFrame(conditions).all()
            common = df1[self._fields1][df1['is_equal']] if self._flag == 0 else df1[self._fields1][~df1['is_equal']]
            if not self._save_file(common):  # 另存为文件
                return False
            else:
                self._save_file(common)
                logger.debug(
                    f"{self._file_name1} 和 {self._file_name2} compared done,same data save to {self._save_path}file")
            return common

    def run(self):
        df1 = self._read_file(self._file1_path())  # 读取file1数据
        df2 = self._read_file(self._file2_path())  # 读取file2数据

        if df2.equals(df1):
            logger.debug(f"{self._file_name1} 和 {self._file_name2} data is same about all fields")
            return ''
        if df1.shape[0] != df2.shape[0]:  # 数据条数不一致，不进行字段比较
            logger.debug(f"{self._file_name1} 和 {self._file_name2} data is not same about all fields")
            return ''
        self._create_directory(self._directory)  # 创建目录
        compared_data = self._compare_data(df1, df2)
        return compared_data


if __name__ == '__main__':
    compare = CompareRowPlus('./files/01a35fe046c530226b78f5de48eb3a48备份.csv',
                             './files/01a35fe046c530226b78f5de48eb3a48.csv',
                             flag=1,
                             # fields1=value,
                             # fields2=value,
                             encoding='utf-16',
                             directory="compare_result",
                             save_path='compare_result/result.xlsx',
                             header=0)
    compare.run()
