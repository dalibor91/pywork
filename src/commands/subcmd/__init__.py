import time
import sys
import subprocess

from random import randint

# executes command in shell
def __cmd(cmd, stdout=sys.stdout, stderr=sys.stderr):
    # print("Executing: %s" % ("python run.py %s" % cmd))
    subprocess.Popen(("python run.py %s" % cmd).split(" "), stdout=sys.stdout, stderr=sys.stderr);

# spawns multiple workers
def __worker(cmd, spawn_number=1):
    for i in range(0, spawn_number):
        __cmd("subcmd %s --worker_id %d" % (cmd, i))

# just a test for executing commands
def __sleep(seconds, worker=None):
    for i in range(0, int(seconds)):
        if worker is None:
            print("Sleeping %s ..." % i)
        else:
            print("Worker %s: Sleeping %s ..." % (worker, i))
        time.sleep(randint(1,seconds))
    print("Done")

# run
# python run.py subcmd --run "--dosleep 15"
# to execute command in separate spawned process for testing purposes
# or run
# python run.py subcmd --worker "--dosleep 15" --number 3
# to execute command in 3 separate workers for testing purposes
def process(argv):
    # run just simple command
    if argv.has('run'):
        return __cmd("subcmd %s" % argv.get_property('run').get_value(10))

    # run multiple workers
    if argv.has('worker'):
        spawn_number = argv.get_property('number')
        return __worker(argv.get_property('worker').get_value(), spawn_number=int(spawn_number.get_value(1) if spawn_number else 1))

    # test command for sleep
    if argv.has('dosleep'):
        worker = argv.get_property('worker_id')
        __sleep(argv.get_property('dosleep').get_value(10), worker.get_value() if worker else None)

    return True
