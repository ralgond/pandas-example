import pandas as pd

'''
查找每个部门工资排在前两名的雇员信息，若雇员工资一样，则并列获取
'''

t1 = pd.read_excel("../data/c6/6查询排前两名的工资【举一反三】.xlsx", sheet_name="雇员表")

t1["rank"] = t1.groupby("部门编号")["工资"].rank(ascending=False, method="dense")

print(t1[t1["rank"] <= 2])