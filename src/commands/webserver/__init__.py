from .help import help

# bin/run webserver run --post --url "/test/?q=1" --body "[1,2,3]"
# bin/run webserver run --get --url "/test/?q=1"

def process(argv):
    if argv.size == 0 or \
        argv.has('help', prefix='') or \
        argv.has('help') or \
        argv.has('h', prefix='-'):
        return help()
