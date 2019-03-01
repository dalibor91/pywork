import http

from urllib.parse import urlparse
from .controllers import controller

# curl -s --unix-socket data/daemon.sock -X GET "http://daemon/asdf?Asd"
class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return controller(urlparse(self.path), self)

    def do_POST(self):
        return controller(urlparse(self.path), self)

    def do_HEAD(self):
        return controller(urlparse(self.path), self)

