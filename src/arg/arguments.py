from .property import Property

class Arguments:
    def __init__(self, data):
        self.argv = data

    def dump(self):
        print(self.argv)

    def has(self, c):
        '''
        Check if arguments have this parameters
        :param c: list or one paramentr
        :return: boolean True or False
        '''
        if isinstance(c, str):
            return True if self.get_property(c) is not None else False
        elif isinstance(c, set):
            for item in c:
                if self.get_property(item) is None:
                    return False
            return True
        return False

    def has_value(self, c):
        return self.has(c) and (self.get_property(c).get_value() != '')

    def get_property(self, name, prefix='--'):
        found = False
        for arg in self.argv:
            if found:
                return Property(arg, name)
            if ("%s%s"%(prefix,name)) == arg:
                found = True
        return Property("", name) if found else None

    def get_property_arr(self, name, prefix='--'):
        found = []
        _found = False
        for arg in self.argv:
            if _found:
                found.append(Property(arg, name))
                _found = False
                continue
            if ("%s%s"%(prefix,name)) == arg:
                _found = True

        return found
