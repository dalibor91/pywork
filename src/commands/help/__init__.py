__main_desc=r"""

This should be main help message when we don't pass
any arguments

    command     - Help about cmd 1
    command     - Help about cmd 2
    command     - Help about cmd 3
    webserver   - Webserver management
    daemon      - Run Daemon
    help        - This message

""".strip()

def process(argv):
    print(__main_desc)
    return True
