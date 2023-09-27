import math

# Функція для обчислення дискримінанту
def calculate_discriminant(a, b, c):
    return b**2 - 4*a*c

# Функція для знаходження коренів на основі обчисленого дискримінанту
def find_roots(a, b, c):
    D = calculate_discriminant(a, b, c)
    
    if D < 0:
        return None  # Рівняння не має дійсних коренів
    elif D == 0:
        x1 = -b / (2*a)
        return [x1]  # Рівняння має один корінь
    else:
        x1 = (-b + math.sqrt(D)) / (2*a)
        x2 = (-b - math.sqrt(D)) / (2*a)
        return [x1, x2]  # Рівняння має два корені

# Введення коефіцієнтів квадратного рівняння
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Виклик функцій для обчислення дискримінанту та знаходження коренів
D = calculate_discriminant(a, b, c)
roots = find_roots(a, b, c)

# Виведення результату
if roots is None:
    print("Рівняння не має дійсних коренів")
else:
    if len(roots) == 1:
        print(f"Рівняння має один дійсний корінь: x = {roots[0]}")
    else:
        print(f"Рівняння має два дійсних корені: x1 = {roots[0]}, x2 = {roots[1]}")
