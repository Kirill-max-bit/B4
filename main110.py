suits = {
    1: "пик",
    2: "трефа",
    3: "бубна",
    4: "червь"
}


ranks = {
    6: "шестерка",
    7: "семерка",
    8: "восьмерка",
    9: "девятка",
    10: "десятка",
    11: "валет",
    12: "дама",
    13: "король",
    14: "туз"
}


m = int(input("Введите номер масти (1-4): "))
k = int(input("Введите номер достоинства карты (6-14): "))


if 1 <= m <= 4 and 6 <= k <= 14:
    suit = suits[m]
    rank = ranks[k]
    full_card_name = f"{rank.capitalize()} {suit}"
    print(full_card_name)
else:
    print("Ошибка: неверные данные.")