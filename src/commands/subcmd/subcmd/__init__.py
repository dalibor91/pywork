import time
import sys

# just a test for executing commands
def dosleep(args):
    seconds = args.get_property('seconds')
    worker = args.get_property('worker_id')
    _worker = worker.get_value() if worker is not None else ""

    if worker is None or _worker == "0":
        print("") # just clean row

    _seconds = int(seconds.get_value()) if seconds is not None else 5
    for i in range(0, _seconds):
        if worker is None:
            print("Sleeping %s | %s" % (str(i).ljust(5), str(sys.argv)))
        else:
            print("Worker %s | Sleeping %s | %s" % (_worker.ljust(5), str(i).ljust(5), str(sys.argv)))
        time.sleep(1)
    print("Done. %s" % (_worker if worker is not None else ""))
