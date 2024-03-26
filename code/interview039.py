import pandas as pd

'''
统计出连续3次为球队得分的球员名单
'''

t1 = pd.read_excel("../data/c6/12连续三次为球队得分的球员名单.xlsx", sheet_name="分数表")

t1 = t1.sort_values(by=["球队", "得分时间"])

print(t1)

t1["球员姓名1"] = t1.groupby("球队")['球员姓名'].shift(1)

t1["球员姓名2"] = t1.groupby("球队")['球员姓名'].shift(2)

print(t1[(t1["球员姓名"] == t1["球员姓名1"]) & (t1["球员姓名"] == t1["球员姓名2"])].drop_duplicates("球员号码"))