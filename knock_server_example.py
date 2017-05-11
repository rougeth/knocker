import socketserver
import threading
import time


class ThreadedTCPRequestHandler(socketserver.BaseRequestHandler):

    def handle(self):
        _, server_port = self.request.getsockname()
        print('Ping on {}'.format(server_port))


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass


if __name__ == '__main__':

    servers = []
    for _ in range(3):
        server = ThreadedTCPServer(('localhost', 0), ThreadedTCPRequestHandler)
        server_thread = threading.Thread(target=server.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        servers.append(server)

    ports = [server.server_address[1] for server in servers]
    print('Listening ports: {} {} {}'.format(*ports))

    try:
        while 1:
            time.sleep(1)
    except KeyboardInterrupt:
        print()  # Jumps ^C char
        for server in servers:
            print('Shutdown {}'.format(server.server_address[1]))
            server.shutdown()
