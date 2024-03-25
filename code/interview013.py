import pandas as pd
import numpy  as np

'''
请查询不及格（<60分）、及格（60～70分）、良好（71～85分）、优秀（86～100分）的学生各有多少人。
'''

t1 = pd.read_excel("../data/c4/4学生成绩分析.xlsx", sheet_name="学生分数表")

t1['等级'] = np.where(t1['分数'] < 60, "不及格",
            np.where(t1['分数'] < 71, "及格",
            np.where(t1['分数'] < 86, '良好', '优秀')))

print(t1.groupby('等级').agg({'学号':'count'}).rename(columns={'学号':'数量'}))