n = input("Введите число: ").zfill(4)
print('Все цифры различны' if len(set(n)) == 4 else 'Не все цифры различны')
