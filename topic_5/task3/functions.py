def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Помилка: ділення на нуль"
    return x / y

def get_user_input():
    num1 = float(input("Введіть перше число: "))
    num2 = float(input("Введіть друге число: "))
    return num1, num2
