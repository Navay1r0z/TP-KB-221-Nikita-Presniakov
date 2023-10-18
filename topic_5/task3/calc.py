from functions import add, subtract, multiply, divide, get_user_input

def main():
    print("Вітаємо у калькуляторі!")
    while True:
        print("Оберіть операцію:")
        print("1. Додавання")
        print("2. Віднімання")
        print("3. Множення")
        print("4. Ділення")
        print("5. Вийти")
        
        choice = input("Ваш вибір: ")
        
        if choice == '5':
            print("Дякуємо за використання калькулятора. До побачення!")
            break
        
        num1, num2 = get_user_input()
        
        if choice == '1':
            result = add(num1, num2)
            print(f"Результат: {result}")
        elif choice == '2':
            result = subtract(num1, num2)
            print(f"Результат: {result}")
        elif choice == '3':
            result = multiply(num1, num2)
            print(f"Результат: {result}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"Результат: {result}")
        else:
            print("Невірний вибір. Спробуйте ще раз.")

if __name__ == "__main__":
    main()
