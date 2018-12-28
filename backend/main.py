from kamchatka.net.server import Server


if __name__ == '__main__':

    server = Server()
    try:
        #server.browse()
        server.run_server()
    except KeyboardInterrupt:
        server.stop_server()

