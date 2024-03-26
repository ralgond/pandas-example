import pandas as pd

'''
按“成绩”列从大到小排列之后，进行累计求和计算。
'''

t1 = pd.read_excel("../data/c6/9学生成绩累计求和.xlsx", sheet_name="学生成绩表")

t2 = t1.sort_values('成绩', ascending=False)

t2['累计'] = t2["成绩"].cumsum();

print(t2)