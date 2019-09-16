# 数据库与模板系统

一，ORM:对象关系映射

首先，我们要了解什么是ORM，ORM就是对象关系映射。。其主要作⽤是在编程中把⾯向对象的概念 

跟数据库中表的概念对应起来。 

举例来说就是，我定义⼀个类，那就对应着⼀张表，这个类的实例，就对应着表中的⼀条记录。 

⾯向对象编程把所有实体看成对象（object），关系型数据库则是采⽤实体之间的关系（relation）连 接数据。 

很早就有⼈提出，关系也可以⽤对象表达，这样的话，就能使⽤⾯向对象编程，来操作关系型数据库。 

Python下常⽤的 ORM 有: Django-ORM、SQLAlchemy、Peewee 等

# 二.举例子

首先在这里，我们使用SQLAlchemy 来操作数据库，看下面的代码：

```
import datetime 

from sqlalchemy import create_engine 

from sqlalchemy.orm import sessionmaker 

from sqlalchemy import Column, String, Integer, Float, Date 

from sqlalchemy.ext.declarative import declarative_base 

\# 建⽴连接与数据库的连接 

engine = create_engine('mysql+pymysql://seamile:54188@localhost:3306/ttt') 

Base = declarative_base(bind=engine) # 创建模型的基础类 

Session = sessionmaker(bind=engine) 

class User(Base): 

'''User 模型''' 

__tablename__ = 'user' # 该模型对应的表名 

id = Column(Integer, primary_key=True) # 定义 id 字段 

name = Column(String(20), unique=True) # 定义姓名字段 

birthday = Column(Date) # 定义⽣⽇字段 

money = Column(Float, default=0.0) # 定义⾦钱字段 

Base.metadata.create_all(checkfirst=True) # 创建表 

session = Session() 

\# 定义⼀些对象 

bob = User(name='bob', birthday=datetime.date(1990, 3, 21), money=234) 

tom = User(name='tom', birthday=datetime.date(1995, 9, 12)) 

lucy = User(name='lucy', birthday=datetime.date(1998, 5, 14), money=300) 

jam = User(name='jam', birthday=datetime.date(1994, 3, 9), money=58) 

alex = User(name='alex', birthday=datetime.date(1992, 3, 17), money=99) 

eva = User(name='eva', birthday=datetime.date(1987, 7, 28), money=175) 

rob = User(name='rob', birthday=datetime.date(1974, 2, 5), money=274) 

ella = User(name='ella', birthday=datetime.date(1999, 5, 26), money=394) 

\# 增加数据 

session.add_all([bob, tom, lucy, jam]) # 在 Session 中记录操作 

session.commit() # 提交到数据库中执⾏ 

\# 删除数据 

session.delete(jam) # 记录删除操作 

session.commit() # 提交到数据库中执⾏ 
tom.money = 270 # 修改数据 

session.commit() # 提交到数据库中执⾏ 

\# 查询数据 

u_query = session.query(User) 

user = u_query.filter_by(id=1).one() 

print(user.name) 

users = u_query.filter(User.id>2).order_by('birthday') 

for u in users: 

print(u.name, u.birthday, u.money) 

\# 根据查询结果进⾏更新 

users.update({'money': User.money - 1}, synchronize_session=False) 

sessiom.commit() 

\# 按数量取出数据: limit / offset 

users = u_query.limit(3).offset(4) 

for u in users: 

print(u.id, u.name)
```

# 三、**Tornado** 的模板系统 

模板系统是为了更快速、更⽅便的⽣产⼤量的⻚⾯⽽设计的⼀套程序。 

借助模板系统，我们可以先写好⻚⾯⼤概的样⼦，然后预留好数据的位置，再然后将我们需要的数据， 

按照既定规则拼到模板中的指定位置，然后渲染出完整⻚⾯。 

现代的模板系统已经相当成熟，甚⾄可以通过 if...else 、 for 等语句在模板中写出简单的逻辑控 制。 

### **1.** 模版与静态⽂件的路径配置 

定义 app 时，在 Application 中定义, 可以是想对路径, 也可以是绝对路径 

```
app = Application(
templates_path = 'templates', # 模版路径
static_path = 'statics' # 静态⽂件路径
)
```

### **2.** 模板中的变量 

在模板中，变量和表达式使⽤ {{ ... }} 包围，可以写⼊任何的 Python 表达式或者变量

<!DOCTYPE html> 

```
<html lang='en'> 

<head>

<meta charset='UTF-8'> 

<title>Templates</title> 

</head> 

<body>

<div>你好 {{ name }}，欢迎回来！</div> 

<div>猜⼀猜，3 x 2 等于⼏？</div> 

<div>我就不告诉你等于 {{ 3 * 2 }}</div>

</body> 

</html>
```

### **3.** 从 **Python** 程序中传递参数

```
class MainHandler(tornado.web.RequestHandler):
def get(self):
name = 'Tom'
say = "Hello, world"
self.render('index.html', name=name, say=say)
```

### **4.** 模板中的 **if...else** 结构

模板中的控制语句使⽤ {% ... %} 包围，如下所示：

```
<p>
根据您的条件我们进⾏了筛选
 {% if 条件 %}
<div>第 1 条数据</div> <div>第 2 条数据</div> <div>。。。</div>
 {% else %}
<div>抱歉我们没有找到合适的内容</div>
 {% end %}
</p>
```

### **5.** 模板中的 **for** 循环

在Python程序中：

```
class MainHandler(tornado.web.RequestHandler):
def get(self):
students = ["Lucy", "Tom", "Bob"]
self.render("student.html", students=students)
```

页面中：

```
<html> <head> <title>学⽣信息</title>
</head> <body> <ul>
 {% for student in students %}
<li>{{ student }}</li>
 {% end %}
</ul>
</body>
</html>
```

### **6.** 静态⽂件

在模板中使⽤静态⽂件时，静态⽂件的路径这样写:

```
<img class="avatar" src="/static/img/coder.jpg" />
```

### **7.** 模板的继承

Tornado 为我们提供了模板的继承机制，只需要写好⽗模板，然后让其他模板继承⼀下即可 

⽗模板⽂件名经常定义为 "base.html"

```
<!DOCTYPE html>
<html lang="en"> <head><meta charset="UTF-8"> <title>{% block title %} 通⽤标题 {% end %}</title>
</head> <body>
 {% block body %}{% end %}
</body>
</html>
```

子模板：

```
{% extends "base.html" %}
{% block title %} ⼦⻚⾯的标题 {% end %}
{% block body %}
<div>
⼦⻚⾯⾥的内容
 Bala Bala
</div>
{% end %}
```

