

class Property:
    def __init__(self, val, name=None):
        self.value = val
        self.name = name

    def get_value(self, def_value=None):
        return self.value if self.value is not None else def_value

    def get_name(self):
        return self.name

    def set_value(self, v):
        self.value = v
        return self

    def set_name(self, n):
        self.name = name
        return self

    def get_subproperty(self, char='='):
        p = Property()
        data = self.get_value().split(char, 1)
        if len(data) != 2:
            raise Error("Can not get subproperty")

        p.set_name(data[0])
        p.set_value(data[1])
        return p
