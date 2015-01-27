ops = {
    "+": lambda x, y: x + y,
    "-": lambda x, y: x - y,
    "%": lambda x, y: x % y,
}

print(ops["+"](2, 3))
print(ops["-"](5, 7))
print(ops["%"](22, 13))
