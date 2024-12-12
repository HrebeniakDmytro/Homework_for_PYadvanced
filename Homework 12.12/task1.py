import json

data = {
    "name": "Олександр",
    "age": 30,
    "hobbies": ["читання", "програмування", "спорт"],
    "is_student": False
}

json_data = json.dumps(data, ensure_ascii=False, indent=4)

with open("data.json", "w", encoding="utf-8") as file:
    file.write(json_data)

print("Дані збережено у файл data.json")

with open("data.json", "r", encoding="utf-8") as file:
    loaded_data = json.load(file)

print("Дані завантажено з файлу:")
print(loaded_data)
