A = type("A", (object,), {"__str__": lambda self: "A"})
B = type("B", (A,),      {"__str__": lambda self: "B"})
C = type("C", (A,),      {"__str__": lambda self: "C"})
D = type("D", (B, C),    {"__str__": lambda self: "D"})
# Já com os métodos __str__ no namespace! [...]

classes = [A, B, C, D]
instances = [cls() for cls in classes]

def msg_returner(msg):
    return lambda self: msg

def show_all():
    print("{} {} {} {}".format(*instances))

show_all() # A B C D
del C.__str__
show_all() # A B A D
C.__str__ = msg_returner("3")
show_all() # A B 3 D
del D.__str__
show_all() # A B 3 B
del B.__str__
show_all() # A A 3 3
del C.__str__
show_all() # A A A A

print(D.mro())
# [<class '__main__.D'>,
#  <class '__main__.B'>,
#  <class '__main__.C'>,
#  <class '__main__.A'>,
#  <type 'object'>]
