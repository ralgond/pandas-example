import pandas as pd
import datetime

'''
（1）剔除表中重复的购买记录。
（2）查询表中数据是否有空值的记录。
（3）将列“用户行为发生时间”重命名为“用户交易时间”
'''

t1 = pd.read_excel("../data/c3/3简单的数据查询.xlsx", sheet_name="用户购买记录")

t1.loc[len(t1.index)] = [1,1,pd.NA, pd.NA, pd.NA]

t1 = t1.dropna(axis=0)

print(t1.shape)

t1 = t1.drop_duplicates()

t1.rename(columns={'用户行为发生时间':'用户交易时间'}, inplace=True)

print(t1)
