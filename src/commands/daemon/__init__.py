from time import sleep
from .help import help
from src.daemon import Daemon

from src.commands.subcmd import command
from src.commands.subcmd import output


def process(argv):
    if argv.has('help', prefix='') or argv.has('help') or argv.has('h'):
        return help()

    _daemon = Daemon(argv)

    if argv.has('status', prefix=''):
        if _daemon.pid_exists:
            print("RUNNING (PID: %s)" % str(_daemon.pid))
        else:
            print("NOT RUNNING")
        return True

    output().null_output()
    
    if argv.has('start', prefix=''):
        return command('subcmd --target daemon')

    if argv.has('stop', prefix=''):
        if _daemon.pid_exists:
            _daemon.stop()

    if argv.has('restart', prefix=''):
        if _daemon.pid_exists:
            _daemon.stop()
            cnt =0
            while True:
                if not _daemon.pid_exists:
                    return command('subcmd --target daemon')
                
                if cnt > 100:
                    print("Unable to restart ")
                    break
                
                cnt += 1
                
                sleep(1)
        else:
            command('subcmd --target daemon')
            
    return True
