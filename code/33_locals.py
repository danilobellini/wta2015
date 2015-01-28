from math import factorial

for i in range(35):
    locals()["f%d" % i] = factorial(i)

print(f0) # 1
print(f1) # 1
print(f5) # 120
print(f15) # 1307674368000

print(dir()) # Como script, Python 2:
#['__builtins__', '__doc__',
# '__file__', '__name__',
# '__package__', 'f0', 'f1', 'f10',
# 'f11', 'f12', 'f13', 'f14', 'f15',
# 'f16', 'f17', 'f18', 'f19', 'f2',
# 'f20', 'f21', 'f22', 'f23', 'f24',
# 'f25', 'f26', 'f27', 'f28', 'f29',
# 'f3', 'f30', 'f31', 'f32', 'f33',
# 'f34', 'f4', 'f5', 'f6', 'f7',
# 'f8', 'f9', 'factorial', 'i']
