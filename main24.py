n = int(input("Введите двузначное число: "))
x, y = divmod(n, 10)
print(n*n == 4*(x**3+y**3))
