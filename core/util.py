__author__ = 'Lucas Navarro'
import socket
from socket import socket, SOCK_DGRAM, AF_INET, gethostname


def get_host():
    s = socket(AF_INET, SOCK_DGRAM)
    s.connect(('google.com', 0))
    #return gethostname()
    return s.getsockname()[0]


def get_port():
    return 9598 #Port






