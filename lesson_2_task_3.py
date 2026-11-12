import math


def square(side):
    # Считаем площадь — сторона в квадрате
    area = side * side

    if isinstance(side, int):
        return int(area)
    else:
        rounded_area = math.ceil(area)
        return rounded_area


print("Результаты вычислений:")
print(f"Сторона 5 → площадь: {square(5)}")
print(f"Сторона 3.2 → площадь: {square(3.2)}")
print(f"Сторона 4 → площадь: {square(4)}")
print(f"Сторона 2.7 → площадь: {square(2.7)}")
print(f"Сторона 6.1 → площадь: {square(6.1)}")
