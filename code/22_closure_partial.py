def adder(a):
    return lambda b: b + a

add2 = adder(2)
sub1 = adder(-1)

print(add2(15))      # 17
print(sub1(4))       # 3
print(add2(sub1(8))) # 9
