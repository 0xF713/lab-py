import math

a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

count = (a % 2 == 0) + (b % 2 == 0) + (c % 2 == 0)

print("Четные числа = ", count)