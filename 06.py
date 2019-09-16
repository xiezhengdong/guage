#!/home/xiezhengdong/.local/bin/python
import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line,define,options
define('host',default='127.0.0.1',help='主机名称',type=str)
define('port',default='8000',help='端口',type=int)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("我是一个爱学习的好孩纸")
class TestHandler(tornado.web.RequestHandler):
    def get(self):
        html=('''
                <form action='/foo/bar' method='post'>
                姓名:<input type='text' name='name'>
                <br>
                年龄:<input type='text' name='age'>
                <br>
                城市:<input type='text' name='city'>
                <br>
                <input type='submit'>
                </form>
                ''')
        self.write(html)
    def post(self):
        name=self.get_argument('name')
        age=self.get_argument('age')
        city=self.get_argument('city')
        self.write("%s今年已经%s岁了，他住在%s"%(name,age,city))
def make_app():
    return tornado.web.Application([(r'/',MainHandler),
        (r'/foo/bar',TestHandler)
        ])
if __name__=='__main__':
    parse_command_line()
    app=make_app()
    app.listen(options.port,options.host)
    tornado.ioloop.IOLoop.current().start()
