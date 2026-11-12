def is_year_leap(year):
    """
    Проверяет, является ли год високосным.

    Аргумент:
    year (int) — год, который нужно проверить.

    Возвращает:
    bool — True, если год високосный, False — если нет.
    """
    return year % 4 == 0


result = is_year_leap(2026)

print(f"год {2026}: {result}")
