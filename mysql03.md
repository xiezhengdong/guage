        数据库的查询：
             SELECT : 字段表达式
                    SELECT 既可以做查询, 也可以做输出
                    select unix_timestamp(); -- 显示Unix时间戳
                    select id, name from student;

              FROM ⼦句
                    语法: select 字段 from 表名;
                    FROM 后⾯是数据源, 数据源可以写多个, 数据源⼀般是表明, 也可以是其他查询的结果
                     WHERE ⼦句: 按指定条件过滤
                        语法: select 字段 from 表名 where 条件;
                        WHERE 是做条件查询, 只返回结果为 True 的数据
                
                    例子：select name from student where city = '上海';

                    空值判断: is null | is not null
                            select `name` from `student` where `description` is null;
                            select `name` from `student` where `description` is not null;

                    范围判断: between ... and ...| not between
                            select id, math from score where math between 60 and 70;
                            select id, math from score where math not between 60 and 70;
                            select * from score where math>=80 and english<=60;

             GROUP BY : 分组查询：
                        按照某⼀字段进⾏分组, 会把该字段中值相同的归为⼀组, 将查询的结果分类显示, ⽅便统计。
                        如果有 WHERE 要放在 WHERE 的后⾯
                        语法: select 字段 from 表名 group by 分组字段;
        
                    select sex, count(id) from student group by sex;
                    -- 在group将需要的结果通过 “聚合函数” 拼接
                    select sex, group_concat(name) from student group by sex;
                    -- 添加where语句
                    -- 按性别分组, 将上海地区的男⽣⼥⽣姓名连接起来
                    select sex, group_concat(name) from student where city='上海' group by sex;

             HAVING：
                        HAVING 与 WHERE 在 SQL 中增加 HAVING ⼦句原因是， WHERE 关键字⽆法与聚合函数⼀起使⽤。
                        语法: SELECT 字段 FROM 表名 HAVING 条件;
                        WHERE : 后⾯不能加上聚合函数,只能写在.数据源的后⾯
                        HAVING : 条件字段必须要在结果集中出现, HAVING 可以写在 GROUP BY 的后⾯
                        例子：
                            取出每个城市中满⾜最⼩出⽣年份⼤于1995的
                            select city, group_concat(birthday) from student group by city having　min(birthday) > '1995-1-1';
                                要注意的是：当使用having的时候，having后面的字段，必须在前面也要存在才可以，要不然会报错的。
             ORDER BY : 按字段排序
                ORDER BY 主要作⽤是排序
                ORDER BY 写在 GROUPBY 后⾯ ,如果有 HAVING 也要写在 HAVING 的后⾯
                语法: select 字段 from 表名 order by 排序字段 asc|desc;
                分为升序 asc 降序 desc, 默认 asc (可以不写)
                    例子：select * from student order by age desc;

             LIMIT : 限制取出数量
                    ３种格式如下：select 字段 from 表名 limit m; -- 从第 1 ⾏到第 m ⾏
                                select 字段 from 表名 limit m, n; -- 从第 m ⾏开始，往下取 n ⾏
                                select 字段 from 表名 limit m offset n; -- 跳过前 n ⾏, 取后⾯的 m ⾏。

            DISTINCT : 去重
                    例子：select distinct city from student;
             dual表：
                dual 是⼀个虚拟表, 仅仅为了保证 select ... from ... 语句的完整性


        函数：
            聚合函数：
                    Name 　　　　　　　　　　　　　　　　　　　　Description
                    AVG() 　　　　　　　　　　　　　　　　　　　返回参数的平均值
                    BIT_AND() 　　　　　　　　　　　　　　　　　按位返回AND
                    BIT_OR() 　　　　　　　　　　　　　　　　　　按位返回OR
                    BIT_XOR() 　　　　　　　　　　　　　　　　　　按位返回异或
                    COUNT() 　　　　　　　　　　　　　　　　　　返回返回的⾏数
                    COUNT(DISTINCT) 　　　　　　　　　　　　　　返回许多不同值的计数
                    GROUP_CONCAT() 　　　　　　　　　　　　　　　　返回连接的字符串
                    JSON_ARRAYAGG() 　　　　　　　　　　　　　　将结果集作为单个JSON数组返回
                    JSON_OBJECTAGG() 　　　　　　　　　　　　　　将结果集作为单个JSON对象返回
                    MAX() 　　　　　　　　　　　　　　　　　　　　返回最⼤值
                    MIN() 　　　　　　　　　　　　　　　　　　　　返回最⼩值
                    STD() 　　　　　　　　　　　　　　　　　　　　　返回样本的标准差
                    STDDEV() 　　　　　　　　　　　　　　　　　　　返回样本的标准差
                    STDDEV_POP() 　　　　　　　　　　　　　　　　　返回样本的标准差
                    STDDEV_SAMP() 　　　　　　　　　　　　　　　　　　返回样本标准差
                    SUM() 　　　　　　　　　　　　　　　　　　　　　　归还总和
                    VAR_POP() 　　　　　　　　　　　　　　　　　　　返回样本的标准差异
                    VAR_SAMP() 　　　　　　　　　　　　　　　　　　　返回样本⽅差
                    VARIANCE() 　　　　　　　　　　　　　　　　　　　　返回样本的标准差异
             

        多表查询：
            UNION联合查询：
                UNION 操作符⽤于合并两个或多个 SELECT 语句的结果集。
                union要求:
                1. 两边 select 语句的字段数必须⼀样
                2. 两边可以具有不同数据类型的字段
                3. 字段名默认按照左边的表来设置
            用法实例：
                      SELECT column_name(s) FROM table1
                        UNION
                        SELECT column_name(s) FROM table2;

        INNER JOIN : 内连接 (交集)：
                                   INNER JOIN 关键字在表中存在⾄少⼀个匹配时返回⾏。
                                    语法：
                                        FROM 表1 INNER JOIN 表2
                                        ON 表1.字段=表2.字段;
                                        -- 或：
                                        SELECT column_name(s)
                                        FROM table1 JOIN table2
                                        ON table1.column_name=table2.column_name;
                                       

                                    LEFT JOIN : 左连接
                                    LEFT JOIN 关键字从左表（table1）返回所有的⾏，即使右表（table2）中没有匹配。如果右表中没有匹配，则结果为 NULL。
                                    语法：
                                    SELECT column_name(s) FROM table1
                                    UNION
                                    SELECT column_name(s) FROM table2;
                                    SELECT 字段
                                    FROM 表1 INNER JOIN 表2
                                    ON 表1.字段=表2.字段;
                                    -- 或：
                                    SELECT column_name(s)
                                    FROM table1 JOIN table2
                                    ON table1.column_name=table2.column_name;

                                   RIGHT JOIN : 右连接：
                                        RIGHT JOIN 关键字从右表（table2）返回所有的⾏，即使左表（table1）中没有匹配。如果左表中没有匹配，则结果为 NULL。
                                    语法：SELECT column_name(s)
                                        FROM table1
                                        RIGHT JOIN table2
                                        ON table1.column_name=table2.column_name;
                                        -- 或：
                                        SELECT column_name(s)
                                        FROM table1
                                        RIGHT OUTER JOIN table2
                                        ON table1.column_name=table2.column_name;
    子查询:
        查询的语句中还有⼀个查询
         select name from student where id in (select id from score where math > 10);                                  


















