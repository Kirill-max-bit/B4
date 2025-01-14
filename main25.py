number = int(input("Введите двузначное число: "))


first_digit = number // 10
second_digit = number % 10


sum_of_digits = first_digit + second_digit

is_sum_two_digit = 10 <= sum_of_digits <= 99


greater_than_number = sum_of_digits > number

print(f"Сумма цифр числа равна {sum_of_digits}.")
print(f"Является ли сумма двузначным числом? {'Да' if is_sum_two_digit else 'Нет'}")
print(f"Больше ли сумма цифр числа, чем само число? {'Да' if greater_than_number else 'Нет'}")
