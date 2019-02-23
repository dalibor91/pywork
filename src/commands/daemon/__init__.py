from .help import help
from .daemon import Daemon

_daemon = Daemon()

def process(argv):
    if argv.has('help', prefix=''):
        return help()

    if argv.has('status', prefix=''):
        return True

    if argv.has('start', prefix=''):
        return True

    if argv.has('stop', prefix=''):
        return True

    return True
