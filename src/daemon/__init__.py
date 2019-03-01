import time
import os
import psutil

from src.context import Context

class Daemon:
    def __init__(self, args):
        self.args = args
        self.pid_file = "%s/daemon.pid" % Context.get("DATA_DIR")
        self.stop_file = "%s/daemon.stop" % Context.get("DATA_DIR")

    @property
    def pid_file_exists(self):
        return os.path.isfile(self.pid_file)

    @property
    def stop_file_exists(self):
        return os.path.isfile(self.stop_file)

    @property
    def pid_exists(self):
        if self.pid_file_exists:
            _pid = self.get_pid
            if _pid:
                return _pid.status() == psutil.STATUS_RUNNING
        return False

    @property
    def get_pid(self):
        if self.pid_file_exists:
            _pid = self.pid
            if _pid > 0:
                try:
                    return psutil.Process(self.pid)
                except:
                    self.log("Unable to find pid %s" % str(_pid))
        return None

    @property
    def pid(self):
        if self.pid_file_exists:
            with open(self.pid_file, 'r') as f:
                return int(f.read())
        return 0

    def log(self, msg):
        print("[ PID: %s ] DAEMON: %s" % (str(os.getpid()), msg))

    def create_pid(self):
        if self.pid_exists:
            raise Exception("Already running")

        with open(self.pid_file, 'w') as f:
            f.write(str(os.getpid()))

        return self.pid_exists

    def stop(self):
        if not self.stop_file_exists and self.pid_exists:
            with open(self.stop_file, "w") as f:
                f.write(" ")
            return True
        return False

    def runner(self):
        self.log("Runner...")

    def check_for_stop(self):
        return os.path.isfile(self.stop_file)

    def cleanup(self):
        self.log("Cleanup...")
        if self.pid_exists:
            os.unlink(self.pid_file)

        if self.stop_file_exists:
            os.unlink(self.stop_file)

    def run(self):
        self.create_pid()

        while True:
            self.runner()

            if self.stop_file_exists:
                self.log("Stoping...")
                break

            time.sleep(1)

        # cleanup files
        self.cleanup()
