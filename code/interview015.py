import pandas as pd
import numpy  as np

'''
查询运单号创建日期在5月、不同单量区间的客户分布
'''
t1 = pd.read_excel("../data/c4/6快递量区间分布.xlsx", sheet_name="快递量区间分布")

print(t1.dtypes)

t2 = t1[(t1['创建日期'] >= pd.Timestamp("2020-05-01")) & (t1['创建日期'] <= pd.Timestamp("2020-05-31"))]

t3 = t2.drop_duplicates(subset=['运单号']).groupby("客户id").agg({"运单号":"count"}).rename(columns={"运单号":"单量"})



t3['单量区间'] = np.where(t3['单量'] <= 5, "0-5",
                      np.where(t3['单量'] <= 10, "6-10",
                               np.where(t3['单量'] <= 20, "11-20", "20以上")))

t3 = t3.reset_index()

t4 = t3.groupby("单量区间").agg({"客户id":"count"}).rename(columns={"客户id":"客户数"})

print(t4)