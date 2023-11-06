# Не відсортований список словників
unsorted_list = [
    {'liquid': 'HardVandal', 'оцінка': 4.5},
    {'liquid': 'Chaser', 'оцінка': 4.7},
    {'liquid': 'Troublemaker', 'оцінка': 4.4},
    {'liquid': 'Twisted Salt', 'оцінка': 4.2}
]

# Вибір способу сортування
sort_option = input("Як ви бажаєте відсортувати список?\n1. Сортувати за назвою рідини\n2. Сортувати за оцінкою\nВиберіть опцію (1 або 2): ").strip()

if sort_option == "1":
    # Сортування за назвами рідини в алфавітному порядку
    sorted_list = sorted(unsorted_list, key=lambda x: x['liquid'])
elif sort_option == "2":
    # Сортування за оцінкою за зростанням
    sorted_list = sorted(unsorted_list, key=lambda x: x['оцінка'])
else:
    print("Неправильний вибір сортування.")

if sorted_list:
    # Виведення відсортованого списку
    print("Відсортований список:")
    for item in sorted_list:
        print(f"Назва рідини: {item['liquid']}, Оцінка: {item['оцінка']}")
