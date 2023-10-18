def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Ділення на нуль неможливе")
    return a / b

def get_number(prompt):
    while True:
        try:
            a = float(input(prompt))
            return a
        except ValueError:
            print("Некоректне значення, спробуйте ще раз.")

while True:
    print("Виберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")
    
    choice = input("Номер операції (1/2/3/4/5): ")
    
    if choice == "5":
        print("Вихід...")
        break
    
    if choice in ('1', '2', '3', '4'):
        first_number = get_number("Перше число: ")
        second_number = get_number("Друге число: ")

        if choice == '1':
            result = add(first_number, second_number)
        elif choice == '2':
            result = subtract(first_number, second_number)
        elif choice == '3':
            result = multiply(first_number, second_number)
        elif choice == '4':
            try:
                result = divide(first_number, second_number)
            except ValueError as e:
                print("Помилка:", e)
                continue

        print("Результат:", result)
