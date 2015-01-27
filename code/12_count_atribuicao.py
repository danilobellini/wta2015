from collections import Iterator

class Counter(Iterator):

    def __init__(self, start=0, step=1):
        self.value = start
        self.step = step
        self.finish = False

    def next(self):
        if self.finish:
            raise StopIteration
        result = self.value
        self.value += self.step
        return result

    __next__ = next # Compatibilidade Python 2/3


g = Counter()
next(g)
next(g)
g.value = 13
next(g)
next(g)
g.step = 7
next(g)
next(g)
next(g)


counter = Counter(start=-5, step=7)
for el in counter:
    print(el)
    counter.step -= 1
    counter.finish = counter.value < -10
