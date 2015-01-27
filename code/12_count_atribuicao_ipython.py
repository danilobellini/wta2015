In [1]: %paste
from collections import Iterator
# [...]
## -- End pasted text --

In [2]: g = Counter()

In [3]: next(g)
Out[3]: 0

In [4]: next(g)
Out[4]: 1

In [5]: g.value = 13

In [6]: next(g)
Out[6]: 13

In [7]: next(g)
Out[7]: 14

In [8]: g.step = 7

In [9]: next(g)
Out[9]: 15

In [10]: next(g)
Out[10]: 22

In [11]: next(g)
Out[11]: 29

In [12]: counter = Counter(start=-5, step=7)

In [13]: for el in counter:
   ....:     print(el)
   ....:     counter.step -= 1
   ....:     counter.finish = counter.value < -10
   ....:
-5
2
8
13
17
20
22
23
23
22
20
17
13
8
2
-5
