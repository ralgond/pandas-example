import pandas as pd

'''
现在要求当用户连续访问同一个页面时，只保留第一次访问记录
'''

t1 = pd.read_excel("../data/c6/14连续访问记录.xlsx", sheet_name="访问记录表")

t1 = t1.sort_values(by=["用户ID", "访问的页面", "访问页面时间"])

t1["上一个访问的页面"] = t1.groupby("用户ID")["访问的页面"].shift(1)

print(t1[t1['访问的页面'] != t1['上一个访问的页面']])