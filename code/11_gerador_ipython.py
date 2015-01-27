In [1]: def count(start=0, step=1):
   ...:     while True:
   ...:         yield start
   ...:         start += step
   ...:

In [2]: gen = count()

In [3]: next(gen)
Out[3]: 0

In [4]: next(gen)
Out[4]: 1

In [5]: next(gen)
Out[5]: 2

In [6]: gen_impares = count(1, step=2)

In [7]: next(gen_impares)
Out[7]: 1

In [8]: next(gen_impares)
Out[8]: 3

In [9]: next(gen_impares)
Out[9]: 5

In [10]: next(gen)
Out[10]: 3

In [11]: g = (el ** 2 for el in count(3)
   ...:               if el % 3 == 0)
   ...:

In [12]: next(g)
Out[12]: 9

In [13]: next(g)
Out[13]: 36

In [14]: next(g)
Out[14]: 81

In [15]: for el in count(5, 3):
   ....:     print(el)
   ....:     if el >= 30:
   ....:         break
   ....:
5
8
11
14
17
20
23
26
29
32
