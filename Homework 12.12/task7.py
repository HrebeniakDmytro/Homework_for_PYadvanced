import csv
import json
import xml.etree.ElementTree as ET

def create_csv(filename):
    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Ім'я", "Прізвище", "Дата народження", "Місто"])
        print(f"Файл {filename} створено/перезаписано.")

def add_row_to_csv(filename):
    with open(filename, mode="a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        name = input("Введіть ім'я: ")
        surname = input("Введіть прізвище: ")
        birth_date = input("Введіть дату народження (рррр-мм-дд): ")
        city = input("Введіть місто: ")
        writer.writerow([name, surname, birth_date, city])
        print("Новий рядок додано до файлу.")

def read_csv(filename):
    with open(filename, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def csv_to_json(csv_filename, json_filename):
    with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        data = [row for row in reader]
    with open(json_filename, mode="w", encoding="utf-8") as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)
    print(f"Файл {csv_filename} конвертовано у {json_filename}.")

def csv_to_xml(csv_filename, xml_filename):
    with open(csv_filename, mode="r", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        root = ET.Element("people")
        for row in reader:
            person = ET.SubElement(root, "person")
            for key, value in row.items():
                ET.SubElement(person, key).text = value
    tree = ET.ElementTree(root)
    tree.write(xml_filename, encoding="utf-8", xml_declaration=True)
    print(f"Файл {csv_filename} конвертовано у {xml_filename}.")

def main():
    filename = "people.csv"
    while True:
        print("\nМеню:")
        print("1. Створити або перезаписати CSV-файл")
        print("2. Додати новий рядок до CSV-файлу")
        print("3. Прочитати CSV-файл")
        print("4. Конвертувати CSV у JSON")
        print("5. Конвертувати CSV у XML")
        print("6. Вийти")
        choice = input("Виберіть опцію: ")

        if choice == "1":
            create_csv(filename)
        elif choice == "2":
            add_row_to_csv(filename)
        elif choice == "3":
            read_csv(filename)
        elif choice == "4":
            csv_to_json(filename, "people.json")
        elif choice == "5":
            csv_to_xml(filename, "people.xml")
        elif choice == "6":
            print("Вихід із програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.")

if __name__ == "__main__":
    main()
