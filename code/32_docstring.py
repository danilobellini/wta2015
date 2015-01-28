# coding: utf-8
def is_palindrome(val):
    """
    Verifica se a representação do valor
    fornecido é um palíndromo
    """
    as_string = repr(val)
    return as_string == as_string[::-1]

# Rodar em um REPL
is_palindrome(123213) # False
is_palindrome(123321) # True

help(is_palindrome) # Exibe a docstring e
                    # outras informações

is_palindrome.__doc__ # Devolve a docstring
#\n
#----Verifica se a representação do valor\n
#----fornecido é um palíndromo\n
#----
