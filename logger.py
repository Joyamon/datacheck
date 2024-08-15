# encoding: utf-8
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : logger.py
# @Software: PyCharm

import logging
from functools import wraps


def setup_logger(name, log_file, level=logging.DEBUG):
    """Function to setup logger"""
    logger = logging.getLogger(name)
    logger.setLevel(level)

    # 日志输出格式
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # 控制台日志
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # 文件日志
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)

    # 添加处理器
    logger.addHandler(console_handler)
    logger.addHandler(file_handler)

    return logger


# 初始化日志
logger = setup_logger('半只程序员>>>', 'log/compare_row_plus.log')


def log_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return wrapper
