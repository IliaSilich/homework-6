def find_max_elements(nested_list):
    max_elements = []

    for inner_list in nested_list:
        if isinstance(inner_list, list):
            if all(isinstance(elem, (int, float)) for elem in inner_list):
                max_elements.append(max(inner_list))
            else:
                raise ValueError("Внутренние элементы вложенных списков должны быть числами")
        else:
            raise ValueError("Внутренние элементы должны быть списками")

    return max_elements


list1 = [[1, 2, 3], [4, 'five', 6], [7, 8, 9]]
list2 = [[1, 2, 3.14], [-4, -5, -6], [7, 8, 9]]
list3 = [[], [], []]

try:
    print(find_max_elements(list1))
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(find_max_elements(list2))
except ValueError as e:
    print(f"Ошибка: {e}")

try:
    print(find_max_elements(list3))
except ValueError as e:
    print(f"Ошибка: {e}")
