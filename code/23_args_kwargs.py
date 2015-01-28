def smaller_first(pair):
    k, v = pair
    return len(k), k
def show_it_all(a, b, c=None, *args, **kwargs):
    for k, v in sorted(locals().items(), key=smaller_first):
        print("{:>6}: {}".format(k, v))

# Rodar no REPL
squares = [i ** 2 for i in range(10)]
ascii = {ch: hex(ord(ch)) for ch in "Place"}

show_it_all(0, -1)
show_it_all(b=0, a=-1)
show_it_all(*squares)
show_it_all(*"First")
show_it_all(1, 2, 3, 4, 5, d=415)
show_it_all(-5, *squares, args=415)
show_it_all(b="Second", **ascii)

# TypeError
show_it_all("First", **ascii)   # "a" 2x
show_it_all(*squares, **ascii)  # "a" 2x
show_it_all(1, 2, 3, 4, 5, b=5) # "b" 2x
show_it_all(b=5, e=0, **ascii)  # "e" 2x
show_it_all(**ascii) # "b" ausente
show_it_all(0)       # "b" ausente
show_it_all()        # "a" ausente
