from kamchatka.views import IndexView, ManageView
from kamchatka.websocket import RemoteControlWebSocket
from tornado.web import StaticFileHandler

urlpatterns = [
    (r'/', IndexView),
    (r'/management', ManageView),
    (r'/static/(.*)', StaticFileHandler, {"path": "../front/app/build/static/"}),
    (r'/remote-control/(.*)', RemoteControlWebSocket)
]
