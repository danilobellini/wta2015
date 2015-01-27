template = "lambda x, y: x %s y"
ops = {s: eval(template % s) for s in "+-*/%"}

print(ops["+"](2, 3))
print(ops["-"](5, 7))
print(ops["%"](22, 13))
