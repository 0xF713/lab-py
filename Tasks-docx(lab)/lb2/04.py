import math

x = float(input("x = "))

if x > 0:
    y = math.log(x)
else:
    y = 3 * x - 2

print("y = ", y)