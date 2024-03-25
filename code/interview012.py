import pandas as pd
import numpy  as np

'''
以60分为及格线，标记出每一行的成绩是及格还是不及格。
'''

t1 = pd.read_excel("../data/c4/3判断成绩及格与否.xlsx", sheet_name="学生成绩表")

t1['是否及格'] = np.where(t1['成绩'] < 60, '不及格', '及格')

print(t1)