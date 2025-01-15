a = int(input("Введите длину конверта (мм): "))
b = int(input("Введите ширину конверта (мм): "))
c = int(input("Введите длину открытки (мм): "))
d = int(input("Введите ширину открытки (мм): "))


c_with_margin = c - 2
d_with_margin = d - 2


if (c_with_margin <= a and d_with_margin <= b) or (c_with_margin <= b and d_with_margin <= a):
    print("Открытка поместится в конверт.")
else:
    print("Открытка не поместится в конверт.")
