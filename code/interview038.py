import pandas as pd

'''
查询出每个部门低于平均薪水的雇员，然后进行培训来提高雇员工作效率，从而提高雇员薪水。
'''

t1 = pd.read_excel("../data/c6/10低于平均薪水的员工.xlsx", sheet_name="薪水表")

t2 = t1.groupby("部门编号")["薪水"].mean().rename("平均薪水")

t3 = t1.merge(t2, how="left", on="部门编号")

print(t3[t3["薪水"] < t3["平均薪水"]].sort_values(by=["部门编号","雇员编号"]))