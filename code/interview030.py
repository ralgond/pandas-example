import pandas as pd
import numpy  as np

'''
查询出每个部门去除最高、最低薪水后的平均薪水。
'''
t1 = pd.read_excel("../data/c6/3去除最大、最小值后求平均值.xlsx", sheet_name="Sheet3")

t1['rank1'] = t1.groupby("部门编号")['薪水'].rank(ascending=False, method="first")
t1['rank2'] = t1.groupby("部门编号")['薪水'].rank(method="first")

t2 = t1[(t1['rank1'] > 1) & (t1['rank2'] > 1)]
print(t2)

t3 = t2.groupby("部门编号")["薪水"].mean()
print(t3)