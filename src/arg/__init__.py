import importlib

from . import arguments as arg

def process_args(argv, path="src.commands"):
    '''
    Processing arguments with autoload
    Arguments
        argv(list) : list passed from command line
        path(str)  : python library path with modules
    '''

    import_module = 'help'
    if len(argv) > 0:
        import_module = argv[0]

    try:
        mdl = importlib.import_module('%s.%s' % (str(path), str(import_module)))
    except Exception as e:
        mdl = importlib.import_module('%s.help' % str(path))
        print("Error: %s" % str(e))
        #if len(argv) > 0:
        #    Colorized.red("Unknown command '%s'" % " ".join(argv))
    mdl.process(arg.Arguments(argv[1:]))
