def square(x):
    return x ** 2

def cube(x):
    return x ** 3

def getNumValue():
    try:
        num = float(input("Введіть число: "))
        return num
    except ValueError:
        print("Невірний ввід. Будь ласка, введіть правильне число.")
        return getNumValue()  

def getOperation():
    valid_operations = ['square', 'cube']
    
    operation = input("Введіть операцію (square or cube): ").lower()
    
    if operation in valid_operations:
        return operation
    else:
        print("Невірна операція. Будь ласка, введіть 'square' or 'cube'.")
        return getOperation()  


value = getNumValue()
operation = getOperation()

if operation == 'square':
    result = square(value)
    print(f"The square of {value} is {result}")
elif operation == 'cube':
    result = cube(value)
    print(f"The cube of {value} is {result}")

