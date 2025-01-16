def is_leap_year(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)


year = int(input("Введите год: "))
print(f"{year} год {'является' if is_leap_year(year) else 'не является'} високосным.")
