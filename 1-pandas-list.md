# Pandas和List

```
>>> import pandas as pd
>>> df = pd.DataFrame( {'a':['A','A','B','B','B','C'], 'b':[1,2,5,5,4,6]})
>>> df
   a  b
0  A  1
1  A  2
2  B  5
3  B  5
4  B  4
5  C  6
>>> df.groupby("a")['b'].apply(list)
a
A       [1, 2]
B    [5, 5, 4]
C          [6]
Name: b, dtype: object
>>> df.groupby("a")['b'].apply(list).reset_index(name='new')
   a        new
0  A     [1, 2]
1  B  [5, 5, 4]
2  C        [6]
>>> df2 = df.groupby("a")['b'].apply(list).reset_index(name='new')
>>> df2.explode('new')
   a new
0  A   1
0  A   2
1  B   5
1  B   5
1  B   4
2  C   6
```
