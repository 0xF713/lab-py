a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

if a == b or a == c or b == c:
    print("Ошибка")
else:
    average = (a + b + c) / 3
    print("Среднее =", average)