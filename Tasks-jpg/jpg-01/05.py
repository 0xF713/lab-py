import math

x = float(input("x = "))

if x != 0:
    result = math.sqrt(x + 3/x)
    print("result = ", result)
else:
    print("problems = (x == 0)")