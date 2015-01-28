In [1]: class A(object):
   ...:     data = "Testing"
   ...:     def __init__(self, data):
   ...:          self.data = data
   ...:

In [2]: other = A("Other")

In [3]: A.data
Out[3]: 'Testing'

In [4]: other.data
Out[4]: 'Other'

In [5]: type(other)
Out[5]: __main__.A

In [6]: type(other).data
Out[6]: 'Testing'

In [7]: vars(other)
Out[7]: {'data': 'Other'}

In [8]: vars(A)
Out[8]:
<dictproxy {'__dict__': <attribute '__dict__' of 'A' objects>,
 '__doc__': None,
 '__init__': <function __main__.__init__>,
 '__module__': '__main__',
 '__weakref__': <attribute '__weakref__' of 'A' objects>,
 'data': 'Testing'}>

In [9]: del other.data

In [10]: vars(other)
Out[10]: {}

In [11]: other.data
Out[11]: 'Testing'
