# Apenas Python 2
from types import CodeType, FunctionType

def change_internal_name(func, old, new):
  fc = func.func_code
  kws = {el[3:]: getattr(fc, el)
         for el in dir(fc) if el.startswith("co_")}
  kws["names"] = tuple(new if el == old else el
                       for el in kws["names"])
  args = (kws[p] for p in ["argcount", "nlocals",
          "stacksize", "flags", "code", "consts",
          "names", "varnames", "filename", "name",
          "firstlineno", "lnotab", "freevars",
          "cellvars"])
  return FunctionType(CodeType(*args),
           func.func_globals, func.func_name,
           func.func_defaults, func.func_closure)

a, b = 32, 42
def test():
    return b
print test()
print change_internal_name(test, old="b", new="a")()
print test()
test = change_internal_name(test, old="b", new="a")
print test()
test = change_internal_name(test, old="a", new="b")
print test()

# 42 (b)
# 32 (a)
# 42 (b)
# 32 (a)
# 42 (b)
