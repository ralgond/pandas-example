import pandas as pd

'''
剔除访问次数前20%的用户后得到每类用户的平均访问次数。
'''

t1 = pd.read_excel("../data/c6/8用户访问次数.xlsx", sheet_name="用户访问次数表")

t1['pct_rank'] = t1['访问量'].rank(ascending=False, pct=True)

t2 = t1[t1["pct_rank"] > 0.2]

print(t2.groupby("用户类型")['访问量'].mean())