import pandas as pd

'''
查找“学生表”中所有重复的学生姓名
'''
t1 = pd.read_excel("../data/c3/6查找重复数据.xlsx", sheet_name="学生表")

print(t1[t1.duplicated(subset=['姓名'])])