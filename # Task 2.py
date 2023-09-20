# Task 2

string1 = "ooijhubjnkm"
string2 = 'rtyuilgdmbs'

result = string1 + " " + string2
print("Додавання рядків:", result)

length = len(result)
print("Довжина рядка:", length)

substring = result[0:6]
print("Вирізка підрядка:", substring)

search_string = "rtyuilgdmbs"
if search_string in result:
    print(f"Рядок '{search_string}' знайдений в рядку.")
else:
    print(f"Рядок '{search_string}' не знайдений в рядку.")

uppercase = result.upper()
lowercase = result.lower()
print("Верхній регістр:", uppercase)
print("Нижній регістр:", lowercase)

replaced = result.replace("Python", "JavaScript")
print("Заміна підрядка:", replaced)

words = result.split()
print("Розділення рядка на список:", words)

joined_string = " ".join(words)
print("Об'єднання списку в рядок:", joined_string)

number_string = "12345"
is_numeric = number_string.isnumeric()
print(f"Чи є рядок числовим: {is_numeric}")

whitespace_string = "  Пробіли  "
stripped_string = whitespace_string.strip()
print("Видалення пробілів:", stripped_string)