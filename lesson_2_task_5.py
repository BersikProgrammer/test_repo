def month_to_season(month):
    # Проверяем, что номер месяца в допустимом диапазоне (1-12)
    if month < 1 or month > 12:
        return "Некорректный номер месяца"

    # Определяем сезон по номеру месяца
    if month in [12, 1, 2]:
        return "Зима"
    elif month in [3, 4, 5]:
        return "Весна"
    elif month in [6, 7, 8]:
        return "Лето"
    else:  # месяцы 9, 10, 11
        return "Осень"


print(month_to_season(2))   # Зима
print(month_to_season(5))   # Весна
print(month_to_season(8))   # Лето
print(month_to_season(11))  # Осень
print(month_to_season(12))  # Зима
print(month_to_season(15))  # Некорректный номер месяца
