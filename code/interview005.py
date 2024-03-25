import pandas as pd

'''
分析购买人数、总销售金额、客单价、客单件、人均购买频次。
'''
t1 = pd.read_excel("../data/c3/5公司经营指标.xlsx", sheet_name="销售订单表")

print("购买人数:", len(t1.drop_duplicates(subset=['顾客ID'])))

print("总销售金额:", (t1['销售数量'] * t1['零售价']).sum())

print("客单价:", (t1['销售数量'] * t1['零售价']).sum() / len(t1.drop_duplicates(subset=['顾客ID'])))

print("客单件:", (t1['销售数量']).sum() / len(t1.drop_duplicates(subset=['顾客ID'])))

print("人均购买频次:", len(t1) / len(t1.drop_duplicates(subset=['顾客ID'])))
