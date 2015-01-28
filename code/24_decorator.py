# coding: utf-8
from functools import wraps, reduce

def double_of(func):
    """Decorator que dobra o resultado da função."""
    @wraps(func) # Copia informações de func
    def wrapper(*args, **kwargs):
        return 2 * func(*args, **kwargs)
    return wrapper

sum_twice = double_of(sum)
print(sum_twice([2, 5, 3])) # 20

@double_of
def prod_twice(data):
    return reduce(lambda x, y: x * y, data, 1)

print(prod_twice([2, 5, 3])) # 60

# A menos dos nomes, o acima é o mesmo que:
def prod(data):
    return reduce(lambda x, y: x * y, data, 1)
prod2x = double_of(prod) # Decorator!

print(prod2x([2, 5, 3])) # 60
