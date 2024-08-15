# encoding: utf-8
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : compare_numeral_field.py
# @Software: PyCharm

def numeral_field_compare(field1, field2):
    if field1 == '' or field2 == '':
        return 'compare field is null'
    try:
        if isinstance(field1, (int, str, float)) and isinstance(field2, str):
            if float(field1).__eq__(float(field2)):
                return True
            else:
                return False
        if isinstance(field1, float) and isinstance(field2, float):
            if field1.__eq__(field2):
                return True
    except ValueError:
        return False


if __name__ == '__main__':
    print(numeral_field_compare("37.96", "37.960000"))
