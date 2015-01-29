# -*- coding: utf-8 -*-
from functools import reduce
from operator import add, mul

class SumProd(object):
    def __init__(self):
        self.count = 0

    def __getitem__(self, key): # 1 argumento!
        """Somatório (não-vazio)"""
        self.count += 1
        return reduce(add, key)

    def __call__(self, *key):
        """Produtório (não-vazio)"""
        self.count += 1
        return reduce(mul, key)

sp = SumProd()
print(  sp(3, 4, 5)  ) # __call__    -> 60
print(  sp[3, 4, 5]  ) # __getitem__ -> 12

print(sp.count) # 2
