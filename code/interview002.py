import pandas as pd

'''
需要知道店铺里每个访客和对应的浏览日期（每个访客同一天浏览多次算作一次记录）。
'''

t1 = pd.read_excel("../data/c3/2电商用户行为.xlsx", sheet_name="用户行为表")

print (t1)

t1 = t1.drop_duplicates(subset=['访客id', '浏览日期'])

print(t1)