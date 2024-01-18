def input_matrix():
    rows = int(input("Введите количество строк: "))
    cols = int(input("Введите количество столбцов: "))

    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            element = float(input(f"Введите элемент матрицы [{i}][{j}]: "))
            row.append(element)
        matrix.append(row)

    return matrix


def sum_columns(matrix):
    if not matrix or not all(isinstance(row, list) for row in matrix) or not all(
            len(row) == len(matrix[0]) for row in matrix):
        raise ValueError("Некорректный формат входных данных. Ожидается двумерный массив.")

    cols_sum = [0] * len(matrix[0])

    for row in matrix:
        for j, element in enumerate(row):
            cols_sum[j] += element

    return cols_sum


try:
    matrix = input_matrix()
    result_sum = sum_columns(matrix)
    print("Сумма элементов по столбцам:", result_sum)
except ValueError as e:
    print(f"Ошибка: {e}")
