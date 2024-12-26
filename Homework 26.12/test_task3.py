import unittest
from task3 import *

class TestStudent(unittest.TestCase):
    def test_valid_student(self):
        student = Student("Олександр", "Іванов", 20, 85.5)
        self.assertEqual(student.first_name, "Олександр")
        self.assertEqual(student.last_name, "Іванов")
        self.assertEqual(student.age, 20)
        self.assertEqual(student.average_grade, 85.5)

    def test_invalid_name(self):
        with self.assertRaises(ValueError):
            Student("", "Іванов", 20, 85.5)

        with self.assertRaises(ValueError):
            Student("Олександр", "", 20, 85.5)

    def test_invalid_age(self):
        with self.assertRaises(ValueError):
            Student("Олександр", "Іванов", -1, 85.5)

        with self.assertRaises(ValueError):
            Student("Олександр", "Іванов", 121, 85.5)

    def test_invalid_average_grade(self):
        with self.assertRaises(ValueError):
            Student("Олександр", "Іванов", 20, -10.0)

        with self.assertRaises(ValueError):
            Student("Олександр", "Іванов", 20, 101.0)

    def test_student_list(self):
        for student in students:
            self.assertIsInstance(student, Student)
            self.assertTrue(0 <= student.age <= 120, "Вік студента має бути валідним.")
            self.assertTrue(0.0 <= student.average_grade <= 100.0, "Середній бал має бути валідним.")

if __name__ == "__main__":
    unittest.main()
