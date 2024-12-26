def calculate_bmi(height: float, weight: float) -> str:
    if height <= 0 or weight <= 0:
        raise ValueError("Зріст і вага повинні бути більше нуля.")

    bmi = weight / (height ** 2)
    if bmi < 18.5:
        return "Недостатня вага"
    elif 18.5 <= bmi < 25:
        return "Маса тіла в нормі"
    else:
        return "Слідкуйте за фігурою"

assert calculate_bmi(1.8, 70) == "Маса тіла в нормі", "Тест 1: Помилка при нормальній вазі."
assert calculate_bmi(1.6, 45) == "Недостатня вага", "Тест 2: Помилка при недостатній вазі."
assert calculate_bmi(1.7, 85) == "Слідкуйте за фігурою", "Тест 3: Помилка при надлишковій вазі."

assert calculate_bmi(1.8, 59.94) == "Недостатня вага", "Тест 4: Помилка на межі недостатньої ваги."
assert calculate_bmi(1.8, 80.99) == "Маса тіла в нормі", "Тест 5: Помилка на межі нормальної ваги."

try:
    calculate_bmi(0, 70)
    assert False, "Тест 6: Очікується ValueError при нульовому зрості."
except ValueError:
    pass

try:
    calculate_bmi(1.8, -10)
    assert False, "Тест 7: Очікується ValueError при від'ємній вазі."
except ValueError:
    pass

try:
    calculate_bmi(-1.8, 70)
    assert False, "Тест 8: Очікується ValueError при від'ємному зрості."
except ValueError:
    pass

print("Усі тести з assert пройдено успішно!")
