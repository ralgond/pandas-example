import pandas as pd
import numpy  as np

'''
分析各订单的退款率（这里的退款率公式为：退款率=退款金额/订单金额）。
'''
t1 = pd.read_excel("../data/c5/2退款分析.xlsx", sheet_name="订单表")

t2 = pd.read_excel("../data/c5/2退款分析.xlsx", sheet_name="退款表")

t3 = t1.merge(t2, how="left", on=["订单号","商品号"])

t4 = t3.groupby("订单号").agg({"金额_x":"sum", "金额_y":"sum"})

print(t4['金额_y'] / t4['金额_x'])