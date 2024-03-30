|标签|Pandas|SQL|
|----|------|---|
|窗口函数|t1['排名'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='first')|SELECT *, row_number() over (partition by 学号 order by 成绩 desc) as 排名|
|窗口函数|t1['排名'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='min')|SELECT *, rank() over (partition by 学号 order by 成绩 desc) as 排名|
|窗口函数|t1['排名'] = t1.groupby("学号")['成绩'].rank(ascending=False, method='dense')|SELECT *, dense_rank() over (partition by 学号 order by 成绩 desc) as 排名|
|窗口函数|t2 = t1.sort_values('成绩', ascending=False)<br> t2['累计'] = t2["成绩"].cumsum()|SELECT *, SUM(成绩) over(order by 成绩 desc rows between unbounded preceding and current row) AS 累计 FROM 学生成绩表;|
|窗口函数|t1 = pd.read_excel("../data/c6/10低于平均薪水的员工.xlsx", sheet_name="薪水表")<br>t2 = t1.groupby("部门编号")["薪水"].mean().rename("平均薪水")<br>t3 = t1.merge(t2, how="left", on="部门编号")<br>t3[t3["薪水"] < t3["平均薪水"]]|SELECT 雇员编号,部门编号,薪水 FROM (SELECT *， AVG(薪水) OVER (PARTITION BY 部门编号) AS 平均薪水 FROM 薪水表) AS a WHERE 薪水 < 平均薪水;|
|窗口函数|t1 = pd.read_excel("../data/c6/14连续访问记录.xlsx", sheet_name="访问记录表")<br>t1 = t1.sort_values(by=["访问页面时间"])<br>t1["上一个访问的页面"] = t1.groupby("用户ID")["访问的页面"].shift(1)<br>print(t1[t1['访问的页面'] != t1['上一个访问的页面']])|SELECT a.用户ID, a.访问的页面, a.访问页面时间 FROM <br>(SELECT 用户ID,访问的页面,访问页面时间, LAG(访问的页面, 1) OVER (PARTITION BY 用户ID ORDER BY 访问页面时间 ASC) AS 上一个访问页面 from 访问记录表) as a WHERE a.上一个访问的页面 IS NULL OR a.访问的页面 != a.上一个访问的页面;|
