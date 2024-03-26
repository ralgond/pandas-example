import pandas as pd
import numpy  as np

'''
需要我们取得每名学生不同课程的成绩排名
'''
t1 = pd.read_excel("../data/c6/1学生成绩排名.xlsx", sheet_name="成绩表")

'''
成绩    rank()  dense_rank()    row_number()
100     1       1               1
100     1       1               2
100     1       1               3
98      4       2               4
'''

t1['row_number'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='first')
t1['rank'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='min')
t1['dense_rank'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='dense')

print(t1)