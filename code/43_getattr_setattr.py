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

game = NameMastermind()
# Para rodar no REPL...
# NÃO APERTE TAB! Exemplo:
#game.abcd() # -> (0, 0)
#game.efgh() # -> (1, 2)
#game.eeff() # -> (0, 0)
#game.ijkh() # -> (1, 1)
#game.lmno() # -> (0, 1)
#game.lmpq() # -> (0, 1)
#game.lmgq() # -> (0, 2)
#game.lmqg() # -> (0, 2)
#game.rstu() # -> (0, 0)
#game.vwxy() # -> (0, 1)
#game.lgzh() # -> (1, 3)
#game.gmvh() # -> (2, 2)
#game.glwh() # -> 'Yeah!'
