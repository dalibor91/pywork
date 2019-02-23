import sys
import os

from importlib import import_module
from random import randint
from subprocess import Popen

class __Output:
    def __init__(self):
        self.outfile = sys.stdout
        self.errfile = sys.stderr

    def null_output(self):
        self.outfile = self.errfile = open(os.devnull, "w")

    def file_output(self, file):
        self.outfile = open("%s.log" % file, "a")
        self.errfile = open("%s.err" % file, "a")

__out = __Output()

# executes command in shell
def __cmd(cmd):
    # print("Executing: %s" % ("python run.py %s" % cmd))
    _proc = Popen(("python run.py %s" % cmd).split(" "), stdout=__out.outfile, stderr=__out.errfile);

    if _proc.pid:
        print("Starting worker with pid: %s" % str(_proc.pid))

    return _proc

# spawns multiple workers
def __worker(cmd, spawn_number=1):
    _suc = True
    for i in range(0, spawn_number):
        _proc = __cmd("subcmd %s --worker_id %d" % (cmd, i))
        if not _proc:
            _suc = _suc and False
    return _suc


# run
# python run.py subcmd --run "--dosleep 15"
# to execute command in separate spawned process for testing purposes
# or run
# python run.py subcmd --worker "--dosleep 15" --number 3
# to execute command in 3 separate workers for testing purposes
# python run.py subcmd --worker "--dosleep 15" --number 3 --output file_path
# python run.py subcmd --worker "--dosleep 15" --number 3 --noout
def process(argv):
    # handle output
    if argv.has_value('output'):
        __out.file_output(argv.get_property('output').get_value())

    # output to dev null
    if argv.has('noout'):
        __out.null_output()

    # run just simple command
    if argv.has('run'):
        return True if __cmd("subcmd %s" % argv.get_property('run').get_value()) else False

    # run multiple workers
    if argv.has('worker'):
        spawn_number = argv.get_property('number')
        return __worker(argv.get_property('worker').get_value(), spawn_number=int(spawn_number.get_value(1) if spawn_number else 1))

    if argv.has_value('target'):
        target = argv.get_property('target').get_value()

        try:
            mdl = import_module('%s.subcmd' % __name__)
            return getattr(mdl, target)(argv)
        except Exception as e:
            print("Unable to load '%s' in '%s' -> %s" % (target, ('%s.subcmd' % __name__), str(e)))
            raise e

    return True

def command(cmd):
    return __cmd(cmd)
