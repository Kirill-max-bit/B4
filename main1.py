import math

def calculate_y(x):
    if x == 0:
        return math.sin(x)
    else:
        return 2 * math.sin(x)

try:
    x = float(input("Введите значение x: "))
except ValueError:
    print("Ошибка ввода! Введено нечисловое значение.")
else:
    result = calculate_y(x)
    print(f"При x = {x}, y = {result}")
