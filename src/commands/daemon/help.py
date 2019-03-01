__main_desc=r"""

Manages daemon. Commands

    status          - Prints status
    start           - Starts daemon
    stop            - Stops daemon
    restart         - Restarts daemon
    help            - Prints this message

Options
    -v | --verbose  - Debug deamon output

""".strip()

def help():
    print(__main_desc)
    return True
