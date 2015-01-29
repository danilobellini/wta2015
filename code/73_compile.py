# coding: utf-8
from types import CodeType, FunctionType

source = """print('Hello World')"""
fname = "<string>"
mode = "single" # exec   -> module
                # single -> statement
                # eval   -> expression
code = compile(source, fname, mode)

exec(code) # Hello World
print(isinstance(code, CodeType)) # True

# Criando uma função (para não usar o exec)
name = "hw"
defaults = tuple()
hw = FunctionType(code, locals(), name,
                  defaults, None)
hw() # Hello World