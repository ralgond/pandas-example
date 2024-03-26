import pandas as pd

'''
查找所有连续出现3次的成绩。
'''

t1 = pd.read_excel("../data/c6/13连续出现 N 次问题【举一反三】.xlsx", sheet_name="成绩表")

# t1 = t1.sort_values("成绩")

t1['成绩1'] = t1["成绩"].shift(1)
t1['成绩2'] = t1["成绩"].shift(2)

#print(t1)

print(t1[(t1['成绩']==t1['成绩1']) & (t1['成绩']==t1['成绩2'])])