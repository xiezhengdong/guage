#!/home/xiezhengdong/.local/bin/python
import tornado.ioloop
import tornado.web
from tornado.options import parse_command_line,define,options
define('host',default='127.0.0.1',help='主机名称',type=str)
define('port',default='8000',help='端口号',type=int)
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('我很好')
class FooHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('你很好')
class BarHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('大家都很好')
def make_app():
    return tornado.web.Application([(r'/',MainHandler),
        (r'/foo',FooHandler),
        (r'/bar',BarHandler)
        ])
if __name__=='__main__':
    parse_command_line()
    app=make_app()
    app.listen(options.port,options.host)
    tornado.ioloop.IOLoop.current().start()
