class NotInstantiatedError(Exception):
    def __init__(self, clsname, msg = None):
        if msg is None:
            msg = "Can't use class '{}' without instantiating.".format(clsname)
        super().__init__(msg)

class ReinstantiateWithArgsError(Exception):
    def __init__(self, clsname, msg = None):
        if msg is None:
            msg = "Reinstantiate without args because the singleton class '{}' has already instantiated.".format(clsname)
        super().__init__(msg)
