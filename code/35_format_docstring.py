# coding: utf-8
# Código original na AudioLazy (exceto pela docstring):
def format_docstring(template_="{__doc__}", *args, **kwargs):
    def decorator(func):
        if func.__doc__:
            kwargs["__doc__"] = func.__doc__.format(*args, **kwargs)
        func.__doc__ = template_.format(*args, **kwargs)
        return func
    return decorator

# Exemplo
def adder(a):
    @format_docstring(a=a)
    def add(b):
        """Efetua a soma {a} + b para o dado b."""
        return a + b
    return add

add3 = adder(3)
sub2 = adder(-2)
help(add3) # Efetua a soma 3 + b para o dado b.
help(sub2) # Efetua a soma -2 + b para o dado b.
