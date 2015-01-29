A = type("A", (object,), {"__str__": lambda self: "A"})
B = type("B", (A,),      {"__str__": lambda self: "B"})
C = type("C", (A,),      {"__str__": lambda self: "C"})
D = type("D", (B, C),    {"__str__": lambda self: "D"})

a, b, c, d = A(), B(), C(), D()

print(isinstance(d, A))      # True
print(isinstance(a, (B, C))) # False
print(isinstance(c, (B, C))) # True

print(issubclass(A, B))      # False
print(issubclass(B, A))      # True
print(issubclass(B, (C, D))) # False
