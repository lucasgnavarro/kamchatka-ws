import tornado.web
from views import IndexHandler
from websocket import WebSocketChatHandler
import core.util as util


host = util.get_host()
port = util.get_port()


app = tornado.web.Application([
    (r'/ws/(.*)', WebSocketChatHandler), \
    (r'/', IndexHandler), \
    (r'/static/(.*)', tornado.web.StaticFileHandler, {"path": "./front/static/"}),
    ], debug=True,)


app.listen(port, address=host)
print "Listening in %s:%s" % (host, port)
tornado.ioloop.IOLoop.instance().start()
