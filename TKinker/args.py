from unittest import result


def add(*args):
    result = 0
    for n in args:
        result += n
    return result


print(add(7, 8, 99))


def calc(n, **kwargs):
    print(kwargs)

    n += kwargs["add"]
    print(n)


calc(5, add=3, multi=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
