# coding: utf-8
template = u"{level} ({author}): {msg}"

print(template.format(
    msg = u"Isto não é uma mensagem.",
    level = u"Info",
    author = u"Danilo",
)) # Exibe:
# Info (Danilo): Isto não é uma mensagem.

msg = u"Contexto como parâmetro?"
level = u"Dinâmico"
author = u"Locals!"

print(template.format(**locals())) # Exibe:
# Dinâmico (Locals!): Contexto como parâmetro?
