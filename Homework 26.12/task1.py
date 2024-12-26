def calculate_speed(distance: float, time: float) -> float:
    if time <= 0:
        raise ValueError("Час має бути більшим за нуль.")
    return distance / time

assert calculate_speed(100, 2) == 50, "Тест 1: Помилка розрахунку швидкості."
assert calculate_speed(150, 3) == 50, "Тест 2: Помилка розрахунку швидкості."
assert calculate_speed(0, 1) == 0, "Тест 3: Швидкість має бути нульовою."
assert calculate_speed(60, 0.5) == 120, "Тест 4: Помилка розрахунку швидкості."
assert calculate_speed(200, 4) == 50, "Тест 5: Помилка розрахунку швидкості."

try:
    calculate_speed(100, 0)
    assert False, "Тест 6: Очікується ValueError при нульовому часі."
except ValueError:
    pass

try:
    calculate_speed(100, -2)
    assert False, "Тест 7: Очікується ValueError при від'ємному часі."
except ValueError:
    pass

print("Усі тести пройдено успішно!")
