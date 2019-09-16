## 数据库⾼级特性

## 1.存储引擎

存储引擎就是如何存储数据、如何为数据建⽴索引和如何更新、查询数据等技术的实现⽅法。
MySQL 默认⽀持多种存储引擎，以适⽤于不同领域 的数据库应⽤需要，⽤户可以通过选择使⽤不同的
存储引擎提⾼应⽤的效率，提供灵活的存储。

如何查看当前的存储引擎：

`show variables like '%storage_engine';`
`show engines;`

### MySQL 常⽤的存储引擎如下：

![1567819869263](C:\Users\32568\AppData\Roaming\Typora\typora-user-images\1567819869263.png)

1. InnoDB
事务型数据库的⾸选引擎，⽀持事务安全表（ACID），⽀持⾏锁定和外键，InnoDB是默认的
MySQL引擎。
InnoDB主要特性有：
1. InnoDB 给 MySQL 提供了具有提交、回滚、崩溃恢复能⼒的事务安全存储引擎。
2. InnoDB 是为处理巨⼤数据量的最⼤性能设计。它的 CPU 效率⽐其他基于磁盘的关系型数据
库引擎⾼。
3. InnoDB 存储引擎⾃带缓冲池，可以将数据和索引缓存在内存中。
4. InnoDB ⽀持外键完整性约束。
5. InnoDB 被⽤在众多需要⾼性能的⼤型数据库站点上
show variables like '%storage_engine';
show engines;
6. InnoDB ⽀持⾏级锁

2. MyISAM

  MyISAM 基于 ISAM 存储引擎，并对其进⾏扩展。它是在Web、数据仓储和其他应⽤环境下最常使
  ⽤的存储引擎之⼀。MyISAM 拥有较⾼的插⼊、查询速度，但不⽀持事物。

  但是，它只⽀持表锁。

3. MEMORY
MEMORY 存储引擎将表中的数据存储到内存中，为查询和引⽤其他表数据提供快速访问。

### 存储引擎的选择

⼀般来说，对插⼊和并发性能要求较⾼的，或者需要外键，或者需要事务⽀持的情况下，需要选择
InnoDB，
插⼊较少，查询较多的场景，优先考虑 MyISAM。

### InnoDB 和 MyISAM 在⽂件⽅⾯的区别

1. InnoDB 将⼀张表存储为两个⽂件
demo.frm -> 存储表的结构和索引
demo.ibd -> 存储数据，ibd 存储是有限的, 存储不⾜⾃动创建 ibd1, ibd2
InnoDB 的⽂件创建在对应的数据库中, 不能任意的移动
create table abc (
name char(10)
) engine=MyISAM charset=utf8;
create table xyz (
name char(10)
) engine=InnoDB charset=utf8;
2. MyISAM 将⼀张表存储为三个⽂件
demo.frm -> 存储表的结构
demo.myd -> 存储数据
demo.myi -> 存储表的索引
MyISAM 的⽂件可以任意的移动

# ⼆、索引

索引就是为特定的 mysql 字段进⾏⼀些特定的算法排序，⽐如⼆叉树的算法和哈希算法，哈希算法是通
过建⽴特征值，然后根据特征值来快速查找。
MySQL 索引的建⽴对于 MySQL 的⾼效运⾏是很重要的，索引可以⼤⼤提⾼MySQL的检索速度。

### 索引的创建原则

1. 适合⽤于频繁查找的列
2. 适合经常⽤于条件判断的列
3. 适合经常由于排序的列
4. 不适合数据不多的列
5. 不适合很少查询的列

#### 创建索引

```
create table 表 (
id int not null,
username varchar(16) not null,
index 索引名(字段名(⻓度))
);
```

### 后期添加索引

```
create index `索引名` on 表名(字段名(⻓度));
```

### 删除索引

```
drop index [索引名] on 表;
```

### 查看索引

```
show index from table_name;
```

# 关系与外键

关系
⼀对⼀
在 A 表中有⼀条记录，在 B 表中同样有唯⼀条记录相匹配
⽐如: 学⽣表和成绩表
⼀对多 / 多对⼀
在 A 表中有⼀条记录，在 B 表中有多条记录⼀直对应
⽐如: 博客中的⽤户表和⽂章表
多对多
A 表中的⼀条记录有多条 B 表数据对应, 同样 B 表中⼀条数据在 A 表中也有多条与之对应
⽐如: 博客中的收藏表

### 外键

外键是⼀种约束。他只是保证数据的⼀致性，并不能给系统性能带来任何好处。
建⽴外键时，都会在外键列上建⽴对应的索引。外键的存在会在每⼀次数据插⼊、修改时进⾏约束检
查，如果不满⾜外键约束，则禁⽌数据的插⼊或修改，这必然带来⼀个问题，就是在数据量特别⼤的情
况下，每⼀次约束检查必然导致性能的下降。

#####  添加外键

-- 为 user 和 userinfo 建⽴关联的外键
alter table userinfo add constraint fk_user_id foreign key(id) references
user(id);
-- 建⽴⽤户与组的外键约束
alter table `user` add `gid` int unsigned;
alter table `user` add constraint `fk_group_id` foreign key(`gid`)
references `group`(`id`);
-- 建⽴⽤户、商品、订单的外键约束
alter table `order` add constraint `fk_user_id` foreign key(`uid`)
references `user`(`id`);
alter table `order` add constraint `fk_prod_id` foreign key(`pid`)
references `product`(`id`);