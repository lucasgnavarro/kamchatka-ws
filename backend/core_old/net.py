__author__ = 'Lucas Navarro'
import socket
import urllib.request
import json
from socket import socket, SOCK_DGRAM, AF_INET, gethostname


def get_external_ip():
    try:
        data = json.loads(urllib.request.urlopen("http://ip.jsontest.com/").read())
        external_ip = data.get('ip', '0.0.0.0')
    except Exception as e:
        external_ip = '0.0.0.0'

    return external_ip

def get_host():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(('google.com', 0))
    #return gethostname()
    return s.getsockname()[0]


def get_port():
    return 9598 #Port






