import math

# Введення коефіцієнтів квадратного рівняння
a = float(input("Введіть коефіцієнт a: "))
b = float(input("Введіть коефіцієнт b: "))
c = float(input("Введіть коефіцієнт c: "))

# Обчислення дискримінанту
D = b**2 - 4*a*c

# Перевірка дискримінанту
if D > 0:
    # Два різних корені
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print("Два різних корені:")
    print(f"x1 = {x1}")
    print(f"x2 = {x2}")
elif D == 0:
    # Один корінь (корінь є подвійним)
    x1 = -b / (2*a)
    print("Один корінь (подвійний корінь):")
    print(f"x1 = {x1}")
else:
    # Дискримінант від'ємний, коренів немає у множині дійсних чисел
    real_part = -b / (2*a)
    imaginary_part = math.sqrt(-D) / (2*a)
    print("Комплексні корені:")
    print(f"x1 = {real_part} + {imaginary_part}i")
    print(f"x2 = {real_part} - {imaginary_part}i")
