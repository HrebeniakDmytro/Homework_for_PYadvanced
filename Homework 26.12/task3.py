class Student:
    def __init__(self, first_name: str, last_name: str, age: int, average_grade: float):
        if not first_name or not last_name:
            raise ValueError("Ім'я та прізвище не можуть бути порожніми.")
        if not (0 <= age <= 120):
            raise ValueError("Вік має бути в діапазоні від 0 до 120 років.")
        if not (0.0 <= average_grade <= 100.0):
            raise ValueError("Середній бал має бути від 0.0 до 100.0.")

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.average_grade = average_grade

    def __repr__(self):
        return (f"Student(first_name='{self.first_name}', last_name='{self.last_name}', "
                f"age={self.age}, average_grade={self.average_grade})")

students = [
    Student("Олександр", "Іванов", 20, 85.5),
    Student("Марія", "Петрівна", 19, 90.0),
    Student("Андрій", "Коваленко", 21, 72.3),
    Student("Ірина", "Шевченко", 22, 88.7),
    Student("Дмитро", "Мельник", 20, 95.0),
    Student("Ольга", "Гончар", 23, 78.0),
    Student("Катерина", "Лисенко", 19, 84.1),
    Student("Максим", "Сидоренко", 18, 91.2),
    Student("Анастасія", "Бондар", 20, 89.9),
    Student("Віктор", "Захаренко", 21, 67.8)
]
