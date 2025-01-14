number = int(input("Введите двузначное число: "))


first_digit = number // 10
second_digit = number % 10


if first_digit > second_digit:
    print(f"Первая цифра {first_digit} больше второй {second_digit}")
elif first_digit < second_digit:
    print(f"Вторая цифра {second_digit} больше первой {first_digit}")
else:
    print("Цифры равны")
