# coding: utf-8
from itertools import count, takewhile, tee

def prime_gen():
    """ Gerador de números primos """
    yield 2
    primes = []
    for value in count(start=3, step=2):
        iter_primes = takewhile(lambda x: x * x <= value, primes)
        if all(value % p != 0 for p in iter_primes):
            primes.append(value)
            yield value

primes, primes_copy = tee(prime_gen(), 2)

for idx, p in enumerate(primes, 1):
    print(u"{:>5}º primo: {}".format(idx, p))
    if idx == 200:
        break

for idx, p in enumerate(primes_copy, 1):
    print(u"{:>5}º primo ao quadrado: {}".format(idx, p ** 2))
    if idx == 200:
        break
