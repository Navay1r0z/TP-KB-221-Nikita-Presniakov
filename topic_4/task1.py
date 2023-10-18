def dodavannya(a, b):
    return a + b

def vidnimannya(a, b):
    return a - b

def mnozhennya(a, b):
    return a * b

def dilyennya(a, b):
    if b == 0:
        raise ZeroDivisionError("Ділення на нуль недопустиме")
    return a / b

while True:
    print("Оберіть операцію:")
    print("1. Додавання")
    print("2. Віднімання")
    print("3. Множення")
    print("4. Ділення")
    print("5. Вихід")

    try:
        vybir = int(input("Введіть номер операції: "))

        if vybir == 5:
            break

        num1 = float(input("Введіть перше число: "))
        num2 = float(input("Введіть друге число: "))

        if vybir == 1:
            print("Результат:", dodavannya(num1, num2))
        elif vybir == 2:
            print("Результат:", vidnimannya(num1, num2))
        elif vybir == 3:
            print("Результат:", mnozhennya(num1, num2))
        elif vybir == 4:
            try:
                print("Результат:", dilyennya(num1, num2))
            except ZeroDivisionError as e:
                print("Помилка:", e)
        else:
            print("Невірний вибір операції")
    
    except ValueError:
        print("Невірний формат числа. Будь ласка, введіть число ще раз.")
    except Exception as e:
        print("Сталася помилка:", e)

print("Дякуємо за користуванням калькулятором!")
