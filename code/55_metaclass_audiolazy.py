from audiolazy import AbstractOperatorOverloaderMeta, meta

class PairMetaClass(AbstractOperatorOverloaderMeta):
    __without__ = "r" # Sem ops reversos __rbinary__

    def __binary__(cls, opmeth):
        return lambda self, other: \
            cls(opmeth.func(self.x, other.x),
                opmeth.func(self.y, other.y))

    def __unary__(cls, opmeth):
        return lambda self: \
            cls(opmeth.func(self.x),
                opmeth.func(self.y))

class Pair(meta(object, metaclass=PairMetaClass)):
    def __init__(self, x, y):
        self.x, self.y = x, y
    def __str__(self):
        return "({}, {})".format(self.x, self.y)

print(Pair(4, 3) - Pair(7, 12))
print(Pair(41, 5) + Pair(18, 3))
print(Pair("a", "bc") + Pair("de", "f"))
print(Pair([1, 2], "abc") * Pair(2, 3))
