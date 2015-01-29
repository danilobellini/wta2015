# Digitar no REPL antes de começar a usar
import macropy.console

from macropy.string_interp import macros, s
a, b, c = "texto", "sem", "modificar"
s["{b[::-1] + c[:2]} {a}, {c[:-1]}do"]
# Out[1]: 'mesmo texto, modificado'
