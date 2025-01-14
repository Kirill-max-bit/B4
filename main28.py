x = int(input("введите трёхзначное число: "))

a1 = x // 100
a2 = x // 10 % 10
a3 = x % 10

if a1 > a3:
    print('Первая')
else:
    print('Последняя')

if a1 > a2:
    print('Первая')
else:
    print('Вторая')

if a2 > a3:
    print('Вторая')
else:
    print('Последняя')
