# -*- coding: utf-8 -*-
import socket
import json
import tornado.web
from tornado.websocket import WebSocketHandler

from kamchatka.net import util
from kamchatka.net.status_codes import HTTP_500
from kamchatka.net.response import simple_response
import kamchatka.settings as s


class ManageView(tornado.web.RequestHandler):

    def get(self):

        # for client in WebSocketView.websocket_clients:
        #     print(client.__dict__)

        # for client in WebSocketView.websocket_clients:
        #     client.write_message('BROTHEEEER')
        host = util.get_host()
        port = s.LISTEN_PORT

        params = {
            'server_url': 'http://{host}:{port}'.format(host=host, port=port),
            'hostname': socket.gethostname().capitalize()
        }
        self.render("../../front/management/index.html", **params)


class IndexView(tornado.web.RequestHandler):

    def get(self):
        # self.write('Index')
        host = util.get_host()
        port = s.LISTEN_PORT
        self.render("../../front/app/build/index.html", host=host, port=port, hostname=socket.gethostname().capitalize())


