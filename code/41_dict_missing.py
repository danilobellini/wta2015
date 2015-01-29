# coding: utf-8
from __future__ import unicode_literals
# Vamos remover acentos!
class DictDefaultsToKey(dict):
    def __missing__(self, key):
        return key

rev_ascii = {
  "a": "áàãâāäă", "A": "ÁÀÃÂĀÄĂ",
  "e": "éèẽêēëĕ", "E": "ÉÈẼÊĒËĔ",
  "i": "íìĩîīïĭ", "I": "ÍÌĨÎĪÏĬ",
  "o": "óòõôōöŏ", "O": "ÓÒÕÔŌÖŎ",
  "u": "úùũûūüŭ", "U": "ÚÙŨÛŪÜŬ",
  "c": "ç",       "C": "Ç",
  "n": "ñ",       "N": "Ñ",
}

ascii_dict = DictDefaultsToKey()
for k, values in rev_ascii.items():
    ascii_dict.update((v, k) for v in values)

def to_ascii(msg):
    return "".join(ascii_dict[ch] for ch in msg)

# Exemplos
to_ascii("La cédille: ç/Ç (Forçação de barra)")
to_ascii("Qui a décidé d'être naïf?")
to_ascii("ñÑãÃsáÁüúù...")
