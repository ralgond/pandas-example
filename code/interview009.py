import pandas as pd

'''
请查找既购买过ProductA产品又购买过ProductB产品，但没有购买ProductC产品的顾客人数。
'''

t1 = pd.read_excel("../data/c4/2如何找出多条件的用户.xlsx", sheet_name="销售订单表")

t1_a = t1[t1['产品']=='ProductA']['顾客ID'].unique();
t1_b = t1[t1['产品']=='ProductB']['顾客ID'].unique();
t1_c = t1[t1['产品']=='ProductC']['顾客ID'].unique();

print(t1_a)
print(t1_b)
print(t1_c)

print(t1[(t1['顾客ID'].isin(t1_a)) & (t1['顾客ID'].isin(t1_b)) & (~t1['顾客ID'].isin(t1_c))])