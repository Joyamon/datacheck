## datacheck

@author: ��ֻ����Ա
@version: 0.0.1
@date: 2024-08-15

## ���

datacheck ��һ����������У��� Python �⡣
֧�ְ��У����бȽϣ�֧�ֶ����ļ���ʽ���� CSV��Excel �ȣ�֧���ļ������ͷ���������ã� ֧�ֶ����������ͺ�У�����
���Է���ؽ�������У�飻 ֧����־��¼��֧�������е��ã�֧�� GUI ���ã�֧�� Web ���ã�֧�� RESTful API ���á�

## ����

- �Ƚ������ļ��Ƿ���ͬ
- ���бȽ�
- ���бȽ�
- �Ƚ������ļ��Ƿ���ͬ���������ͬ��
- �Ƚ������ļ��Ƿ���ͬ���������ͬ��
- ֧�ֶ����������ͺ�У�����
- ֧���û������ֶ�У��
- ֧�ֶ����ļ���ʽ���� CSV��Excel ��
- ֧���ļ������ͷ����������
- ֧����־��¼
- ����ȥ��
- ֧�������е���
- ֧�� GUI ����
- ֧�� Web ����
- ֧�� RESTful API ����

## ��װ

```bash
pip install datacheck
```

## ʹ��ʾ��

* ���бȽ������ļ��Ƿ���ͬ

```python

from datacheck.compare_row_plus import CompareRowPlus

value1 = ['id', 'name', 'age']
value2 = ['id', 'name', 'age']
compare = CompareRowPlus('af1c9b53652bef321057dc5e8c89d77f.csv',
                         'af1c9b53652bef321057dc5e8c89d77f����.csv',
                         flag=1,
                         fields1=value1,
                         fields2=value2,
                         encoding='utf-16',
                         header=0,
                         directory="compare_result",
                         save_path='./compare_result/result.xlsx'
                         )
compare.run()
```

* ����˵��

| ������       | ����   | Ĭ��ֵ                | ˵��                                        |
|-----------|------|--------------------|-------------------------------------------|
| file1     | str  | None               | ��һ���ļ�·��                                   |
| file2     | str  | None               | �ڶ����ļ�·��                                   |
| flag      | int  | 0                  | 0: �Ƚ������ļ��Ƿ���ͬ���������ͬ�У�1: �Ƚ������ļ��Ƿ���ͬ���������ͬ�� |
| fields1   | list | None               | ��һ���ļ����ֶ��б�Ĭ�϶Ա������ֶ�                       |
| fields2   | list | None               | �ڶ����ļ����ֶ��б�Ĭ�϶Ա������ֶ�                       |
| encoding  | str  | 'utf-8'            | �ļ�����                                      |
| header    | int  | 0                  | �ļ�ͷ������                                    |
| directory | str  | result             | �ԱȽ�����Ŀ¼                                  |
| save_path | str  | result/result.xlsx | �ԱȽ������ļ�                                  |

    ע�⣺directory �� save_path ����ͬʱ���ڣ�����ᱨ��:
    ʹ��ʾ����
    ��� directory="compare_result" �� save_path="./compare_result/result.xlsx" �����ڣ���ԱȽ���ᱣ���� compare_result/result.xlsx �ļ��С�
    ��� directory�� save_path �������ڣ���ԱȽ����Ĭ�ϱ����ڵ�ǰĿ¼�µ� result/result.xlsx �ļ��С�

* �ļ�ȥ��deduplicate

```python
from datacheck.deduplicate import deduplicate

deduplicate(data='af1c9b53652bef321057dc5e8c89d77f.csv',
            column_name=['id', 'name', 'age']
            )

```

* ����˵��

| ������         | ����   | Ĭ��ֵ | ˵��      |
|-------------|------|-----|---------|
| data        | str  | ��   | �ļ�·��    |
| column_name | list | ��   | ��Ҫȥ�ص��ֶ� |

* �жԱȣ���ֵͬ��Ϊ��ɫ�����뵽Excel�ļ� compare_two_column

```python
from datacheck.compare_column import compare_two_column

compare_two_column(data='af1c9b53652bef321057dc5e8c89d77f.csv',
                   column1='id',
                   column2='name',
                   output='compare_result')


```

* ����˵��

| ������     | ����  | Ĭ��ֵ | ˵��       |
|---------|-----|-----|----------|
| data    | str | ��   | �ļ�·��     |
| column1 | str | ��   | ��һ���ֶ�    |
| column2 | str | ��   | �ڶ����ֶ�    |
| output  | str | ��   | ����ԱȽ���ļ� |

## ��Ŀ�ṹ

```
datacheck
    ������ result   # �ԱȽ�����Ŀ¼
    ������ files     # �Ա��ļ�Ŀ¼
    ������ __init__.py  # ��ʼ���ļ�
    ������ README.md     # ��Ŀ˵���ļ�
    ������ requirements.txt     # ��Ŀ�����ļ�
    ������ deduplicate.py        # �ļ�ȥ��
    ������ compare_column.py        # �жԱ�
    ������ compare_field.py        # �ֶζԱ�
    ������ compare_numeral_field.py     # ��ֵ�ֶζԱ�
    ������ compare_row.py            # �жԱ�
    ������ compare_row_plus.py         # �жԱ� ֧���Զ����ֶΣ�ȫ���ֶζԱ�
    ������ logger.py                # ��־��¼
    ������ read_table.py        # ��ȡ�ļ���csv,Excel��
    ������ timer.py                # ��ʱ��
    ������ setup.py             # ��װ�ļ�
    
      
```
## �ԱȽ��ͼ
* df1
![image](pic/df1.png)
* df2
![image](pic/df2.png)
* �ԱȽ��
![image](pic/result.png)


## ����

��ӭ�ύ issue �� PR��һ������ datacheck �⡣

## ���֤

datacheck ��һ����Դ��Ŀ��ʹ�� MIT ���֤��



