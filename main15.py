def days_since_start_of_year(year, month):
    start_day = (month - 1) * 31 // 12
    start_day += year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) and (month >= 3)
    total_days = start_day + (year - 1) * 365 + (year - 1) // 4 - (year - 1) // 100 + (year - 1) // 400
    return total_days


def age(birthdate, today):
    birth_year, birth_month = birthdate[0], birthdate[1]
    today_year, today_month = today[0], today[1]

    birth_days = days_since_start_of_year(birth_year, birth_month)
    today_days = days_since_start_of_year(today_year, today_month)

    age_in_days = today_days - birth_days
    age_in_years = age_in_days // 365

    return age_in_years


birthdate = (1990, 1)
today = (2023, 12)

age_in_years = age(birthdate, today)
print(f"Возраст: {age_in_years} лет")
