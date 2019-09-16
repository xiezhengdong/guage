　　shell编程与运维
   什么是shell脚本？
      通过 Shell 中的各种命令, 开发者和运维⼈员可以对服务器进⾏维护⼯作。
    但每次都⼿动输⼊命令, ⼯作效率太低, ⽽且很容易出错, 尤其是需要维护⼤量服务器时。
    为了能够对服务器批量执⾏操作, 我们可以将需要执⾏的命令写⼊⽂件, 批量执⾏, 这种⽂件便是                                  　　　Shell 脚本。Shell 脚本⼀般是以 .sh 结尾的⽂本⽂件, 当然, 也可以省略扩展名。       

        shell脚本首行：脚本⽂件第⼀⾏通过注释的⽅式指明执⾏脚本的程序，格式就是如下所示：
                                                                #!/bin/bash
        常见的方式有以下三种：
            #!/bin/sh
            #!/bin/bash
            #!/usr/bin/env bash
　　第一个脚本文件如下所示：
            shell脚本文件一般都是以.sh结尾的
            １．先创建一个a.sh文件
            ２．然后写入文本
            例如：
                #!/bin/bash
                echo "hello"
                echo "world"
                echo "whoami"
             3.执行chmod a+x a.sh　对脚本进行授权处理
             ４． ./a.sh执行脚本
             ５．查看脚本的退出状态：echo $?
                在这里值得注意的是：linux里面，所有程序在执行结束之后都有状态码，０代表正常，正整数代表异常退出。
　　
　　　变量：
        # 变量定义: 等号前后没有空格
        a=12345
        b=xy
        切记：变量在使用之前，要在变量名前面加上$符号，还有，要注意引号的差别，最好使用双引号，保险一点。
             定义当前Shell下的全局变量
1. 定义: export ABC=9876543210123456789
2. 定义完后, 在终端⾥⽤ source 加载脚本: source ./test.sh

         常⽤的系统环境变量
        $PATH : 可执⾏⽂件⽬录
        $PWD : 当前⽬录
        $HOME : 家⽬录
        $USER : 当前⽤户名
        $UID : 当前⽤户的 uid
        
    if 语句的用法：格式如下：
        if command
        then 
            command
        elif command
            commands
        else
            commands
        fi
    注意：一定不能忘了在if语句结束的时候加上fi
         if 语句检查判断的依据实际上是, 后⾯所跟的命令的状态码: 0 为 true, 其他值 为 false

    条件测试命令: [ ... ]
    shell 提供了⼀种专⽤做条件测试的语句 [ ... ]
    这⼀对⽅括号本质上是⼀个命令, ⾥⾯的条件是其参数, 所以 [ 的后⾯和 ] 的前⾯必须有空
    格, 否则会报错。
        他可以进⾏三种⽐较
        数值⽐较
        字符串⽐较
        ⽂件⽐较
        ⽤法:
                    3. 条件列表
                    数值⽐较
                    if command
                    then
                     commands
                    elif command
                     commands
                    else
                     commands
                    fi
                    if ls /xxx
                    then
                     echo 'exist xxx'
                    else
                     echo 'not exist xxx'
                    fi
                    if [ condition ]
                    then
                     commands
                    fi
                    Condition 说明
                    n1 -eq n2 检查n1是否与n2相等
                    n1 -ge n2 检查n1是否⼤于或等于n2
                    n1 -gt n2 检查n1是否⼤于n2
                    n1 -le n2 检查n1是否⼩于或等于n2
                    n1 -lt n2 检查n1是否⼩于n2
                    n1 -ne n2 检查n1是否不等于n2
                    Condition 说明
                    str1 = str2 检查str1是否和str2相同
                    str1 != str2 检查str1是否和str2不同
                    str1 < str2 检查str1是否⽐str2⼩
                    str1 > str2 检查str1是否⽐str2⼤
                    -n str1 检查str1的⻓度是否⾮0
                    -z str1 检查str1的⻓度是否为0
                    字符串⽐较
                    ⽂件⽐较
                    Condition 说明
                    -d file 检查file是否存在并是⼀个⽬录
                    -e file 检查file是否存在
                    -f file 检查file是否存在并是⼀个⽂件
                    -r file 检查file是否存在并可读
                    -w file 检查file是否存在并可写
                    -x file 检查file是否存在并可执⾏
                    -s file 检查file是否存在并⾮空
                    -O file 检查file是否存在并属当前⽤户所有
                    -G file 检查file是否存在并且默认组与当前⽤户相同
                    file1 -nt file2 检查file1是否⽐file2新
                    file1 -ot file2 检查file1是否⽐file2旧


　　　　 for 循环的基本格式:
                for 变量 in 序列 do
                     要执⾏的命令
                done
        例如：
            for i in `seq 1 10`
            do
             if [[ $[ $i % 2] == 0 ]]
             then
             echo "偶数: $i"
             else
             echo "奇数: $i"
             fi
            done
1. seq START END 语句⽤来产⽣⼀个数字序列
2. $[ NUM1 + NUM2 ] 语句⽤来进⾏基本的数学运算
3. [[ ... ]] 语句⽤来更⽅便的进⾏⽐较判断
            
 C语⾔⻛格的 for 循环:
        for ((i=0; i<10; i++))
        do
         echo "num is $i"
        done
       

函数：
 function foo() {
 echo "---------------------------"
 echo "Hello $1, nice to meet you!"
 echo "---------------------------"
}

 函数的使⽤
在终端或脚本中直接输⼊函数名即可，不需要⼩括号
传参也只需将参数加到函数名后⾯，以空格做间隔，像正常使⽤命令那样
$@,代表传参可以传多个
函数的参数：直接在调用的时候，后面加上参数就行，参数之间有空格隔开

获取用户输入：
read -p "请输⼊⼀个数字：" num
echo "您输⼊的是：$num










