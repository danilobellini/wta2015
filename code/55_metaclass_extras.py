# Resultado:
#
#(-3, -9)
#(59, 8)
#(ade, bcf)
#([1, 2, 1, 2], abcabcabc)

# Sintaxe Python 2
class Pair(object):
    __metaclass__ = PairMetaClass
    # [...]

# Sintaxe Python 3
class Pair(object, metaclass=PairMetaClass):
    # [...]

# Exemplo de vars(opmeth):
{'arity': 2,
 'symbol': '+',
 'func': <function
          _operator.add>,
 'name': 'add',
 'dname': '__add__',
 'rev': False}
