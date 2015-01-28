# Função geradora
def count(start=0, step=1):
    while True:
        yield start
        start += step

# Geradores são iteradores
gen = count()
next(gen)
next(gen)
next(gen)
gen_impares = count(1, step=2)
next(gen_impares)
next(gen_impares)
next(gen_impares)
next(gen)

# Expressão geradora
g = (el ** 2 for el in count(3)
             if el % 3 == 0)
next(g)
next(g)
next(g)

# Iteradores são iteráveis
for el in count(5, 3):
    print(el)
    if el >= 30:
        break
