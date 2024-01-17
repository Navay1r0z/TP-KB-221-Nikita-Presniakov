list = [
    {"name": "Jack", "phone": "0631234567", "age": 20, "planet": "Earth"},
    {"name": "Amber", "phone": "0631234567", "age": 22, "planet": "Mars"},
    {"name": "Patrick", "phone": "0631234567", "age": 21, "planet": "Venus"},
    {"name": "Nik", "phone": "0631234567", "age": 19, "planet": "Jupiter"}
]

def print_all_elements():
    sorted_elements = sorted(list, key=lambda x: x["name"])
    for element in sorted_elements:
        str_for_print = f"Element name is {element['name']}, Age is {element['age']}, Phone is {element['phone']}, Planet is {element['planet']}"
        print(str_for_print)

def add_new_element():
    name = input("Please enter element name: ")
    age = int(input("Please enter element age: "))
    phone = input("Please enter element phone: ")
    planet = input("Please enter element planet: ")
    new_element = {"name": name, "phone": phone, "age": age, "planet": planet}

    list.append(new_element)
    list.sort(key=lambda x: x["name"])
    print("New element has been added")

def delete_element():
    name = input("Please enter name to be deleted: ")
    delete_position = -1
    for element in list:
        if name == element["name"]:
            delete_position = list.index(element)
            break
    if delete_position == -1:
        print("Element was not found")
    else:
        del list[delete_position]
        print("Element has been deleted")

def update_element():
    name = input("Please enter name to be updated: ")
    for index, element in enumerate(list):
        if name == element["name"]:
            new_name = input("Enter new name: ")
            new_age = int(input("Enter new age: "))
            new_phone = input("Enter new phone: ")
            new_planet = input("Enter new planet: ")
            new_element = {"name": new_name, "age": new_age, "phone": new_phone, "planet": new_planet}

            del list[index]
            insert_position = 0
            for pos, elem in enumerate(list):
                if new_name > elem["name"]:
                    insert_position = pos + 1
                else:
                    break
            list.insert(insert_position, new_element)
            print("Element has been updated")
            break
    else:
        print("Element not found")

def main():
    while True:
        choice = input("Please specify the action [C create, U update, D delete, P print, X exit]: ")
        if choice.upper() == "C":
            print("New element will be created:")
            add_new_element()
        elif choice.upper() == "U":
            print("Existing element will be updated")
            update_element()
        elif choice.upper() == "D":
            print("Element will be deleted")
            delete_element()
        elif choice.upper() == "P":
            print("List will be printed")
            print_all_elements()
        elif choice.upper() == "X":
            print("Exit")
            break
        else:
            print("Wrong choice")

if __name__ == "__main__":
    main()
