class Context:
    def __init__(self):
        raise Error("Can not have instance")

    @staticmethod
    def __data(name=None, val=None):
        if not hasattr(Context, 'runtime_data'):
            setattr(Context, 'runtime_data', dict())

        if name is not None:
            Context.runtime_data[name] = val

        return Context.runtime_data

    @staticmethod
    def has(name):
        return True if name in Context.__data() else False

    @staticmethod
    def set(name, val):
        Context.__data(name, val)

    @staticmethod
    def get(name):
        if Context.has(name):
            return Context.__data()[name]
        return None

    @staticmethod
    def data():
        return Context.__data()
