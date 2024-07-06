premium-algo-100
【数组 / 字符串】
数组列表中的最大距离 中等
摆动排序 中等
易混淆数 简单
字符串的左右移 简单
相隔为1的编辑距离 中等
反转字符串中的单词II 中等
形成字符串的最短路径 中等
【滑动窗口】
至多包含两个不同字符的最长子串 中等
至多包含 K 个不同字符的最长子串 中等
最大连续1的个数II 中等
长度为K的无重复字符子串 中等
【哈希】
找出变位映射 简单
回文排列 简单
句子相似性 简单
单行键盘 简单
移位字符串分组 中等
最大唯一数 简单
数元素 简单
找出所有行中最小公共元素 中等
【矩阵】
有效的单词方块 简单
孤独像素I 中等
稀疏矩阵的乘法 中等
粉碎糖果 中等
【区间集合】
缺失的区间 简单
会议室 简单
会议室II 中等
给字符串添加加粗标签 中等
删除区间 中等
【栈】
三元表达式解析器 中等
寻找排列 中等
基本计算器III 困难
【队列】
数据流中的移动平均值 简单
第一个唯一数字 中等
【链表】
删除链表M个节点之后的N个节点 简单
循环有序列表的插入 中等
给单链表加一 中等
逆序打印不可变链表 中等
【二叉树】
二叉树最长连续序列 中等
二叉树最长连续序列II 中等
统计同值子树 中等
子树的最大平均值 中等
二叉树的边界 中等
寻找二叉树的叶子节点 中等
二叉树的垂直遍历 中等
【二叉搜索树】
最接近的二叉搜索树值 简单
最接近的二叉搜索树值II 困难
验证二叉搜索树的前序遍历序列 中等
查找两棵二叉搜索树之和 中等
最大二叉搜索子树 中等
【N叉树】
克隆N叉树 中等
找到N叉树的根节点 中等
N叉树的直径 中等
【图】
搜寻名人 中等
杀掉进程 中等
无向图中连通分量的数目 中等
从始点到终点的所有路径 中等
网络爬虫 中等
岛屿数量II 困难
不同岛屿的数量 中等
并行课程 中等
【图 - 广度优先搜索】
迷宫 中等
迷宫II 中等
迷宫 III 困难
进击的骑士 中等
墙与门 中等
离建筑物最近的距离 困难
火星词典 困难
【前缀树】
设计内存文件系统 困难
设计搜索自动补全系统 困难
【堆】
前五科的均分 简单
连接木棍的最低费用 中等
校园自行车分配 中等
K距离间隔重排字符串 困难
【二分查找】
等差数列中缺失的数字 简单
有序数组中的缺失元素 中等
找到最大整数的索引 中等
检查一个数是否在数组中占绝大多数 简单
分享巧克力 困难
子数组最大平均数II 困难
【设计】
设计井字棋 中等
贪吃蛇 中等
迭代压缩字符串 简单
字符串的编码与解码 中等
锯齿迭代器 中等
最大栈 困难
力扣排行榜 中等
序列化和反序列化N叉树 困难
将N叉树编码为二叉树 困难
【回溯】
中心对称数II 中等
因子的组合 中等
花括号展开 中等
【动态规划】
栅栏涂色 中等
粉刷房子 中等
粉刷房子II 困难
四个键的键盘 中等
不相交的握手 困难
【数学】
阿姆斯特朗数 简单
统计只含单一字母的子串 简单
找出隐藏数组中出现次数最多的元素 中等
矩阵中1的最大数量 困难

