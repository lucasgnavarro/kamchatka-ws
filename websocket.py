__author__ = 'Lucas Navarro'
import tornado.websocket
import simplejson
from core.audioUtils import audio_action
from core.videoUtils import video_action
from core.peripheralUtils import keyboard_action, key_pressed


clients = []

class WebSocketChatHandler(tornado.websocket.WebSocketHandler):
    def open(self, idClient):
        self.id = idClient
        clients.append(self)
        print "open WebSocketChatHandler %s"%self.id


    def on_message(self, message):
        print message

        self.set_action(message)
        for client in clients:
            #si tengo el id del cliente
            if client.id == self.id:
                print 'CLIENTE %s'%client.id
                client.write_message('LA PUTA QUE TE PARIO%s'%message)

    def on_close(self):
        clients.remove(self)


    def set_action(self,message):
        msg = simplejson.loads(message)
        #print msg.get("family")
        #print msg.get("action")
        #print platform.system()

        if msg.get("family") == 'audio':
            print '**AUDIO**'
            audio_action(msg.get("action"))
        elif msg.get("family") == 'video':
            print '**VIDEO**'
            video_action(msg.get("action"))
        elif msg.get("family") == 'keyboard':
            print '**KEYBOARD**'
            keyboard_action(msg.get("action"))
        elif msg.get("family") == 'key_pressed':
            print '**KEY_PRESSED**'
            key_pressed(msg.get("action"))

