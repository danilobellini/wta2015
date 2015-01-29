import sys

class Metaclass(type):
    def __init__(cls, name, bases, namespace):
        print("Initializing class {}\n"
              "bases: {}\n"
              "namespace: {}"
              .format(name, bases, namespace))

if sys.version_info.major == 2: # Python 2
    exec("""class M1(object): __metaclass__ = Metaclass""")
else: # Python 3
    exec("""class M1(object, metaclass=Metaclass): pass""")

# Initializing class M1
# bases: (<class 'object'>,)
# namespace: {'__module__': '__main__', ...}

# Similar: M1 = Metaclass("M1", (object,), {})
# (mas o namespace resultante nem '__module__' possui)