sql-premium-50
【查询】
寻找今年具有正收入的客户 简单
从不订购的客户 简单
计算特殊奖金 简单
购买了产品A和产品B却没有购买产品C的顾客 中等
每位学生的最高成绩 中等
题目及答案：编写解决方案，找出每位学生获得的最高成绩和它所对应的科目，若科目成绩并列，取 course_id 最小的一门。查询结果需按 student_id 增序进行排序。
示例 1：
输入：
Enrollments 表：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 2          | 2         | 95    |
| 2          | 3         | 95    |
| 1          | 1         | 90    |
| 1          | 2         | 99    |
| 3          | 1         | 80    |
| 3          | 2         | 75    |
| 3          | 3         | 82    |
+------------+-----------+-------+
输出：
+------------+-------------------+
| student_id | course_id | grade |
+------------+-----------+-------+
| 1          | 2         | 99    |
| 2          | 2         | 95    |
| 3          | 3         | 82    |
+------------+-----------+-------+
```sql
select student_id, course_id, grade
from (
    select student_id, course_id, grade,
    rank() over (partition by student_id order by grade desc, course_id asc) as ranking 
    from Enrollments
) t1
where t1.ranking = 1
order by student_id asc;
```
【连接】
组合两个表 简单
没有卖出的卖家 简单
排名靠前的旅行者 简单
销售员 简单
计算布尔表达式的值 中等
题目及答案：计算表 Expressions 中的布尔表达式。
示例 1：
输入：
Variables 表:
+------+-------+
| name | value |
+------+-------+
| x    | 66    |
| y    | 77    |
+------+-------+
Expressions 表:
+--------------+----------+---------------+
| left_operand | operator | right_operand |
+--------------+----------+---------------+
| x            | >        | y             |
| x            | <        | y             |
| x            | =        | y             |
| y            | >        | x             |
| y            | <        | x             |
| x            | =        | x             |
+--------------+----------+---------------+
输出:
+--------------+----------+---------------+-------+
| left_operand | operator | right_operand | value |
+--------------+----------+---------------+-------+
| x            | >        | y             | false |
| x            | <        | y             | true  |
| x            | =        | y             | false |
| y            | >        | x             | true  |
| y            | <        | x             | false |
| x            | =        | x             | true  |
+--------------+----------+---------------+-------+
解释：
如上所示, 你需要通过使用 Variables 表来找到 Expressions 表中的每一个布尔表达式的值.
```sql
select e.left_operand, e.operator, e.right_operand,
case e.operator
      when '>' then if(v1.value > v2.value, 'true', 'false')
      when '<' then if(v1.value < v2.value, 'true', 'false')
      else if (v1.value=v2.value, 'true', 'false')
end as value
from Expressions e
left join Variables v1 on e.left_operand=v1.name
left join Variables v2 on e.right_operand=v2.name;
```
查询球队积分 中等
```sql
select team_id, team_name, 
ifnull(sum(m.num_points), 0) num_points
from Teams
left join (
    select host_team as team_id, 
    (case 
    when host_goals > guest_goals then 3
    when host_goals = guest_goals then 1
    else 0 end) num_points from Matches
    union all
    select guest_team as team_id, 
    (case 
    when host_goals < guest_goals then 3
    when host_goals = guest_goals then 1
    else 0 end) num_points from Matches
) m
on Teams.team_id = m.team_id
group by team_id
order by team_id asc, num_points desc;
```
【聚合函数】
2020年最后一次登录 简单
游戏玩法分析I 简单
仓库经理 简单
订单最多的客户 简单
查找每个员工花费的总时间 简单
即时食物配送I 简单
苹果和桔子 中等
两人之间的通话次数 中等
题目及答案：编写解决方案，统计每一对用户 (person1, person2) 之间的通话次数和通话总时长，其中 person1 < person2
输入：
Calls 表：
+---------+-------+----------+
| from_id | to_id | duration |
+---------+-------+----------+
| 1       | 2     | 59       |
| 2       | 1     | 11       |
| 1       | 3     | 20       |
| 3       | 4     | 100      |
| 3       | 4     | 200      |
| 3       | 4     | 200      |
| 4       | 3     | 499      |
+---------+-------+----------+
输出：
+---------+---------+------------+----------------+
| person1 | person2 | call_count | total_duration |
+---------+---------+------------+----------------+
| 1       | 2       | 2          | 70             |
| 1       | 3       | 1          | 20             |
| 3       | 4       | 4          | 999            |
+---------+---------+------------+----------------+
解释：
用户 1 和 2 打过 2 次电话，总时长为 70 (59 + 11)。
用户 1 和 3 打过 1 次电话，总时长为 20。
用户 3 和 4 打过 4 次电话，总时长为 999 (100 + 200 + 200 + 499)。
```sql
#题解一
select 
if(from_id<to_id, from_id, to_id) as person1,
if(from_id<to_id, to_id, from_id) as person2,
count(1) as call_count,
sum(duration) as total_duration
from Calls
group by person1, person2;
#题解二
select 
    from_id as person1,
    to_id as person2,
    count(1) as call_count,
    sum(duration) as total_duration
from calls
group by least(from_id, to_id),greatest(from_id, to_id);
```
【排序和分组】
银行账户概要II 简单
查找重复的电子邮箱 简单
合作过至少三次的演员和导演 简单
消费者下单频率 简单
每天的领导和合伙人 简单
上月播放的儿童适宜电影 简单
可以放心投资的国家 中等
题目及答案：一家电信公司想要投资新的国家。该公司想要投资的国家是:  该国的平均通话时长要严格地大于全球平均通话时长。
示例 1:

