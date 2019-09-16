# 虚拟环境与Git

## 一.MVC网站架构

首先，我们要知道什么是MVC式的结构，这种模式是软件工程中的一种软件架构模式，把软件系统分为三个部分：

#### 模型(Model),它是程序需要操作的数据或信息。

####  视图(View),它提供给用户的操作界面,是程序的外壳。 

#### 控制器(Controller),它负责根据用户从"视图层"输?的指令,选取"数据层"中的数据,然后对其进相应的操作,产生最终结果。

对应到我们的服务器程序，简单来说，就是⼀些模块只负责前端⻚⾯显示，另⼀些模块只负责数据模型的定义和数据的操作，其他模块负责连接这两部分，并进⾏必要的逻辑处理。

对应到我们的程序细节，我们可以按照程序的功能不同，分为3个模块。

```
project/
		|--models.y   -->model层
		|--view.py    -->view层
		|--main.py    -->controller层
		
		|--statics/
		|  |--img/
```

# ⼆、虚拟环境

在以后实际的工作中，我们可能要同时维护多个项目，每个项目使用的软件包，版本都可能不一样，这时，如果把所有的版本都装在全局中的话，可能会发生报错，所以我们要为不同的项目单独设置它运行所需的环境，这个时候，虚拟环境就体现出作用了。

#### 1.安装

pip install virtualenv

#### 2.创建虚拟环境

```
cd ~/你自己的文件夹
#虚拟环境可以在任何位置创建，但是一般情况下，与项目文件夹放在一起。
virtualenv env
```

#### 3.加载虚拟环境

source ~/项目文件夹/env/bin/activate    #目的是激活虚拟环境

#### 4.退出虚拟环境

deactivate  #  当开发完成后，就可以退出当前虚拟环境

#### 5.导出虚拟环境的软件包

pip freeze>requirements.txt

#### 6.当别的用户需要下载时

首先 ，source 文件夹名/bin/activate

pip install -r requirements

# 三.版本控制工具与Git

版本控制工具的作用	

```
1.能够追踪全部代码的状态
2.能够进⾏版本之间的差异对⽐ 
3.能够进⾏版本回滚
4.能够协助多个开发者进⾏代码合并
```

常见的版本工具：

CVS:已经凉了

svn:中心化的版本控制工具，需要一台中心服务器

git：分布式的版本控制工具，中心服务器不再是必须的

hg:纯python开发的版本控制工具

Github:依靠Git创建的一个平台

记住：所有文本类的东西都可以交给版本控制工具来管理

## 操作步骤：

### 1.起步

配置自己的账号和邮箱

```
gitconfig--globaluser.name'你的名字'
gitconfig--globaluser.email'你的邮箱'
```

```
设置要忽略的⽂件
对于不需要让Git追踪的⽂件可以在项⽬⽬录下创建.gitignore文件
touch .gitignore

.gitignore⽂件中可以写需要忽略的⽂件名，或是某⼀类⽂件的通配符,如下:
*.pyc 
*.log 
*.sqlite3 
.DS_Store 
.venv/
.idea/
__pycache__/
```

### 2.必须要掌握的命令

git init 对仓库进行初始化，产生了一个.git的目录，这个文件夹就是本地仓库

git log 查询历史提交记录

git init 对仓库进行初始化，产生了一个.git的目录，这个文件夹就是本地仓库

git add   将当前文件夹下所有文件添加到'暂存区'中

git commit -m '完成管理系统'      将‘暂存区’中的代码提交到本地仓库

git push -u origin master        	将本地仓库推送到远程仓库，第一次之后可以直接使用git push即可

ssh-keygen 		在家目录下~/.ssh 目录下生成一对公钥和密钥

将公钥内容复制到Github

git clone:第一次操作，将远程仓库整个的拉下来

git pull:将远程仓库最新的更新拉下来

git checkout  还原，后面可以加id来实现回滚，也可以直接加文件名，但是，如果文件已经在暂存区了的话，就不能直接使用git checkout了，可以先使用git reset来先还原，在进行操作。

![](C:\Users\32568\AppData\Roaming\Typora\typora-user-images\1568201569988.png)

pip   

​		python安装目录/lib/python3.6/