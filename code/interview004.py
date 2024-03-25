import pandas as pd

'''
现需要分析出用户的总数、用户的平均年龄。
'''
t1 = pd.read_excel("../data/c3/4游戏APP用户分析.xlsx", sheet_name="用户登录信息表")

t1 = t1.drop_duplicates(subset=['用户ID'])

print("用户总数:", len(t1))
print("用户平均年龄:", t1['用户年龄'].mean())