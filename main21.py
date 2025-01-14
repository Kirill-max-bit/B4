a = int(input("Введите число: "))
b = int(input("Введите число: "))

if a % b == 0:
    print("да")
else:
    print("Нет")
    print("Остаток от деления: ", a % b)
