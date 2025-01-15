def check_brick_fit(a, b, c, x, y):
    if (a <= x and b <= y) or (a <= y and b <= x):
        return True
    if (a <= x and c <= y) or (a <= y and c <= x):
        return True
    if (b <= x and c <= y) or (b <= y and c <= x):
        return True

    return False


a = float(input("Введите длину кирпича: "))
b = float(input("Введите ширину кирпича: "))
c = float(input("Введите высоту кирпича: "))
x = float(input("Введите ширину отверстия: "))
y = float(input("Введите высоту отверстия: "))

if check_brick_fit(a, b, c, x, y):
    print("Кирпич пройдет в отверстие.")
else:
    print("Кирпич не пройдет в отверстие.")