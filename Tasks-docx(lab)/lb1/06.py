n = int(input("Введите число n = "))

years = n // 365
remainder = n % 365

months = remainder // 30
days = remainder % 30

print(f"Годы: {years} Месяцы: {months} Дни: {days}")