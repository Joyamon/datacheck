
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

setup(
    name='datacheck',
    summary='数据校验工具',
    homepage='https://github.com/18152007693/datacheck',
    version='0.0.1',
    author='半只程序员',
    author_email='18152007693@163.com',
    packages=find_packages(),
    install_requires=[
        'pandas',
        'openpyxl',
        'logging'
    ]
)
