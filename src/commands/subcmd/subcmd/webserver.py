from src.context import Context
from src.webserver import DaemonHTTPServer
from src.webserver.handler import Handler

def webserver(args):
    sock_file = "%s/daemon.sock" % Context.get("DATA_DIR")
    srv = DaemonHTTPServer(sock_file, Handler)
    srv.serve_forever()
