import sys # Para funcionar em Python 2 e 3
if sys.version_info.major == 2:
    from cachetools import lru_cache
else:
    from functools import lru_cache

@lru_cache(maxsize=1000)
def fib(n):
    return n if n <= 1 else fib(n - 2) + fib(n - 1)

print(fib(500))
