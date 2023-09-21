# Task 3

def calculate_discriminant(a, b, c):
    """Обчислення дескримінанта для квадратного рівняння ax^2 + bx + c = 0."""
    discriminant = b**2 - 4*a*c
    return discriminant

a = 2
b = 5
c = -3
result = calculate_discriminant(a, b, c)
print(f"Дескримінант для рівняння {a}x^2 + {b}x + {c} = 0 дорівнює {result}")