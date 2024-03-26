import pandas as pd
import numpy as np

'''
（1）分析平台售卖螺蛳粉的店铺数、总销售额、商品种类数、总购买人数等。
（2）找出销售额排名前10的店铺，并明确其购买人数、销售额。
（3）找出购买人数排名前10的商品，并明确其购买人数。
（4）明确螺蛳粉商品的价格区间是怎么分布的，以及每个区间的占比（按照0～50元，51～100元，101～150元，150元以上区间进行分析）。
（5）找出螺蛳粉购买人数最多的前10个地域
'''

t1 = pd.read_excel("../data/c8/1店铺销售分析.xlsx", sheet_name="Sheet1")

#(1)
print("店铺数:", t1["店铺名称"].nunique())
print("总销售额:", round(t1["价格"] * t1["购买人数"]).sum()/10000, 2)
print("商品种类数:", t1["商品名称"].nunique())
print("总购买人数:", round(t1["购买人数"].sum() / 10000, 2))

#(2)
# 计算每种商品的销售额
t1['销售额'] = t1['价格']*t1["购买人数"]
# 计算每个店铺的销售额
t2 = t1.groupby("店铺名称").agg({'销售额':"sum", '购买人数':"sum"})

t2["店铺销售额排名"] = t2['销售额'].rank(ascending=False, method='first')

t3 = t2[t2['店铺销售额排名'] <= 10].sort_values("店铺销售额排名")

print(t3)

#(3)
t2 = t1.groupby("商品名称").agg({'购买人数':"sum"});

t2['购买人数排名'] = t2['购买人数'].rank(method="first", ascending=False)

t2 = t2[t2['购买人数排名'] <= 10]

print (t2.sort_values("购买人数排名"))

#(4)
t1['价格区间'] = np.where(t1['价格'] <= 50, "0-50",
                      np.where(t1['价格'] <= 100, "51-100",
                               np.where(t1['价格'] <= 150, "101-150", "150以上")))

print (t1.groupby("价格区间").agg({"商品名称":"count"}).rename(columns={"商品名称":"数量"}))

#(5) 
t2 = t1.groupby("买家地址").agg({"购买人数":"sum"})

t2['排名'] = t2['购买人数'].rank(ascending=False, method="first")

t3 = t2[t2['排名'] <= 10]

print (t3.sort_values("排名"))