输入：
Person 表：
+----+----------+--------------+
| id | name     | phone_number |
+----+----------+--------------+
| 3  | Jonathan | 051-1234567  |
| 12 | Elvis    | 051-7654321  |
| 1  | Moncef   | 212-1234567  |
| 2  | Maroua   | 212-6523651  |
| 7  | Meir     | 972-1234567  |
| 9  | Rachel   | 972-0011100  |
+----+----------+--------------+
Country 表:
+----------+--------------+
| name     | country_code |
+----------+--------------+
| Peru     | 051          |
| Israel   | 972          |
| Morocco  | 212          |
| Germany  | 049          |
| Ethiopia | 251          |
+----------+--------------+
Calls 表:
+-----------+-----------+----------+
| caller_id | callee_id | duration |
+-----------+-----------+----------+
| 1         | 9         | 33       |
| 2         | 9         | 4        |
| 1         | 2         | 59       |
| 3         | 12        | 102      |
| 3         | 12        | 330      |
| 12        | 3         | 5        |
| 7         | 9         | 13       |
| 7         | 1         | 3        |
| 9         | 7         | 1        |
| 1         | 7         | 7        |
+-----------+-----------+----------+
输出：
+----------+
| country  |
+----------+
| Peru     |
+----------+
解释：
国家 Peru 的平均通话时长是 (102 + 102 + 330 + 330 + 5 + 5) / 6 = 145.666667
国家 Israel 的平均通话时长是 (33 + 4 + 13 + 13 + 3 + 1 + 1 + 7) / 8 = 9.37500
国家 Morocco 的平均通话时长是 (33 + 4 + 59 + 59 + 3 + 7) / 6 = 27.5000 
全球平均通话时长 = (2 * (33 + 4 + 59 + 102 + 330 + 5 + 13 + 3 + 1 + 7)) / 20 = 55.70000
所以, Peru 是唯一的平均通话时长大于全球平均通话时长的国家, 也是唯一的推荐投资的国家.
```sql
select c.name as country
from Country c, Person p, Calls cc
where (cc.caller_id=p.id or cc.callee_id=p.id) and left(p.phone_number,3)=c.country_code
group by c.country_code
having avg(cc.duration) > (select avg(duration) from Calls);
```

【高级查询和连接】
连续空余座位 简单
每个产品在不同商店的价格 简单
直线上的最近距离 简单
丢失信息的雇员 简单
页面推荐 中等
树节点 中等
游戏玩法分析III 中等
大满贯数量 中等
应该被禁止的Leetflex账户 中等

