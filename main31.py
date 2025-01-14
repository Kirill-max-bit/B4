def check_digits(number):    
    hundreds = number // 100
    tens = (number // 10) % 10
    units = number % 10

    all_same = hundreds == tens and tens == units

    has_duplicates = hundreds == tens or hundreds == units or tens == units

    return all_same, has_duplicates


three_digit_number = int(input("Введите трехзначное число: "))

all_same, has_duplicates = check_digits(three_digit_number)

if all_same:
    print("Все цифры числа одинаковые.")
else:
    print("Не все цифры числа одинаковые.")

if has_duplicates:
    print("Среди цифр числа есть одинаковые.")
else:
    print("Среди цифр числа нет одинаковых.")
