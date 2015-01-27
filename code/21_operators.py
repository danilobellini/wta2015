def add(x, y): return x + y
def sub(x, y): return x - y
def mod(x, y): return x % y

ops = {
    "+": add,
    "-": sub,
    "%": mod,
}

def apply_op(symbol, x, y):
    return ops[symbol](x, y)

print(apply_op("+", 2, 3))   # 5
print(apply_op("-", 5, 7))   # -2
print(apply_op("%", 22, 13)) # 9
