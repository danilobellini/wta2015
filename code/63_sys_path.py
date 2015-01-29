import os, sys

# Primeiro diretório de sys.path é o
# "." de quando o script foi chamado.

os.chdir("..") # Isto é irrelevante
for name in sys.path:
    print(name)

#/home/danilo/Desktop/WTA/code
#[...]
