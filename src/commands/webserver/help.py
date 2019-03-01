__main_desc=r"""

Manages webserver. Commands

    status          - Prints status
    run             - Starts daemon

Options
    -v   | --verbose       - Debug deamon output
    -get | --get     [url] - Sends GET  request
    -post| --post    [url] - Sends POST request
    -body| --body   [body] - Body for request

""".strip()

def help():
    print(__main_desc)
    return True
