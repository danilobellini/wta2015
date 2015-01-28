class A(object):
    data = "Testing"
    def __init__(self, data):
        self.data = data

other = A("Other")

# Digitar no IPython:
A.data
other.data
type(other) # other.__class__
type(other).data
vars(other)
vars(A)

# E se apagarmos da instância?
del other.data
vars(other)
other.data
