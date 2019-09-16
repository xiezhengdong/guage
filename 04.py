#!/home/xiezhengdong/.local/bin/python
import tornado.ioloop
import tornado.web
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('好好学习，天天向上')
class FooHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("我喜欢你")
def make_app():
    return tornado.web.Application([(r'/',MainHandler),(r'/foo',FooHandler)])
if __name__ =='__main__':
    app=make_app()
    app.listen(8000)
    tornado.ioloop.IOLoop.current().start()




    
        

    

    
    
    
