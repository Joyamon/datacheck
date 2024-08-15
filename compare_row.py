# encoding: utf-8
# @Time    : 2024/08/13
# @Author  : 半只程序员
# @Email   : 18152007693@163.com
# @File    : compare_row.py
# @Software: PyCharm


from .read_table import get_data_from_file


def compare():
    df = get_data_from_file('飞帆 - 副本.csv', encoding='utf-16')
    # 判断 SPU 和 SKU 是否相等
    # df["是否相等"] = df["系统SPU"] == df["系统SKU"] and df["电话"] == df["phone"]
    df["是否相等"] = (df["系统SPU"] == df["系统SKU"]) & (df["电话"] == df["phone"])
    equal_sku_spu = df[df["是否相等"]]
    print(equal_sku_spu)

    # 创建一个样式函数，用于设置背景色
    def highlight_all(s):
        return ['background-color: yellow'] * len(s)

    # 应用样式
    styled_df = equal_sku_spu.style.apply(highlight_all, axis=1)
    # 保存为Excel文件，包含样式
    try:
        styled_df.to_excel('equal_sku_spu_with_color.xlsx', index=False, engine='openpyxl')
        print("文件已保存为 'equal_sku_spu_with_color.xlsx'")
    except PermissionError:
        print('文件已打开，请关闭它')


if __name__ == '__main__':
    print(compare())
