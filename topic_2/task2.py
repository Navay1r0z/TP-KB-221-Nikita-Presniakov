# Функція для додавання чисел
def add(x, y):
    return x + y

# Функція для віднімання чисел
def subtract(x, y):
    return x - y

# Функція для множення чисел
def multiply(x, y):
    return x * y

# Функція для ділення чисел
def divide(x, y):
    if y == 0:
        return "Ділення на нуль неможливе"
    return x / y

print("Оберіть операцію:")
print("1. Додавання")
print("2. Віднімання")
print("3. Множення")
print("4. Ділення")

# Введення операції користувачем
choice = input("Виберіть номер операції (1/2/3/4):")

# Введення чисел користувачем
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))

# Обчислення результату в залежності від вибору користувача
if choice == '1':
    print("Результат:", add(num1, num2))
elif choice == '2':
    print("Результат:", subtract(num1, num2))
elif choice == '3':
    print("Результат:", multiply(num1, num2))
elif choice == '4':
    print("Результат:", divide(num1, num2))
else:
    print("Вибрано неправильну операцію")
