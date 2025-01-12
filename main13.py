def has_real_roots(a, b, c):
    D = b**2 - 4*a*c

    if D > 0:
        print("Уравнение имеет два вещественных корня.")
    elif D == 0:
        print("Уравнение имеет один вещественный корень.")
    else:
        print("Уравнение не имеет вещественных корней.")


a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))

has_real_roots(a, b, c)
