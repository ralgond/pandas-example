import pandas as pd
import numpy as np

'''
在表3.1中，找出姓名为空值和不为空值的教师信息。
'''
t1 = pd.read_excel("../data/c3/1查找空值.xlsx", sheet_name="教师表");

t1.loc[len(t1.index)] = [1, pd.NA]

print (t1)

print(t1[t1.isna().any(axis=1)])