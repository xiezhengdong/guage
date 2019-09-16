    用户权限：
        首先，我们要理解linux中用户和用户组的概念，一个用户组可以有多个用户，每一个用户都有唯一的用户名，并且还会有唯一的一个uid和它对应。同样的，每一个用户组也会有一个唯一的名称，会有一个唯一的gid与之对应。
    root用户的uid 和gid都是０，如果你想查询用户名与uid,用户组与gid的对应情况，可以进入 /etc/passwd 和　/etc/group中。最后，要是想查询用户的密码信息，可以进入 /etc/shadow.

    下面介绍一下这三种格式分别代表的意义：
        １．passwd格式：root:x:0:0:root:/root:/bin/bash
                root代表用户名，x在早期的时候是记录密码的，现在已经作废了，第一个０代表uid,第二个0代表gid,接下来的一个root只是起到注释的作用，/root代表家目录，/bin/bash代表登录之后使用的shell.
        ２．shadow格式：root:$1$lrKCOpzq$IHP2BuuKxMdLaBw/:17877:0:99999:7:::
                root代表用户名，$1$lrKCOpzq$IHP2BuuKxMdLaBw代表密码，17877代表最后一次修改密码的日期，这里的单位是天数，是从1970年７月１号０点０分开始到你最后一次修改密码的天数，然后０代表密码几日内不可修改，99999代表密码有效的天数，７代表密码失效前几天内提醒用户。
        ３．group格式： wheel:x:10:bob,tom
                wheel代表的是组名，10代表的是组id(gid),bob和tom代表的是该组的成员。
    
    用户管理，即用户的添加和删除：
        １．添加用户
                useradd -mU -G 组名 -s /bin/bash 用户名
                useradd -D  显示默认配置
                    -G GROUPS : 新账户的附加组列表
                    -m : 在 /home ⽬录创建⽤户的家⽬录
                    -U : 创建与⽤户同名的组
        切记：添加完用户之后，可以对用户设置密码，可以用sudo passwd 用户名。但是在切换用户的时候，一定要牢记：如果只是用su 用户名，那么仅仅是切换用户身份，此时新用户的家目录还是以前的，要想有一个新的家目录，就要用su - 用户名。

        ２．删除用户：
                userdel -r 用户名
                    －r 删除主目录和邮件池 ，要是删除不了，就用　userdel -rf 用户名

    用户组管理，即用户组的添加，删除，修改用户属性：
        １．添加组
                groupadd 组名
                    -g GID : 为新组使⽤ GID
        ２．删除组
                groupdel -rf 组名
        3.修改用户属性
                usermod 用户名　-G 组名
                    -G　新的附加组，就是将一个用户添加到一个用户组里面
                    -a  将用户追加到上边-G中提到的附加组中，并且不从其他组中删除此用户
        
    查看登录的用户：
                who 查看谁正在登录
                w 查看谁正在登录，并在显示每个登陆⽤户正在执⾏last 查看历史登陆记录
                lastb 查看失败的登陆记录
                lastlog 查看全部⽤户最后⼀次登陆的时间
    
    文件权限：
            linux给一个文件或者目录设置了三种权限，分别是r(读），w(写），x(执行）。但是与此同时，linux又给不同身份的用户设定了对文件的不同权限，用户身份可以分为：
                                                        1. owner ⽂件拥有者
                                                        2. group 同组⼈
                                                        3. other 其他⼈
            
    使⽤ ls -l 可以看到⽂件的权限信息:
        drwxr-xr-x  2 xiezhengdong xiezhengdong   4096 8月  26 20:28  .themes
        drwx------  3 xiezhengdong xiezhengdong   4096 8月  28 08:51  .thunderbird
        drwxr-xr-x  3 xiezhengdong xiezhengdong   4096 8月  26 21:18  .var
        drwxr-xr-x  2 xiezhengdong xiezhengdong   4096 8月  26 20:28  Videos
        drwx------  5 xiezhengdong xiezhengdong   4096 8月  27 09:02  .vnc
        -rw-------  1 xiezhengdong xiezhengdong     60 8月  29 18:40  .Xauthority
        -rw-r--r--  1 xiezhengdong xiezhengdong    132 8月  26 12:27  .xinputrc
        drwxr-xr-x  2 xiezhengdong xiezhengdong   4096 8月  28 14:21  模板
根据上面的结果来看：
                第一列就是文件的权限信息，第一列的第一个字母代表这个文件是目录，还是文件，如果是d,代表是一个目录，如果是－,代表是一个文件，如果是l,代表是一个链接文件。接下来就是第一列除去第一个字母外剩下的九个字符，分为三组，三个一组，分别代表不同用户身份的权限。前三个代表owner，即用户自身，中间三个代表同一个用户组的其他用户，后面三个代表其他用户。

    权限修改：
            １．通过符号修改
                    chmod u+rwx test.txt
                    chmod g+wx test.txt
                    chmod o+x test.txt
                    chmod a-rwx test
               chmod u=rwx,g=rx,o=r test.txt  给test.txt这个文件设置权限，用户自身可读可写可执行，同组人可读可执行，其他人只能读。
            ２．通过数字修改
                     chmod 777 test.txt
                     chmod 751 test.txt
                r(读）＝＝》４
　　　　　　　　　 w(写）＝＝》２
                x(执行）＝＝》１    
                        
    修改文件拥有者：
            chown 用户名:用户组　文件　　这个只能将一个文件的拥有者改变，要想改变它的拥有者和用户组的话，要先进入那个用户组才行。如果要是想一次性改变所有文件夹和文件的话，要用-R,即　chown -R 用户名：用户组　文件
            chown ting:xiezhengdong test　即将test这个文件的拥有者改为用户ting,在xiezhengdong这个用户组下。

    文本操作：
        echo xyz : 打印⽂本
        echo -e 'a\nb\nc\nd'　原样输出，里面的\n会发生作用
        echo xyz > a.txt : 将输出的⽂本重定向到⽂件a.txt中，a.txt原有内容会被覆盖
        echo xyz >> a.txt : 将输出的⽂本追加到⽂件a.txt中，a.txt原有内容不会被覆盖
        cat ⽂件名 : 查看⽂件
        head -n N ⽂件名 : 查看⽂件的前 N ⾏
        tail -n N ⽂件名 : 查看⽂件的后 N ⾏
        less ⽂件 : 快速浏览⽂件
        按 j 向下
        按 k 向上
        按 f 向下翻屏
        按 b 向上翻屏
        按 g 到全⽂开头
        按 G 到全⽂结尾
        按 q 退出
        sort ⽂本或⽂件 : 将结果按升序排序
        sort -r ⽂本或⽂件 将结果按降序排序
        uniq 去重, 依赖排序, 常跟在 sort 后⾯使⽤
        awk '{print $N}' 打印出相关列
        wc 字符统计
        -c : 统计字符
        -w : 统计单词
        -l : 统计⾏
        例如: 统计代码⾏数 wc -l abc.py
        管道符: |
        管道符可以连接两个命令，将前⾯的输出作为后⾯的输⼊
        history|grep useradd　　查找后面所有的useradd
        history|grep -A 3 useradd  查找所有useradd的后三个命令
        history|grep -B 3 useradd　查找所有useradd的前三个命令
        history|grep -C 3 useradd　查找所有useradd的前三个和后三个命令
        history|grep -E 'user*'　　查找后面所有带‘user'的命令

        练习: 统计出⾃⼰使⽤的最多的 10 个命令
        答案: history | awk '{print $2}' | sort | uniq -c | sort -gr | head -n 10
        七、vim
        VIM 是终端下最常⽤的编辑器，有 “编辑器之神” 之称，简洁⽽强⼤！
        VIM 分为三种模式：命令模式，插⼊模式，底栏命令模式
        1. 按 esc 键，进⼊命令模式
        h, j, k, l 光标左、下、上、右移动
        ctl + e 向下滚动
        ctl + y 向上滚动
        ctl + f 向下翻屏
        ctl + b 向上翻屏
        yy 复制整⾏
        yw 复制整⾏
        p 粘贴到下⼀⾏
        P 粘贴到下⼀⾏
        dd 删除整⾏
        d3w 向前删除3个单词
        7x 删除7个字符
        u 撤销
        ctl + r 重做
        c3w 剪切3个单词
        gg 跳⾄⽂件⾸⾏
        shift + g 跳⾄⽂件结尾
        shift + h 跳⾄屏幕⾸⾏
        shift + m 跳⾄屏幕中间
        shift + l 跳⾄屏幕结尾
        ctl + v 列编辑
        shift + v 选中整列
        shift + > 向右缩进
        shift + < 向左缩进
        2. 按 i 键，进⼊插⼊模式
        插⼊模式下正常输⼊即可
        想做其他操作，必须先按 ESC 键回到命令模式
        3. 在命令模式时按 : 键，进⼊底栏命令模式
        23 跳⾄⽂件的第 23 ⾏
        %s/abc/123/g 把⽂件中所有的 abc 替换成 123
        set nu 打开⾏号
        set nonu 关闭⾏号
        w 保存
        q 退出
        wq 保存并退出























