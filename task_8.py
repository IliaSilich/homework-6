def merge_sorted_arrays(arr1, arr2):
    if not arr1 or not arr2 or not all(isinstance(elem, (int, float)) for elem in arr1 + arr2):
        raise ValueError("Некорректный формат входных данных. Ожидается два упорядоченных массива чисел.")

    merged_array = []
    i, j = 0, 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])

    return merged_array


try:
    array1 = [float(x) for x in input("Введите элементы первого упорядоченного массива через пробел: ").split()]
    array2 = [float(x) for x in input("Введите элементы второго упорядоченного массива через пробел: ").split()]

    result_merged_array = merge_sorted_arrays(array1, array2)
    print("Объединенный упорядоченный массив:", result_merged_array)
except ValueError as e:
    print(f"Ошибка: {e}")
