# request对象

```
概念：django框架根据Http请求报文自动生成的一个对象，包含了请求各种信息。
属性：
       path：请求的完整路径
       method：GET  1.11版本最大数据量2K
	          POST 参数存在请求体中，文件上传等。
			  请求的方法，常用GET,POST
			  应用场景：前后端分离的底层 判断请求方式 执行对应的业务逻辑
	   GET：QueryDict类字典结构 key-value
		                      一个key可以对应多个值
		                      get 获取最后一个
		                      getlist 获取多个
							类似字典的参数，包含了get请求方式的所有参数
	  POST： 类似字典的参数，包含了post请求方式的所有参数
	  encoding：编码方式，常用utf-8
	  FILES：类似字典的参数，包含了上传的文件  文件上传的时候会使用  
	         页面请求方式必须是post   form的属性enctype=multipart/form-data
	         flask和django通用的   一个是专属于django
	  COOKIES：类似字典的参数，包含了上传的文件  获取cookie
	  session：类似字典，表示会话
	  META：   应用反爬虫  REMOTE_ADDR  拉入黑名单
	           客户端的所有信息 ip
	           print(request.META)
			  for key in request.META:
			        print(key, request.META.get(key))
			  print("Remote IP", request.META.get("REMOTE_ADDR"))
```

# HttpResponse对象

当浏览器访问服务器的时候  那么服务器响应的数据类型

响应分类：（1）HTML响应   （2）JsonResponse（前后端分离）

```
（1）基类HttpResponse   不使用模板，直接HttpResponse()
	def hello(request):
             response = HttpResponse()
             response.content = "德玛西亚"
             response.status_code = 404
             response.write("千锋")
             response.flush()
        return response
     方法
		 init				初始化内容
	     write(xxx)			直接写出文本
         flush()				冲刷缓冲区
         set_cookie(key,value='xxx',max_age=None,exprise=None)
         delete_cookie(key)		删除cookie，上面那个是设置
         
（2）render转发：
		方法的返回值类型也是一个HttpResponse

（3）HttpResponseRedirect重定向
     HttpResponse的子类，响应重定向:可以实现服务器内部跳转
	return HttpResponseRedict('/grade/2017')使用的时候推荐使用反向解析
	
	状态码：302
	
	简写方式：简写redirect方法的返回值类型就是HttpResponseRedirect
	
	反向解析：
            （1）页面中的反向解析 url方法
                      	  {% url 'namespance:name'
                      url 位置参数
                          {% url 'namespace:name'  value1 value2 %}
                      url关键字参数
                          {% url 'namespace:name' key1=value1 key2 = value2 %}
            （2）python代码中的反向解析（一般python代码的反向解析都会结合重定向一起使用）
                          reverse('namespace:name')
                      位置参数
                          reverse('namespace:name', args=(value1, value2 ...))
                          reverse('namespace:name', args=[value1, value2 ...])
                      关键字参数
                          reverse('namespace:name', kwargs={key1:value2, key2:value2 ...})

```

# JsonResponse

```
这个类是HttpRespon的子类，它主要和父类的区别在于：
1.它的默认Content-Type 被设置为： application/json

2.第一个参数，data应该是一个字典类型，当 safe 这个参数被设置为：False ,那data可以填入任何能被转换为JSON格式的对象，比如list, tuple, set。 默认的safe 参数是 True. 如果你传入的data数据类型不是字典类型，那么它就会抛出 TypeError的异常。

def get_info(request):
	data = {
        "status": 200,
        "msg": "ok",
    }
	return JsonResponse(data=data)
```

# HttpResponse子类

```
HttpResponse子类
	HttpResponseRedirect 
		-302
	HttpResponsePermanentRedirect
		- 重定向，永久性- 
		-301
	HttpResponseBadRequest	
		-400
	HttpResponseNotFound
		- 404
	HttpResponseForbidden
		- 403   csrf 防跨站攻击 
	HttpResponseNotAllowed
		- 405   
	HttpResponseServerError
		- 500
	Http404- Exception
           - raise 主动抛异常出来
```

# 会话技术

### cookie：

```
	客户端会话技术，数据都存储在客户端，以key-value进行存储，支持过期时间max_age，默认请求会携带本网站的所有cookie，cookie不能跨域名，不能跨浏览器，cookie默认不支持中文base64
	cookie是服务器端创建  保存在浏览器端
	设置cookie应该是服务器 response
	获取cookie应该在浏览器 request
	删除cookie应该在服务器 response
cookie使用：
	设置cookie：response.set_cookie(key,value）
	获取cookie：username =request.COOKIES.get("username")
	删除cookie：response.delete_cookie("content")
	
	可以加盐：加密 获取的时候需要解密
		加密  response.set_signed_cookie('content', uname, "xxxx")
		解密  
			 获取的是加盐之后的数据
			 	uname = request.COOKIES.get('content)
			 获取的是解密之后数据
			 uname = request.get_signed_cookie("content", salt="xxxx")
		
	通过Response将cookie写到浏览器上，下一次访问，浏览器会根据不同的规则携带cookie过来
		max_age:整数，指定cookie过期时间  单位秒
		expries:整数，指定过期时间，还支持是一个datetime或	timedelta，可以指定一个具体日期时间
		max_age和expries两个选一个指定
		过期时间的几个关键时间
			max_age 设置为 0 浏览器关闭失效
			设置为None永不过期
			expires=timedelta(days=10) 10天后过期
```

### session

```
	服务端会话技术，数据都存储在服务端，默认存在内存 RAM，在django被持久化到了数据库中，该表叫做
	Django_session,这个表中有三个字段，分别为seesion_key,session_data,expris_date.
	Django中Session的默认过期时间是14天，支持过期，主键是字符串，默认做了数据安全，使用了BASE64
		- 使用的base64之后 那么这个字符串会在最后面添加一个=
		- 在前部添加了一个混淆串
	依赖于cookies
session使用：
	设置session
		    request.session["username"] = username
	获取session
		    username = request.session.get("username")
	使用session退出
            del request.session['username']
                cookie是脏数据
            response.delete_cookie('sessionid')
                session是脏数据
            request.session.flush()
			   冲刷
	session常用操作
		get(key,default=None) 根据键获取会话的值
		clear() 清楚所有会话
		flush() 删除当前的会话数据并删除会话的cookie
		delete request['session_id'] 删除会话
		session.session_key获取session的key
		request.session[‘user’] = username
			数据存储到数据库中会进行编码使用的是Base64
```

