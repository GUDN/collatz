from functools import wraps


class ValueKeepingGenerator:
    def __init__(self, g):
        self.g = g
        self.value = None

    def __iter__(self):
        self.value = yield from self.g


def keep_value(func):
    @wraps(func)
    def g(*args, **kwargs):
        return ValueKeepingGenerator(func(*args, **kwargs))

    return g
