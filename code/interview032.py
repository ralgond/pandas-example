import pandas as pd

'''
查询每门课程前三名学生的成绩。
'''

t1 = pd.read_excel("../data/c6/5查询排前三名的成绩.xlsx", sheet_name="成绩表")

t1["rank"] = t1.groupby("课程号")['成绩'].rank(ascending=False, method="dense");

print(t1[t1['rank'] <= 3])
