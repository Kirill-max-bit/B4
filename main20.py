m = int(input("Введите m: "))
n = int(input("Введите n: "))
d, r = divmod(m, n)
print("не делится" if r else d)
