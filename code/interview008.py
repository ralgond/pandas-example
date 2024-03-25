import pandas as pd

'''
现在需要找出语文课中成绩排名第二的学生成绩
'''

t1 = pd.read_excel("../data/c4/1查找成绩第二名的学生成绩.xlsx", sheet_name="课程表")

t2 = t1[t1['课程']=='语文']

print(t2[t2['成绩'] < t2['成绩'].max()]['成绩'].max())