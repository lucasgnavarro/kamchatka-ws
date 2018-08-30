# -*- coding: utf-8 -*-
import tornado.ioloop
import tornado.web
import webbrowser

import kamchatka.urls
import kamchatka.settings as s
from kamchatka.net import util


class Server:

    listen_port = None
    host = util.get_host()

    def __init__(self, *args, **kwargs):
        self.mapped_urls = kwargs.get('urls', [])

        # Config Port
        if 'port' in kwargs:
            self.listen_port = kwargs.get('port', 9898)
        else:
            try:
                self.listen_port = s.LISTEN_PORT
            except Exception as e:
                print('LISTEN_PORT is not defined in settings, default port now is 9898')
                self.listen_port = 9898

        if 'debug' in kwargs:
            self.debug = kwargs.get('debug', False)
        else:
            try:
                self.debug = s.DEBUG
            except Exception as e:
                self.debug = False

    def map_urls(self):
        if not self.mapped_urls:
            try:
                self.mapped_urls = kamchatka.urls.urlpatterns
            except Exception as e:
                print('Exception on map urls {e}'.format(e=e))

    def run_server(self):
        self.map_urls()
        app = tornado.web.Application(self.mapped_urls, debug=self.debug)
        app.listen(self.listen_port)
        print('Running server on Port {port}, debug mode is {debug}'.format(port=self.listen_port, debug=self.debug))
        # self.browse()
        tornado.ioloop.IOLoop.current().start()

    def stop_server(self):
        tornado.ioloop.IOLoop.current().stop()

    def browse(self):
        _url = 'http://{host}:{port}/management'.format(host=self.host , port=self.listen_port)
        webbrowser.open_new_tab(_url)
