# encoding: utf-8
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : compare_field.py
# @Software: PyCharm

def field_compare(field1, field2):
    if field1 == '' or field2 == '':
        return 'compare field is null'
    try:
        if isinstance(field1, str) and isinstance(field2, str):
            if field1.__eq__(field2):  # 两个字符串相等
                return True
            else:
                return False
    except ValueError:
        return False


if __name__ == '__main__':
    print(field_compare('456', '123'))
