# ⼀、事务

​     事务主要⽤于处理操作量⼤、复杂度⾼、并且关联性强的数据。
⽐如说, 在⼈员管理系统中, 你删除⼀个⼈员, 你即需要删除⼈员的基本资料, 也要删除和该⼈员相关的信
息, 如信箱, ⽂章等等, 这样, 这些数据库操作语句就构成⼀个事务！
在 MySQL 中只有 Innodb 存储引擎⽀持事务。
事务处理可以⽤来维护数据库的完整性, 保证成批的 SQL 语句要么全部执⾏, 要么全部不执⾏。主要针对
insert, update, delete 语句⽽设置

2. ### 事务四⼤特性

在写⼊或更新资料的过程中, 为保证事务 (transaction) 是正确可靠的, 所必须具备的四个特性 (ACID)：
1. 原⼦性 (Atomicity) ：
事务中的所有操作, 要么全部完成, 要么全部不完成, 不会结束在中间某个环节。
事务在执⾏过程中发⽣错误, 会被回滚 (Rollback) 到事务开始前的状态, 就像这个事务从来没
有执⾏过⼀样。
2. ⼀致性 (Consistency)：
在事务开始之前和事务结束以后, 数据库的完整性没有被破坏。
这表示写⼊的资料必须完全符合所有的预设规则, 这包含资料的精确度、串联性以及后续数据库可
以⾃发性地完成预定的⼯作。
3. 隔离性 (Isolation)：
数据库允许多个并发事务同时对其数据进⾏读写和修改的能⼒, 隔离性可以防⽌多个事务并发执⾏
时由于交叉执⾏⽽导致数据的不⼀致。
事务隔离分为不同级别, 包括:
1. 读取未提交 (Read uncommitted)
所有事务都可以看到其他未提交事务的执⾏结果
本隔离级别很少⽤于实际应⽤，因为它的性能也不⽐其他级别好多少
该级别引发的问题是——脏读(Dirty Read)：读取到了未提交的数据
2. 读提交 (read committed)
这是⼤多数数据库系统的默认隔离级别（但不是MySQL默认的）
它满⾜了隔离的简单定义：⼀个事务只能看⻅已经提交事务做的改变
这种隔离级别出现的问题是: 不可重复读(Nonrepeatable Read)：
不可重复读意味着我们在同⼀个事务中执⾏完全相同的 select 语句时可能看到不⼀样的
结果。
导致这种情况的原因可能有：
有⼀个交叉的事务有新的commit，导致了数据的改变;
⼀个数据库被多个实例操作时,同⼀事务的其他实例在该实例处理其间可能会有新
的commit
3. 可重复读 (repeatable read)
这是MySQL的默认事务隔离级别
它确保同⼀事务的多个实例在并发读取数据时，会看到同样的数据⾏
此级别可能出现的问题: 幻读(Phantom Read)：当⽤户读取某⼀范围的数据⾏时，另⼀
个事务⼜在该范围内插⼊了新⾏，当⽤户再读取该范围的数据⾏时，会发现有新的“幻
影” ⾏
InnoDB 通过多版本并发控制 (MVCC，Multiversion Concurrency Control) 机制解决幻
读问题；
InnoDB 还通过间隙锁解决幻读问题
4. 串⾏化 (Serializable)
这是最⾼的隔离级别
它通过强制事务排序，使之不可能相互冲突，从⽽解决幻读问题。简⾔之,它是在每个读
的数据⾏上加上共享锁。MySQL锁总结
在这个级别，可能导致⼤量的超时现象和锁竞争
4. 持久性 (Durability)：
事务处理结束后, 对数据的修改就是永久的, 即便系统故障也不会丢失。

3. ### 语法与使⽤

开启事务: BEGIN 或 START TRANSACTION
提交事务: COMMIT , 提交会让所有修改⽣效
回滚: ROLLBACK , 撤销正在进⾏的所有未提交的修改
创建保存点: SAVEPOINT identifier
删除保存点: RELEASE SAVEPOINT identifier
把事务回滚到保存点: ROLLBACK TO identifier
设置事务的隔离级别: SET TRANSACTION
InnoDB 提供的隔离级别有
`READ`
`UNCOMMITTED`
`READ COMMITTED`
`REPEATABLE READ`
`SERIALIZABLE`

# ⼆、锁

锁是计算机协调多个进程或线程并发访问某⼀资源的机制。
锁保证数据并发访问的⼀致性、有效性；
锁冲突也是影响数据库并发访问性能的⼀个重要因素。
锁是Mysql在服务器层和存储引擎层的的并发控制

### 分类

⾏级锁
⾏级锁是Mysql中锁定粒度最细的⼀种锁，表示只针对当前操作的⾏进⾏加锁。
⾏级锁只有 InnoDB 引擎⽀持。
⾏级锁能⼤⼤减少数据库操作的冲突。其加锁粒度最⼩，但加锁的开销也最⼤。
特点：开销⼤，加锁慢；会出现死锁；锁定粒度最⼩，发⽣锁冲突的概率最低，并发度也最
⾼。
表级锁
表级锁是MySQL中锁定粒度最⼤的⼀种锁
对当前操作的整张表加锁，它实现简单，资源消耗较少，被⼤部分MySQL引擎⽀持。
特点：开销⼩，加锁快；不会出现死锁；锁定粒度⼤，发出锁冲突的概率最⾼，并发度最
低。

# Python操作

```
import pymysql
db = pymysql.connect(host='localhost',
user='user',
password='passwd',
db='db',
charset='utf8')
try:
with db.cursor() as cursor:
```


# 插⼊
```
sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
```


# 需要⼿动提交才会执⾏
```
db.commit()
with db.cursor() as cursor:
```


# 读取记录
```
sql = "SELECT `id`, `password` FROM `users` WHERE `email`=%s"
cursor.execute(sql, ('webmaster@python.org',))
result = cursor.fetchone()
print(result)
finally:
db.close()
```



# 数据备份与恢复

1. 备份

```
mysqldump -h localhost -u root -p123456 dbname > dbname.sql
```

2. 恢复

```
mysql -h localhost -u root -p123456 dbname < ./dbname.sql
```

