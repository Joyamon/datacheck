# encoding: utf-8
import pandas as pd

# 示例数据框
df1 = pd.DataFrame({
    'field1': [1, 2, 3, 4, 5],
    'field2': [1, 2, 3, 4, 5],
    'field3': [1, 2, 3, 4, 5],
    'field4': [1, 2, 3, 4, 5],
    'field5': [1, 2, 3, 4, 5]
})

df2 = pd.DataFrame({
    'field1': [1, 2, 3, 4, 0],
    'field2': [1, 2, 3, 0, 5],
    'field3': [1, 2, 0, 4, 5],
    'field4': [1, 0, 3, 4, 5],
    'field5': [0, 2, 3, 4, 5]
})

# 给定长度index
length_index = 5

# 要判断相等的字段列表
fields1 = [f'field{i+1}' for i in range(length_index)]
fields2 = [f'field{i+1}' for i in range(length_index)]

# 根据长度index动态构建相等判断条件
conditions = [(df1[fields1[i]] == df2[fields2[i]]) for i in range(length_index)]

# 将所有条件合并
df1['是否相等'] = pd.DataFrame(conditions).all()

print(df1)