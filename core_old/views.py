__author__ = 'Lucas Navarro'
import tornado.web
import core_old.util as util
import socket


class IndexHandler(tornado.web.RequestHandler):


    @tornado.web.asynchronous
    def get(request):
        host = util.get_host()
        port = util.get_port()
        request.render("./front/index.html", host=host, port=port, hostname=socket.gethostname().capitalize())
