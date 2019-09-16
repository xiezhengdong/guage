    MySQL中的编码和数据类型:
            1.字符集
                常见字符集：
                        ASCII: 基于罗⻢字⺟表的⼀套字符集, 它采⽤1个字节的低7位表示字符, ⾼位始终为0。
                LATIN1: 相对于ASCII字符集做了扩展, 仍然使⽤⼀个字节表示字符, 但启⽤了⾼位, 扩展了字
                符集的表示范围。
                GB2312: 简体中⽂字符, ⼀个汉字最多占⽤2个字节
                GB: 只是所有的中⽂字符, ⼀个汉字最多占⽤2个字节
                UTF8: 国际通⽤编码, ⼀个汉字最多占⽤3个字节
                UTF8MB4: 国际通⽤编码, 在utf8的基础上加强了对新⽂字识别, ⼀个汉字最多占⽤4个字节

            ２．字符集在什么时候发挥自己的作用：
                            1. 保存数据的时候需要使⽤字符集
                            2. 数据传输的时候也需要使⽤字符集
                            3. 在存续的时候使⽤字符集
                            1. 在MySQL的服务器上, 在数据库中, 在表的使⽤上, 在字段的设置上.
                            2. 在服务器安装的时候, 可以指定默认的字符集

                查看当前mysql系统⽀持的字符集：

                                 show variables like 'character_%';
                修改当前的 mysql 系统的字符集编码：
                                set names gbk;
                指定修改：
                        set character_set_client = gbk;
                        set character_set_results = gbk;
    校对集：
        在某⼀种字符集下, 为了使字符之间可以互相⽐较, 让字符和字符形成⼀种关系的集合, 称之为校对集。
        ⽐如说 ASCII 中的 a 和 B, 如果区分⼤⼩写 a > B, 如果不区分 a < B;
        不同字符集有不同的校对规则, 命名约定：以其相关的字符集名开始, 通常包括⼀个语⾔名, 并且以
        _ci 、 _cs 或 _bin 结束。
        _ci : ⼤⼩写不敏感
        _cs : ⼤⼩写敏感
        _bin : binary collation ⼆元法, 直接⽐较字符的编码, 可以认为是区分⼤⼩写的, 因为字符集
        中'A'和'a'的编码显然不同。
        
        show character set; -- 查看字符集 和 校对集
        show collation; -- 显示所有的校对集
        

    MySQL的数据类型：
         整型：
            一个无符号数一定是非负数
                create table t3(
                 age tinyint unsigned
                )
            显示宽度 (zerofill)
            整型显示宽度, 位数不⾜时⽤ 0 填充
                 create table t4(
                 id int(10) zerofill primary key auto_increment,
                 name char(32)
                );
                insert into t4 values(12345, '5个');

            浮点型：
                定点数的位数更加⻓
                    使⽤⽅式:
                    float(M,D)
                    double(M,D)
                    decimal(M,D)
                    M 是⽀持多少个⻓度, D 是⼩数点后⾯的位数
                    
                    create table t5 (
                         a float(10, 2),
                         b double(10, 2),
                         c decimal(10, 2)
                        );
                        
                        
       字符串类型：
            

    枚举：
         枚举(enum)
            多选⼀的时候使⽤的⼀种数据类型
            在前端使⽤单选框的时候, 枚举类型可以发挥作⽤
            枚举类型的优点:
            1. 限制值
            2. 节省空间
            3. 运⾏效率⾼
            
        create table t6(
         name varchar(32),
         sex enum('男','⼥','保密') default 3
        );
        -- 枚举类型的计数默认从1开始
        insert into t6 set name='王宝强',sex=1;

        集合(set)
    SET最多可以有64个不同的成员。类似于复选框, 有多少可以选多少。
        create table t7 (
         name varchar(32),
         hobby set('吃','睡','玩','喝','抽')
        );
        insert into t7 values('张三','睡,抽,玩,吃,喝');
        insert into t7 values('李四','睡,抽');

    时间类型：
         datetime：
                create table datetime_test (
                     create_at datetime
                    );
                    insert into datetime_test values('2019-4-2 16:54:00');

        3.timestamp 时间戳类型
        时间戳类型在显示⽅⾯和datetime是⼀样的, 在存储上不⼀样
        范围从 1970-1-1 0:0:0 到 2038-1-19 11:14:07
        时间戳使⽤ 4 个字节表示
        该值⼤⼩与存储的位⻓有关: 2 ** (4 * 8 - 1)
        
            create table timestamp_test (
             create_time timestamp
            );
            insert into timestamp_test values(now());
            insert into timestamp_test values('2038-1-19 11:14:07');
            insert into timestamp_test values('2038-1-19 11:14:08'); -- 错误
            
         布尔型
        mysql中的bool类型也是1和0
            create table `bool`(
                 cond boolean
                );
                insert into `bool` set cond=True; -- 成功
                insert into `bool` set cond=False; -- 成功
                insert into `bool` set cond=1; -- 成功
                insert into `bool` set cond='True'; -- 失败
             列的属性
            插⼊的值是否可以为空
            null : 是可以为空,默认不写
            not null : 不可以为空,如果插⼊的时候,摸个字段的值为空,则报错


            default
                默认值⼀般是和null做搭配的

            auto_increment
                    ⾃动增⻓的列
                    默认从 1 开始
                    常配合主键使⽤的

            primary key
                    主键⼀般是唯⼀的标识
                    特性:不能为空,也不能重复,⼀张表当中只可以拥有⼀个主键

            unique
                唯⼀键,保证列当中的每⼀个数据都不重复
                邮箱不可以重复,⼿机号不可以重复

            comment
                注释: 给开发者看的, ⼀般⽤来对相应字段进⾏说明


             SQL注释
                单⾏注释: -- 你好
                多⾏注释: /* 巴拉巴拉 */
                MySQL 独有的单⾏注释: # 哈哈哈哈













        


















                    
                                
                                