```sql
SELECT DISTINCT a.account_id AS account_id  -- 封他！
FROM LogInfo a, LogInfo b
WHERE a.account_id = b.account_id  -- 某个用户
    AND a.ip_address != b.ip_address -- 异地登陆
    AND a.logout <= b.logout  -- 其中一个还没下线
    AND b.login <= a.logout  -- 另一个就登上来了
;
```
【子查询】
院系无效的学生 简单
求团队人数 简单
游戏玩法分析II 简单
部门工资最高的员工 中等
```sql
#题解一
select d.name as Department, 
t.name as Employee, t.salary as Salary
from (
    select name, salary, departmentId,
    rank() over (partition by departmentId order by salary desc) as ranking
    from Employee
) t, Department d
where t.departmentId=d.id and t.ranking=1
#题解二
SELECT
	Department.NAME AS Department,
	Employee.NAME AS Employee,
	Salary
FROM
	Employee,
	Department
WHERE
	Employee.DepartmentId = Department.Id 
	AND (Employee.DepartmentId, Salary)
    IN (SELECT DepartmentId, max(Salary)
        FROM Employee
        GROUP BY DepartmentId)
```
每件商品的最新订单 中等
最近的三笔订单 中等
解答：写一个解决方案，找到每个用户的最近三笔订单。如果用户的订单少于 3 笔，则返回他的全部订单。
返回的结果按照 customer_name 升序 排列。如果有相同的排名，则按照 customer_id 升序 排列。如果排名还有相同，则按照 order_date 降序 排列。
示例 1:

输入：
Customers
+-------------+-----------+
| customer_id | name      |
+-------------+-----------+
| 1           | Winston   |
| 2           | Jonathan  |
| 3           | Annabelle |
| 4           | Marwan    |
| 5           | Khaled    |
+-------------+-----------+

