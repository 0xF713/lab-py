a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

D = b**2 - 4*a*c

print("D =", D)

if D < 0:
    print("Корней нет")
else:
    if D == 0:
        x = -b / (2*a)
        print("Один корень x =", x)
    else:
        x1 = (-b + D**0.5) / (2*a)
        x2 = (-b - D**0.5) / (2*a)
        print("Два корня:")
        print("x1 =", x1)
        print("x2 =", x2)