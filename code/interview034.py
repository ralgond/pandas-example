import pandas as pd

'''
查询每个班级成绩排在前40%的学生信息。
'''

t1 = pd.read_excel("../data/c6/7前40%用户.xlsx", sheet_name="成绩表")

t2 = t1.groupby("班级")['成绩'].quantile(0.4)

print (t2)

t3 = t1.merge(t2, how="left", on="班级")

print(t3)

print(t3[t3['成绩_x'] >= t3['成绩_y']])