Orders
+----------+------------+-------------+------+
| order_id | order_date | customer_id | cost |
+----------+------------+-------------+------+
| 1        | 2020-07-31 | 1           | 30   |
| 2        | 2020-07-30 | 2           | 40   |
| 3        | 2020-07-31 | 3           | 70   |
| 4        | 2020-07-29 | 4           | 100  |
| 5        | 2020-06-10 | 1           | 1010 |
| 6        | 2020-08-01 | 2           | 102  |
| 7        | 2020-08-01 | 3           | 111  |
| 8        | 2020-08-03 | 1           | 99   |
| 9        | 2020-08-07 | 2           | 32   |
| 10       | 2020-07-15 | 1           | 2    |
+----------+------------+-------------+------+
输出：
+---------------+-------------+----------+------------+
| customer_name | customer_id | order_id | order_date |
+---------------+-------------+----------+------------+
| Annabelle     | 3           | 7        | 2020-08-01 |
| Annabelle     | 3           | 3        | 2020-07-31 |
| Jonathan      | 2           | 9        | 2020-08-07 |
| Jonathan      | 2           | 6        | 2020-08-01 |
| Jonathan      | 2           | 2        | 2020-07-30 |
| Marwan        | 4           | 4        | 2020-07-29 |
| Winston       | 1           | 8        | 2020-08-03 |
| Winston       | 1           | 1        | 2020-07-31 |
| Winston       | 1           | 10       | 2020-07-15 |
+---------------+-------------+----------+------------+
解释：
Winston 有 4 笔订单, 排除了 "2020-06-10" 的订单, 因为它是最老的订单。
Annabelle 只有 2 笔订单, 全部返回。
Jonathan 恰好有 3 笔订单。
Marwan 只有 1 笔订单。
结果表我们按照 customer_name 升序排列，customer_id 升序排列，order_date 降序排列。
```sql
select c.name as customer_name, c.customer_id,
t.order_id, t.order_date
from(
select order_id, order_date, customer_id,
rank() over (partition by customer_id order by order_date desc) as ranking from Orders) t, Customers c
where c.customer_id=t.customer_id and ranking <=3
order by c.name asc, c.customer_id asc, t.order_date desc;
```
每天的最大交易 中等
【高级主题：窗口函数和公共表表达式（CTE）】
项目员工III 中等
找到连续区间的开始和结束数字 中等
每位顾客最经常订购的商品 中等
访问日期之间最大的空档期 中等
向公司CEO汇报工作的所有人 中等
查找成绩处于中游的学生 困难
示例 1：
输入：
Student 表：
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 1           | Daniel        |
| 2           | Jade          |
| 3           | Stella        |
| 4           | Jonathan      |
| 5           | Will          |
+-------------+---------------+
Exam 表：
+------------+--------------+-----------+
| exam_id    | student_id   | score     |
+------------+--------------+-----------+
| 10         |     1        |    70     |
| 10         |     2        |    80     |
| 10         |     3        |    90     |
| 20         |     1        |    80     |
| 30         |     1        |    70     |
| 30         |     3        |    80     |
| 30         |     4        |    90     |
| 40         |     1        |    60     |
| 40         |     2        |    70     |
| 40         |     4        |    80     |
+------------+--------------+-----------+
输出：
+-------------+---------------+
| student_id  | student_name  |
+-------------+---------------+
| 2           | Jade          |
+-------------+---------------+
解释：
对于测验 1: 学生 1 和 3 分别获得了最低分和最高分。
对于测验 2: 学生 1 既获得了最高分, 也获得了最低分。
对于测验 3 和 4: 学生 1 和 4 分别获得了最低分和最高分。
学生 2 和 5 没有在任一场测验中获得了最高分或者最低分。
因为学生 5 从来没有参加过任何测验, 所以他被排除于结果表。
由此, 我们仅仅返回学生 2 的信息。
```sql
#超级简单，开窗函数，把成绩正着排一下，再倒着排一下，只要这两列都不是1，那就是中间
select t1.student_id,s.student_name
from
(
select *,
if(dense_rank() over(partition by exam_id order by score desc)=1,1,0) d_rank,
if(dense_rank() over(partition by exam_id order by score )=1,1,0) a_rank
from Exam
) t1 left join Student s on t1.student_id =s.student_id
group by t1.student_id
having sum(d_rank)=0 and sum(a_rank)=0
order by student_id;
```
寻找没有被执行的任务对 困难
题目与解答：编写解决方案报告没有被执行的（主任务，子任务）对，即没有被执行的（task_id, subtask_id）。以任何顺序返回即可。
示例 1：
输入：
Tasks 表:
+---------+----------------+
| task_id | subtasks_count |
+---------+----------------+
| 1       | 3              |
| 2       | 2              |
| 3       | 4              |
+---------+----------------+
Executed 表:
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 2          |
| 3       | 1          |
| 3       | 2          |
| 3       | 3          |
| 3       | 4          |
+---------+------------+
输出：
+---------+------------+
| task_id | subtask_id |
+---------+------------+
| 1       | 1          |
| 1       | 3          |
| 2       | 1          |
| 2       | 2          |
+---------+------------+
解释：
Task 1 被分成了 3 subtasks (1, 2, 3)。只有 subtask 2 被成功执行, 所以我们返回 (1, 1) 和 (1, 3) 这两个主任务子任务对。
Task 2 被分成了 2 subtasks (1, 2)。没有一个subtask被成功执行, 因此我们返回(2, 1)和(2, 2)。
Task 3 被分成了 4 subtasks (1, 2, 3, 4)。所有的subtask都被成功执行，因此对于Task 3,我们不返回任何值。
```sql
#1.用recursive列出每个task的全部subtask_id。这里把subtasks_count就是最大的subtask_id，然后往下减1直到subtask_id是1就行了
#2.上面的table left join Executed，然后Executed.subtask_id 是null的就是所求结果
with recursive t(task_id, subtask_id) as (
    SELECT task_id, subtasks_count FROM Tasks
    UNION ALL
    SELECT task_id, subtask_id-1 FROM t where subtask_id-1>0
)
SELECT * FROM t left join Executed using(task_id, subtask_id) 
WHERE Executed.subtask_id is null 
ORDER BY task_id, subtask_id;
```
报告系统状态的连续日期 困难
题目与解答：系统 每天 运行一个任务。每个任务都独立于先前的任务。任务的状态可以是失败或是成功。
编写解决方案找出 2019-01-01 到 2019-12-31 期间任务连续同状态 period_state 的起止日期（start_date 和 end_date）。即如果任务失败了，就是失败状态的起止日期，如果任务成功了，就是成功状态的起止日期。
最后结果按照起始日期 start_date 排序。
示例 1：

