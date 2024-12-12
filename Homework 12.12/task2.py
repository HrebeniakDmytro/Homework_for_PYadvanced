import xml.etree.ElementTree as ET

root = ET.Element("library")

book1 = ET.SubElement(root, "book", id="1")
ET.SubElement(book1, "title").text = "Майстер і Маргарита"
ET.SubElement(book1, "author").text = "Михайло Булгаков"
ET.SubElement(book1, "year").text = "1966"

book2 = ET.SubElement(root, "book", id="2")
ET.SubElement(book2, "title").text = "Кобзар"
ET.SubElement(book2, "author").text = "Тарас Шевченко"
ET.SubElement(book2, "year").text = "1840"

tree = ET.ElementTree(root)
tree.write("library.xml", encoding="utf-8", xml_declaration=True)

print("XML-файл 'library.xml' створено.")

tree = ET.parse("library.xml")
root = tree.getroot()

print("\nВсі книги:")
for book in root.findall("book"):
    title = book.find("title").text
    author = book.find("author").text
    print(f"Назва: {title}, Автор: {author}")

author_name = "Тарас Шевченко"
print(f"\nКниги автора {author_name}:")
for book in root.findall(f".//book[author='{author_name}']"):
    title = book.find("title").text
    print(f"Назва: {title}")

new_book = ET.SubElement(root, "book", id="3")
ET.SubElement(new_book, "title").text = "Захар Беркут"
ET.SubElement(new_book, "author").text = "Іван Франко"
ET.SubElement(new_book, "year").text = "1883"

tree.write("library.xml", encoding="utf-8", xml_declaration=True)
print("\nНовий елемент додано та файл оновлено.")
