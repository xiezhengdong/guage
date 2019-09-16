MYSQL介绍：
        数据库介绍：
            数据库是⽤来存储数据的, 数据是不是直接存储在数据库中?不是的, 数据库中还有⼀个结构, 叫做表, 表中中存储的才是数据。
    数据库的三层模型：
                １．层次模型
                ２．网状模型
                ３．关系模型
            在这里，我最主要想讲的是关系模型，因为现在的主流数据库都是关系模型。
           特点:
1. 每张表都是独⽴的, 没有导航结构
2. 表于表之间会建⽴公共字段, 也就将两张表之间建⽴了关系
注意: 公共的字段名可以不⼀样, 但是数据类型必须相同(数据类型相同的不⼀定是公共字段), 两个字段的含义必须也要⼀致.
关系型数据库, 解决了数据的完整性, 也解决导航问题, 但是带来的是低效率 
            
行，列，字段的属性：
        1. ⼀⾏就是⼀条记录也是⼀条数据
        2. ⼀列就是⼀个字段, 也是表的⼀个属性
        3. 字段的属性: 是⽤来描述这个列的功能
        
Ｌinux数据库的开启和连接：
        开启数据库服务：
                1. Ubuntu : service mysql start|stop|restart|reload|status
                2. Deepin : systemctl stop|start mysqld
                3. CentOS7 : systemctl stop|start mysqld
                4. CentOS6 : service mysqld start|stop|restart|reload|status

        连接数据库：
            mysql -h localhost -u root -p密码　-P端口
            1. -h : host(ip地址) localhost = 127.0.0.1
            2. -u : username(⽤户账户)
            3. -p : password(密码)
            4. -P : port(端⼝, 默认端⼝3306)
        退出数据库的方法：
            1. exit
            2. quit
            3. \q
            4. 快捷键：ctrl + d
    这四种退出方法其实效果都是一样的，觉得哪个好用，就用哪一个。

    忘记密码的解决办法：
                1. 修改配置: vim /etc/my.cnf
                2. 找到 [mysqld] 在下⾯添加⼀句 skip-grant-tables
                3. 修改完重新启动
    ＳＱＬ语言，是一种结构化的查询语言，是⼀种数据库查询和程序设计语⾔，⽤于存取数据以及查询、更新和管理关系数据库系统；同时也是数据库脚本⽂件的扩展名。


       数据库的各种操作如下:
            1.创建数据库
                create database [if not exists] `数据库名` charset=字符编码(utf8mb4);
            ２．查看数据库
                show databases;

            3.选择数据库
                use ｀数据库的名字｀
            ４．修改数据库
                alter database `数据库名｀　charset=字符集;
            5.删除数据库
                drop database `数据库的名字｀

 表的各种操作如下：
            １．表的创建
         create table [if not exists] `表的名字`(
         id int not null auto_increment primary key comment '主键',
         account char(255) comment '⽤户名' default 'admin',
         pwd varchar(65535) comment '密码' not null
        ) engine=myisam charset=utf8mb4;
        在这里，如果字符集不指定，默认继承库的字符集
        engine 默认innodb
            
            ２．查看所有的表
            要先选择数据库之后，我们才能查表
            show tables;
        
            3.删除表
            删除表必须在数据库中进行删除
            
            ４．显示建表结构
             desc ｀表名｀;

            5.修改表
                -- 修改表的名称
                    alter table `old_name` rename `new_name`;
                    -- 增加⼀个新的字段
                    alter table `table_name` add `field_name` 数据类型 属性;
                    -- 将某个字段添加在第⼀个位置
                    复制表
                    1. create table 表名 select * from 要被复制的表名 ;
                    特点: 把数据给复制过来了, 但是没有复制主键
                    2. create table 表名 like 要被复制的表名 ;
                    特点: 复制所有表结构, 但是不复制数据
                    数据可以单独复制
                    insert into 表名 select * from 要被复制的表名 ;
                    CURD 语句的基本使⽤
                    insert(插⼊)
                    alter table `table_name` add `field_name` 数据类型 属性 first;
                    -- 添加在某⼀个字段之后
                    alter table `table_name` add `field_name` 数据类型 属性 after 指定字段;
                    -- 修改字段的属性
                    alter table `table_name` modify `字段名` 数据类型 属性;
                    -- 修改字段的名称
                    alter table `表名` change `原字段名` `新的字段名` 数据类型 属性;
                    -- 修改字段的位置
                    alter table `表名` change `原字段名` `新的字段名` 数据类型 after `指定字段`;
                    -- 修改表的引擎
                    alter table `表名` engine = innodb|myisam;
                    -- 移动表 到指定的数据库
                    alter table `表名` rename to 数据库名.表名;
                    
            复制表：
                1. create table 表名 select * from 要被复制的表名 ;
                特点: 把数据给复制过来了, 但是没有复制主键
                2. create table 表名 like 要被复制的表名 ;
                特点: 复制所有表结构, 但是不复制数据
        当然，数据可以单独复制，格式如后面：insert into 表名 select * from 要被复制的表名 ;
        
       
        alter table `table_name` add `field_name` 数据类型 属性 first;
        -- 添加在某⼀个字段之后
        alter table `table_name` add `field_name` 数据类型 属性 after 指定字段;
        -- 修改字段的属性
        alter table `table_name` modify `字段名` 数据类型 属性;
        -- 修改字段的名称
        alter table `表名` change `原字段名` `新的字段名` 数据类型 属性;
        -- 修改字段的位置
        alter table `表名` change `原字段名` `新的字段名` 数据类型 after `指定字段`;
        -- 修改表的引擎
        alter table `表名` engine = innodb|myisam;
        -- 移动表 到指定的数据库
        alter table `表名` rename to 数据库名.表名;
        create table abc(
         id int primary key auto_increment comment '主键',
         username char(32) not null comment '账户',
         password char(32) not null comment '密码'
        ) engine=myisam;
        insert into abc values(null, 'admin', md5(123456)), (null, 'admin1',
        md5(123456));
        select(查询)
        update(更新)
        delete(删除)
        -- 主键字段不⽤我们考虑
        -- not null 的字段, 说明⼀定要输⼊数据
        -- ⼀次插⼊⼀⾏
        insert into `表名` set `字段`=值, `字段`=值;
        -- ⼀次插⼊多⾏
        insert into `表名`(字段1, 字段2....) values (值1, 值2...), (值1, 值2...);
        insert into `表名` values (null, 值1, 值2....), (null, 值1, 值2....);
        -- * 的位置⼀个结果集
        -- * 代表所有的字段名
        select * from `表名`;
        select 字段1, 字段2 from `表名`;
        update `表名` set `字段名`=值, `字段`=值;
        -- 在更新的时候⼀定要加上where条件
        -- where相当于if条件, 只执⾏返回结果为True的语句
        update `表名` set `字段名`=值, `字段`=值 where `字段`=值;
        update `表名` set `字段名`=值, `字段`=值 where `字段`=值 and `字段`=值;
        -- 删除表中的所有数据
        delete from `表名`;
        -- 在删除的时候⼀定要加上where条件
        -- where相当于if条件, 只执⾏返回结果为True的语句
        delete from `表名` where `字段` = 值;
        delete from `表名` where `字段` in (1, 2, 3, 4);
        -- ⼀旦数据被删除, 再次插⼊数据, ⾃增⻓的列的记录值, 从最⼤值的下⼀次开始.
        -- 在开发中, 真实数据是⽆价的, 数据是不会被删除
        -- 数据保留位置, 是为了数据恢复准备的.
        -- 删除表在重建=>清空表(在开发的时候会经常使⽤)
        truncate `表名`
        -- mysql中创建⼀个远程连接的⽤户并且授权
        -- root不可以执⾏远程连接
        grant all privileges on *.* to 'admin'@'%'identified by '123456' with grant
        option;


        
　　总结：
    　　     增
                数据库: create database `库名`;
                表: create table `表名`;
                字段: alter table `表名` add `字段名` 类型 [属性];
                数据: insert into `表名`;
                        
            删
                数据库: drop database `库名`;
                表: drop  table `表名`;
                字段: alter table `表名` drop `字段名`;
                数据: delete from `表名` where ...;
            
            改
                数据库: alter database `库名` ...;
                表: alter table `表名` ...;
                字段: alter table `表名` modify | change ...;
                数据: update `表名` set ...;
            
            查
                数据库: show database [like ...];
                表: show tables [like ...];
                字段: desc `表名`;
                数据: select * from `表名` where ...;






















