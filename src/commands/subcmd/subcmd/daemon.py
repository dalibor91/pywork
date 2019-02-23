from src.daemon import Daemon

def daemon(args):
    daemon = Daemon(args)
    daemon.run()
