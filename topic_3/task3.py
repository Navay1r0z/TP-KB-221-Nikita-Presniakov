def main():
    # Створимо початковий словник
    my_dict = {'one': 1, 'two': 2, 'three': 3}

    # Виведемо початковий словник
    print("Початковий словник:")
    print(my_dict)

    # Оновлення словника з іншим словником
    update_dict = {'four': 4, 'five': 5}
    my_dict.update(update_dict)
    print("\nОновлений словник (за допомогою update()):")
    print(my_dict)

    # Видалення ключа та відповідного значення зі словника
    key_to_delete = 'two'
    del my_dict[key_to_delete]
    print(f"\nСловник після видалення ключа '{key_to_delete}':")
    print(my_dict)

    # Очищення словника
    my_dict.clear()
    print("\nСловник після очищення (clear()):")
    print(my_dict)

    # Створимо новий словник
    new_dict = {'apple': 'яблуко', 'banana': 'банан', 'cherry': 'вишня'}

    # Виведемо ключі словника
    print("\nКлючі словника (keys()):")
    print(new_dict.keys())

    # Виведемо значення словника
    print("\nЗначення словника (values()):")
    print(new_dict.values())

    # Виведемо пари ключ-значення словника
    print("\nПари ключ-значення словника (items()):")
    print(new_dict.items())

if __name__ == "__main__":
    main()
