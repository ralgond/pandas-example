import pandas as pd

'''
如何分析每个城市的总流入人口数量
'''

t1 = pd.read_excel("../data/c3/7城市人口流动分析.xlsx", sheet_name="各城市人口流动表")

print(t1.groupby('流入城市').agg({'数量': sum}))