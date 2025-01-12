import math
D = 2 * math.sqrt(int(input('Введите площадь круга: '))/math.pi)
a = math.sqrt(2)*(int(input('Введите площадь квадрата: '))/4)
if D <= a:
    print('Входит')
else:
    print('Не входит')
    