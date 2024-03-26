import pandas as pd

'''
计算该6名同学的成绩中去除最高分、最低分后的平均分数。
'''
t1 = pd.read_excel("../data/c6/4去除最大值、最小值后求平均值【举一反三】.xlsx", sheet_name="某班 6 名同学的成绩")

t1['rank1'] = t1['成绩'].rank(ascending=False, method='first')
t1['rank2'] = t1['成绩'].rank(method='first')

t2 = t1[(t1['rank1'] > 1) & (t1['rank2'] > 1)]
print(t2['成绩'].mean())