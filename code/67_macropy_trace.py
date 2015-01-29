# Digitar no REPL antes de começar a usar
import macropy.console

from macropy.tracing import macros, trace

def first_primes():
  yield 2
  yield 3
  yield 5
  yield 7

with trace:
    prod = 1
    for i in first_primes():
        prod = prod * (i ** 2)

# Saída fornecida:

#prod = 1
#for i in first_primes():
#    prod = prod * (i ** 2)
#first_primes() -> <generator object first_primes at 0x7f83c08266e0>
#prod = prod * (i ** 2)
#i ** 2 -> 4
#prod * (i ** 2) -> 4
#prod = prod * (i ** 2)
#i ** 2 -> 9
#prod * (i ** 2) -> 36
#prod = prod * (i ** 2)
#i ** 2 -> 25
#prod * (i ** 2) -> 900
#prod = prod * (i ** 2)
#i ** 2 -> 49
#prod * (i ** 2) -> 44100
