# coding: utf-8
import dis, sys
from types import CodeType, FunctionType
PY2 = sys.version_info.major == 2

# Vamos trocar o operador ** em f:
f = lambda x, y: x ** 2 + y
fc = f.func_code if PY2 else f.__code__
print(f(5, 7)) # 32

dis.dis(f) # "Disassembly" do bytecode Python
#  7           0 LOAD_FAST                0 (x)
#              3 LOAD_CONST               1 (2)
#              6 BINARY_POWER
#              7 LOAD_FAST                1 (y)
#             10 BINARY_ADD
#             11 RETURN_VALUE

# Exibe os valores do bytecode em hexadecimal
code = fc.co_code
if PY2:
    code = map(ord, code)
print(" ".join("%02x" % val for val in code))
# 7c 00 00 64 01 00 13 7c 01 00 17 53
#                   ^^
#                   Valor que queremos mudar

# Armazena os valores do objeto code
kws = {el[3:]: getattr(fc, el)
       for el in dir(fc) if el.startswith("co_")}

# Troca o primeiro BINARY_POWER por BINARY_ADD
kws["code"] = kws["code"].replace(b"\x13", b"\x17", 1)

# Ordena os valores do objeto code e cria o novo code
args = [kws[p] for p in ["argcount", "nlocals",
        "stacksize", "flags", "code", "consts",
        "names", "varnames", "filename", "name",
        "firstlineno", "lnotab", "freevars",
        "cellvars"]]
if not PY2:
    args.insert(1, 0) # No keyword-only argument
new_code = CodeType(*args)

# Cria a nova função
ftpl = "func_%s" if PY2 else "__%s__"
fparams = ["globals", "name", "defaults", "closure"]
fargs = (getattr(f, ftpl % n) for n in fparams)
new_f = FunctionType(new_code, *fargs)

# Voilà!
dis.dis(new_f)
#  7           0 LOAD_FAST                0 (x)
#              3 LOAD_CONST               1 (2)
#              6 BINARY_ADD
#              7 LOAD_FAST                1 (y)
#             10 BINARY_ADD
#             11 RETURN_VALUE

print(new_f(5, 7)) # 14
# Efetivamente lambda x, y: x + 2 + y
