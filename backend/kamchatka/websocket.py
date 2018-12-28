from tornado.websocket import WebSocketHandler
import json

from kamchatka.peripheral.keyboard import Keyboard
from kamchatka.peripheral.audio import SoundMixer as Audio
from kamchatka.peripheral.video import VideoAdapter as Video
from kamchatka.net.response import simple_response
from kamchatka.net.status_codes import HTTP_500

class RemoteControlWebSocket(WebSocketHandler):
    """
    WebSocket view :O
    """
    websocket_clients = []

    def check_origin(self, origin):
        """
        CORS Related Method
        """
        return True

    def __init__(self, application, request, **kwargs):
        super().__init__(application, request, **kwargs)

        self.id = None
        self.mapped_listeners = {
            'a': Audio,
            'k': Keyboard,
            'v': Video
        }

    def open(self, *args, **kwargs):
        """
        On Open Websocket method
        :param args:
        :param kwargs:
        :return:
        """
        self.id = args[0]
        self.websocket_clients.append(self)     # Append to websockets Queue

    def on_message(self, message):
        _msg = json.loads(message)
        family = _msg.get('f')

        params = {'action': _msg.get('a')}

        if _msg.get('value') is not None:
            params['value'] = _msg.get('value')

        print(params)

        if family in self.mapped_listeners:
            obj = self.mapped_listeners[family]()
            _response = obj.process(**params)
        else:
            _response = simple_response(data=None, status_code=HTTP_500,
                                        message='Action requested is not mapped ({0}) '.format(family))

        # Loop througt websocket_clients and find current websocket
        for client in self.websocket_clients:
            if client.id == self.id:
                self.write_message(json.dumps(_response))

    def on_close(self):
        self.websocket_clients.remove(self)
