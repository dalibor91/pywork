import socket
from socketserver import TCPServer
from http.server import HTTPServer

class DaemonHTTPServer(HTTPServer):
    address_family = socket.AF_UNIX

    def server_bind(self):
        TCPServer.server_bind(self)
        self.server_name = "daemon_http_server"
        self.server_port = 0
