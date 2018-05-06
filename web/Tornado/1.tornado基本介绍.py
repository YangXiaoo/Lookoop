#date(2018-4-27)

-------------基础-------------
1)异步编程原理
	协程(coroutine):在一个线程之内，无需操作系统参与，由程序自身调度的执行单位。
	在一个进程之内同时处理多个协程(请求)，充分利用CPU时间，就需要异步编程

2)epoll
	发起访问，将网络连接的文件描述符（fd）和期待事件（read）注册到 epoll 里。当期待事件发生，epoll 触发事件处理机制，通过回调函数通知 tornado，tornado 切换协程。	

3)用生成器实现协程
	yield gen.sleep(1)
	一个函数执行中间，先通过 yield 出去一下，随后再回来执行后面部分。Tornado 就利用了 yield 的这个特性，在需要等待时先离开当前协程，等待结束了再回来。
-------------
#http_0.py
from tornado.ioloop import IOLoop
from tornado import gen, web
class ExampleHandler( web.RequestHandler ): 
#用一个继承于 web.RequestHandler 的类构造处理 HTTP 访问的 handler
　@gen.coroutine
#装饰器作用：把一个普通的函数变成一个返回 Future 对象的函数，即异步函数。
　def get( self ):
	#重载get方法构造GET请求
　　delay = self.get_argument( 'delay', 5 )
　　yield gen.sleep( int( delay ))
　　self.write( { "status": 1, "msg": "success" } )
　　self.finish() #需要结束，若有模板则还要传递给模板
#　@gen.coroutine
#　def post( self ):
#　　pass

#通过 Application 对象将构造好的 ExampleHandler 与一个 uri 联系起来
application = web.Application( [
　　　　　　( r"/example", ExampleHandler ),
　　　　　　#( r"/other", OtherHandler ),
　　　　　　], autoreload = True )
application.listen( 8765 ) #监听接口
'''
若开启多个服务进程则如下：
from tornado.httpserver import HTTPServer
server = HTTPServer( application )
server.bind( 8765 )
server.start( 4 )  #同时启动 4 个进程
'''
IOLoop.current().start()  #启动消息循环
----------------------------
4)数据库操作
-------
#http_db.py
from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado_mysql import pools
connParam = { 'host': 'localhost', 'port': 3306, 'user': 'root',
　　　'passwd': 'zzzzzz', 'db': 'testdb' }
class GetUserHandler( web.RequestHandler ):
　POOL = pools.Pool(
　　　connParam,
　　　max_idle_connections=1,
　　　max_recycle_sec=3,
　　　　)
　@gen.coroutine
　def get( self ):
　　userid = self.get_argument( 'id' )
　　cursor = yield self.POOL.execute( 'select name from user
　　　　　　　　　　　　　　　where id = %s', userid )
　　if cursor.rowcount &gt; 0:
　　　self.write( { "status": 1, "name": cursor.fetchone()[0] } )
　　else:
　　　self.write( { "status": 0, "name": "" } )
　　self.finish()
application = web.Application( [
　　　　　　　( r"/getuser", GetUserHandler ),
　　　　　　　　　], autoreload = True )
application.listen( 8765 )
IOLoop.current().start()
------------
5)访问网络
---------
#http_req.py
from tornado.ioloop import IOLoop
from tornado import gen, web
from tornado.httpclient import AsyncHTTPClient
url = 'http://hq.sinajs.cn/list=sz000001'
class GetPageHandler( web.RequestHandler ):
　@gen.coroutine
　def get( self ):
　client = AsyncHTTPClient()
　response = yield client.fetch( url, method = 'GET' )
　self.write( response.body.decode( 'gbk' ))
　self.finish()
application = web.Application( [
　　　　　　　( r"/getpage", GetPageHandler ),
　　　　　　　　　], autoreload = True )
application.listen( 8765 )
IOLoop.current().start()
#用浏览器访问http://localhost:8765/getpage则可以看到http://hq.sinajs.cn/list=sz000001页面的内容
------------