|标签|Pandas|SQL|
|----|------|---|
|窗口函数|t1['排名'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='first')|SELECT *, row_number() over (partition by 学号 order by 成绩 desc) as 排名|
|窗口函数|t1['排名'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='min')|SELECT *, rank() over (partition by 学号 order by 成绩 desc) as 排名|
|窗口函数|t1['排名'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='dense')|SELECT *, dense_rank() over (partition by 学号 order by 成绩 desc) as 排名|
