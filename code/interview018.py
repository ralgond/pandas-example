import pandas as pd
import numpy  as np

'''
查找出所有学生的学号、姓名、课程和成绩
'''
t1 = pd.read_excel("../data/c5/1多表查询解题步骤的应用.xlsx", sheet_name="学生信息表")

t2 = pd.read_excel("../data/c5/1多表查询解题步骤的应用.xlsx", sheet_name="学生成绩表")

print(t1.merge(t2, how='left', on='学号'))