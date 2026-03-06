import math

def f(x):
    return (math.exp(x) - math.exp(-x)) / (math.exp(x) + math.exp(-x))

# a)
x1 = 1
print("x = 1:", f(x1))

# b)
x2 = math.log(2)
print("x = ln(2):", f(x2))

# c)
x3 = -4
print("x = -4:", f(x3))

# Короткий вариант
# import math
# for x in [1, math.log(2), -4]:
# print(f"x = {x:.4f} -> y = {math.tanh(x):.4f}")