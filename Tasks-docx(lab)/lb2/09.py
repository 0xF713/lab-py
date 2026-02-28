n = int(input("Введите двузначное число: "))

n = abs(n)  # чтобы работало и с отрицательными числами

if 10 <= n <= 99:
    first = n // 10
    second = n % 10
    
    if first == second:
        print("Да")
    else:
        print("Нет")
else:
    print("Число не двузначное")