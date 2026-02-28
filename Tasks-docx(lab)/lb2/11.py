x = float(input("Введите x: "))

if -1 <= x <= 1:
    if x >= 0:
        y = x ** (1/3)
    else:
        y = -(-x) ** (1/3)
else:
    y = abs(x)

print("y =", y)