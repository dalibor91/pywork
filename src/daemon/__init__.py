import time
import os

from src.context import Context

class Daemon:
    def __init__(self, args):
        self.args = args
        self.pid_file = "%s/.pid" % Context.get("DATA_DIR")

    @property
    def pid_file_exists(self):
        return os.path.isfile(self.pid_file)

    @property
    def pid_exists(self):
        if self.pid_file_exists:
            # todo: more advanced check for windows
            if os.name == 'nt':
                return True

            try:
                os.kill(self.pid, 0)
            except OSError:
                return False
            else:
                return True
        return False

    @property
    def pid(self):
        if self.pid_file_exists:
            with open(self.pid_file, 'r') as f:
                return int(f.read())
        return 0

    def create_pid(self):
        if self.pid_exists:
            raise Exception("Already running")

        with open(self.pid_file, 'w') as f:
            f.write(str(os.getpid()))

        return self.pid_exists

    def remove_pid_file(self):
        if self.pid_exists:
            os.unlink(self.pid_file)

    def run(self):
        self.create_pid()
        cnt=0
        while True:
            print("Daemon check")
            time.sleep(1)
            cnt += 1
            if cnt > 1000:
                break
        self.remove_pid_file()
