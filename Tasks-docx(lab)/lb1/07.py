import numpy as np

# Ввод x с клавиатуры
x = float(input("Введите x: "))

print("|2 + 3x| =", np.abs(2 + 3*x))
print("sin(2πx) =", np.sin(2 * np.pi * x))
print("e^(2x) =", np.exp(2 * x))
print("ln(x^3) =", np.log(x**3))
print("sqrt(x + 3/x) =", np.sqrt(x + 3/x))
print("arctg(3x) =", np.arctan(3 * x))