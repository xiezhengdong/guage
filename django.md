# cs 和bs

首先，让我们再回顾一下之前在学习flask的时候提到过的cs/bs,还有与mvc和mvt相关的知识。

```
cs和bs分别指的是客户端和服务器，浏览器和服务器。
client server 和 browser server
B/S结构是WEB兴起后的一种网络结构模式，WEB浏览器是客户端最主要的应用软件。这种模式统一了客户端，将系统功能实现的核心部分集中到服务器上，简化了系统的开发、维护和使用。
```

cs 和 bs之间的区别有哪些：

分别可以从五个方面来回答，如下图所示：





# mvc

```
MVC：软件架构思想
	简介：
		MVC开始是存在于桌面程序中的，M是指业务模型 model，V是指用户界面 view，C则是控制器 controler，使用MVC的目的是将M和V的实现代码分离，从而使同一个程序可以使用不同的表现形式。比如一批统计数据可以分别用柱状图、饼图来表示。C存在的目的则是确保M和V的同步，一旦M改变，V应该同步更新
实现了模型层的复用
	核心思想: 
		解耦合
	面向对象语言：高内聚  低耦合
	Model
		模型
		封装数据的交互操作
			CRUD
	View
		视图
		是用来将数据呈现给用户的
	Controller
		控制器
		接受用户输入输出
		用来协调Model和View的关系，并对数据进行操作，筛选
	流程
		控制器接受用户请求
		调用模型，获取数据
		控制器将数据展示到视图中
```

# MTV

```
MTV
	也叫做MVT
	本质上就是MVC，变种
	Model
		同MVC中Model
	Template
		模板
		只是一个html，充当的是MVC中View的角色，用来做数据展示
	Views
		视图函数
		相当于MVC中Controller
```



# django的介绍与使用：

#### 安装：

```
pip install django==1.11.7
查看是否安装成功的话，使用以下命令：
pip freeze
pip list
```

#### 创建django项目：

```
django-admin startproject 项目名称
tree命令来查看项目结构
如果没有安装tree的话，使用sudo apt install tree 来安装。
```

```
项目结构如下所示：
	项目名字
		manage.py(管理整个项目的文件，以后的命令都基本通过它来调用)
	项目名字
		__init__
			Python包而不是一个文件夹
		settings
			项目全局的配置文件
			ALLOWED_HOST=['*']
			修改Settings
				LANGUAGE_CODE='zh-hans'
				TIME_ZONE='Asia/Shanghai'
		urls
			根路由
				url(p1,p2)
```

#### 启动项目：

```
python manage.py runserver	使用开发者服务器启动项目，默认会使用本机的8000端口
启动服务器命令
（1）python manage.py runserver
 (2)python manage.py runserver 9000
 (3)python manage.py runserver 0.0.0.0:9000
```

####  创建一个应用：

```
python manage.py startapp App和django-admin startapp App都可以创建一个应用。
	App结构
		__init__
		views
			视图函数（视图函数的参数是request,方法的返回值类型是HttpResponse
		models
			模型
		admin
			后台管理
		apps
			应用配置
		tests
			单元测试
		migrations
			__init__
			迁移目录
```

#### 拆分路由

```
python manage.py startapp two
创建urls
	urlpatterns=[
        url(r'^index/',views.index)
	]
创建views方法
url(r'^two/',include('two.urls'))
```

编写视图函数：

```
def index(request):
	return HttpResponse('ok')
返回的数据类型是一个HttpResponse类型，记住：当要返回一个页面的时候，一定要在括号里面的第一个位置加上参数request,如下所示：
	def test(request):
		return render(request,'test.html')
在使用模板的时候，要先在项目的settings中注册，即：
INSTALLED_APPS -->>'TWO'
```

#### 模板配置

```
模板配置有两种情况
		①在App中进行模板配置
		  - 只需在App的根目录创建templates文件夹即可
		  - 必须在INSTALLED_APP下安装app
		②在项目目录中进行模板配置
		  - 需要在项目目录中创建templates文件夹并标记
		  - 需要在settings中进行注册  settings--》TEMPLATES--》DIRS-	
		
	
os.path.join(BASE_DIR,'templates')
		  注意：开发中常用项目目录下的模板    理由：模板可以继承，复用
```

# **django的工作机制：**

重点记住：

```
1.用manage .py runserver 启动Django服务器时就载入了在同一目录下的settings .py。该文件包含了项目中的配置信息，如URLConf等，其中最重要的配置就是ROOT_URLCONF，它告诉Django哪个Python模块应该用作本站的URLConf，默认的是urls .py

2.当访问url的时候，Django会根据ROOT_URLCONF的设置来装载URLConf。

3.然后按顺序逐个匹配URLConf里的URLpatterns。如果找到则会调用相关联的视图函数，并把HttpRequest对象作为第一个参数(通常是request)

4.最后该view函数负责返回一个HttpResponse对象。
```

# 整个创建流程：

```
1 创建虚拟环境

2 安装django
        pip install django==1.11.7

3 创建django项目
        django-admin startproject  xxx

4 启动服务器的命令
        python manage.py runserver

5 项目的结构
        项目名字
            项目名字
                init
                urls
                settings
                wsgi
            manage.py

6 修改虚拟环境的步骤
    file-->setting-->project interpreter-->add-->exist environment-->...
    虚拟环境的文件夹--》bin--》python

7 修改欢迎页面为中文
    在settings中修改LANGUAGE_CODE = 'zh-hans'

8 修改为当前系统时间
    在settings中修改TIME_ZONE = 'Asia/Shanghai'

9 允许所有主机访问
    在settings中修改ALLOWED_HOSTS = ['*']

10 启动服务器设置端口号和主机
    python manage.py runserver
    python manage.py runserver 9000
    python manage.py runserver 0.0.0.0:9000

11 视图函数的位置
    （1）项目名字下的视图函数  就是不用
        在urls定义路由路径
            url(r'^路径/',views.视图函数名字不加圆括号)
                eg:url(r'^index/',views.index)
        在views中定义视图函数
            def index(request):
                return HttpResponse('index')

     如果把所有的视图函数都放在项目下了 那么代码看起来就特别的臃肿
     所以我们一般的企业级开发 都是把每一个模块封装出一个app
    （2）App
            1.创建App
                 django-admin startapp App/python manage.py startapp App
            2.在App中创建urls
            3.在urls中创建urlpatterns=[] 我们称在app下urls叫做子路由
            4.在跟路由（项目下的urls）加载子路由  url(r'^app/',include('App.urls'))
            5.在子路由中定义请求资源路径也就是路由
                url(r'^index/',views.index)
            6.在App下的views下创建视图函数
            7.访问 127.0.0.1：8000/跟路由的名字/子路由的名字
                eg:127.0.0.1:8000/app/index/


```



















