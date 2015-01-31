In [1]: %paste
# coding: utf-8
from random import choice, randint
from string import ascii_lowercase

def mastermind(guess, secret):
    """
    Compara as strings de entrada e devolve um par de inteiros
    (caracteres corretos na posição correta,
     caracteres corretos se desconsiderarmos a posição)

    Origem: https://gist.github.com/danilobellini/5311427
    """
    return sum(1 for g, s in zip(guess, secret) if g == s), \
           sum(min(guess.count(x), secret.count(x)) for x in set(secret))

class NameMastermind(object):
    def __init__(self):
        size = randint(3, 8)
        name = "".join(choice(ascii_lowercase) for el in xrange(size))
        self._name = name
        setattr(self, name, lambda: "Yeah!")
    def __getattr__(self, name):
        return lambda: mastermind(name, self._name)

## -- End pasted text --                                                                                                                            
In [2]: game = NameMastermind()

In [3]: game.abcd()
Out[3]: (0, 1)

In [4]: game.a()
Out[4]: (0, 0)

In [5]: game.b()
Out[5]: (0, 1)

In [6]: game.ab()
Out[6]: (0, 1)

In [7]: game.aab()
Out[7]: (1, 1)

In [8]: game.efgh
Out[8]: <function __main__.<lambda>>

In [9]: game.efgh()
Out[9]: (0, 0)

In [10]: game.efghA()
Out[10]: (0, 0)

In [11]: game.ijkl()
Out[11]: (0, 0)

In [12]: game._name
Out[12]: 'urbrsr'

In [13]: game.urbrst()
Out[13]: (5, 5)

In [14]: game.urbrrs()
Out[14]: (4, 6)

In [15]: game.urbrsr()
Out[15]: 'Yeah!'

In [16]: game2 = NameMastermind()

In [17]: game2._name
Out[17]: 'vxbjqzy'

In [18]: game2.urbrsr()
Out[18]: (1, 1)

In [19]: from string import Template

In [20]: Template.__metaclass__
Out[20]: string._TemplateMetaclass