输入：
Failed table:
+-------------------+
| fail_date         |
+-------------------+
| 2018-12-28        |
| 2018-12-29        |
| 2019-01-04        |
| 2019-01-05        |
+-------------------+
Succeeded table:
+-------------------+
| success_date      |
+-------------------+
| 2018-12-30        |
| 2018-12-31        |
| 2019-01-01        |
| 2019-01-02        |
| 2019-01-03        |
| 2019-01-06        |
+-------------------+
输出：
+--------------+--------------+--------------+
| period_state | start_date   | end_date     |
+--------------+--------------+--------------+
| succeeded    | 2019-01-01   | 2019-01-03   |
| failed       | 2019-01-04   | 2019-01-05   |
| succeeded    | 2019-01-06   | 2019-01-06   |
+--------------+--------------+--------------+
解释：
结果忽略了 2018 年的记录，因为我们只关心从 2019-01-01 到 2019-12-31 的记录
从 2019-01-01 到 2019-01-03 所有任务成功，系统状态为 "succeeded"。
从 2019-01-04 到 2019-01-05 所有任务失败，系统状态为 "failed"。
从 2019-01-06 到 2019-01-06 所有任务成功，系统状态为 "succeeded"。
```sql
本题最关键的一步是要找到同状态连续的时间记录，也就是要将连续的时间分到同一个组内，然后只需要在组内找到最小和最大的时间即可。

首先处理 Succeeded 表，一个比较简单的想法是给所有的记录分配一个 id，连续的时间 id 相同。使用 pre_date 表示上一条记录的时间，如果当前时间和 pre_date 的时间相差为 1，那么他们是连续的时间，id 相同，否则，当前记录的 id 要和上一个记录 id 不同，这里可以使用 id + 1 表示。

使用 DATEDIFF 计算两条记录的时间差。并将 pre_date 设置为当前时间，供下一次计算使用。
DATEDIFF(@pre_date, @pre_date := success_date)
使用 IF 判断当前记录的 id。
IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id+1)
使用上面的方法我们可以给 Succeeded 表的每一条记录添加一个 id。然后我们就可以使用 GROUP BY 将 id 相同的分到一组，计算最小和最大时间。

SELECT period_state, MIN(date) as start_date, MAX(date) as end_date
FROM (
    SELECT
        success_date AS date,
        "succeeded" AS period_state,
        IF(DATEDIFF(@pre_date, @pre_date := success_date) = -1, @id, @id := @id+1) AS id 
    FROM Succeeded, (SELECT @id := 0, @pre_date := NULL) AS temp
    UNION
    SELECT
        fail_date AS date,
        "failed" AS period_state,
        IF(DATEDIFF(@pre_date, @pre_date := fail_date) = -1, @id, @id := @id+1) AS id 
    FROM Failed, (SELECT @id := 0, @pre_date := NULL) AS temp
) T  WHERE date BETWEEN "2019-01-01" AND "2019-12-31"
GROUP BY T.id
ORDER BY start_date ASC;
```
