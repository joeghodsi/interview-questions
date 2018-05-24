class Singleton:
    def __init__(self, decorated):
        self._decorated = decorated

    def instance(self):
        if not hasattr(self, '_instance'):
            self._instance = self._decorated()
        return self._instance

    def __call__(self):
        raise TypeError('Singletons must be accessed through `instance()`.')

    def __instancecheck__(self, inst):
        return isinstance(inst, self._decorated)
