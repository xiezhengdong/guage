#!/home/xiezhengdong/.local/bin/python
import tornado.ioloop
import tornado.websocket
from tornado.options import parse_command_line,define,options
define('host',default='127.0.0.1',help='主机名称',type=str)
define('port',default='8000',help='端口号',type=int)
class MainHandler(tornado.websocket.WebSocketHandler):
    conn_pool=set()
    def open(self):
        print('客户端和我连接')
        self.conn_pool.add(self)
    def on_message(self,message):
        self.write_message('我受到了消息%s'%message)
        self.broadcast(message)
        
    def on_close(self):
        print('断开连接')

    def broadcast(self,message):
        for conn in self.conn_pool:
            if conn is  not self:
                conn.write_message(message)
        

    
        
def make_app():
    return tornado.web.Application([(r'/msg',MainHandler),
        
        
        ])
if __name__=='__main__':
    parse_command_line()
    app=make_app()
    app.listen(options.port,options.host)
    tornado.ioloop.IOLoop.current().start()
