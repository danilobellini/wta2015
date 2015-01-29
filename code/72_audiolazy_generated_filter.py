from audiolazy import z

filt = z ** -2 / (- 2 * z ** -1 + 1)

# Ao usar o filt, ele gerará
def gen(seq, memory, zero):
  m1 , = memory
  d1 = d2 = zero
  for d0 in seq:
    m0 = d2 + --2 * m1
    yield m0
    m1 = m0
    d2 = d1
    d1 = d0
