import pandas as pd
import numpy  as np

'''
分析订单数在0-2、3-5、5单以上的各有多少人。
'''
t1 = pd.read_excel("../data/c4/5店铺订单分析.xlsx", sheet_name="订单表")

t1['等级'] = np.where(t1['订单数'] <= 2, '0-2', 
            np.where(t1['订单数'] <= 5, '3-5', '5以上'))

print(t1.groupby('等级').agg({'客户编码':'count'}).rename(columns={'客户编码':'数量'}))