def find_insert_position(sorted_list, new_element):
    left, right = 0, len(sorted_list) - 1

    while left <= right:
        mid = (left + right) // 2
        if sorted_list[mid] == new_element:
            # Якщо елемент вже є в списку, повертаємо позицію, на якій він знаходиться
            return mid
        elif sorted_list[mid] < new_element:
            left = mid + 1
        else:
            right = mid - 1

    # Якщо не знайдено відповідного елемента, повертаємо позицію для вставки
    return left

# Приклад використання функції
sorted_list = [1, 3, 5, 7, 9]
new_element = 4
position = find_insert_position(sorted_list, new_element)
print(f"Позиція для вставки {new_element} у відсортований список: {position}")
