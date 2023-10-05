# Функція для тестування extend
def test_extend():
    list1 = [1, 2, 3]
    list2 = [4, 5, 6]
    list1.extend(list2)
    print("extend():", list1)

# Функція для тестування append
def test_append():
    list1 = [1, 2, 3]
    list1.append(4)
    print("append():", list1)

# Функція для тестування вставки (ідентифікатор, значення)
def test_insert():
    list1 = [1, 2, 3]
    list1.insert(1, 4)
    print("insert():", list1)

# Функція для тестування видалення (val)
def test_remove():
    list1 = [1, 2, 3, 4, 3]
    list1.remove(3)
    print("remove():", list1)

# Функція для тестування очищення
def test_clear():
    list1 = [1, 2, 3]
    list1.clear()
    print("clear():", list1)

# Функція для тестування сортування
def test_sort():
    list1 = [3, 1, 2, 4]
    list1.sort()
    print("sort():", list1)

# Функція для тестування зворотного
def test_reverse():
    list1 = [1, 2, 3]
    list1.reverse()
    print("reverse():", list1)

# Функція для тестування копії
def test_copy():
    list1 = [1, 2, 3]
    list2 = list1.copy()
    print("copy():", list2)

# Виклик функцій для тестування
test_extend()
test_append()
test_insert()
test_remove()
test_clear()
test_sort()
test_reverse()
test_copy()
