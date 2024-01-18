def transpose_matrix(matrix):
    if not isinstance(matrix, list) or not matrix or not all(isinstance(row, list) for row in matrix):
        raise ValueError("Некорректный формат входных данных. Ожидается многомерный список.")

    for row in matrix:
        if not all(isinstance(elem, (int, float)) for elem in row):
            raise ValueError("Некорректный формат входных данных. Ожидается список чисел.")

    transposed_matrix = [list(row) for row in zip(*matrix)]
    return transposed_matrix


input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

try:
    result_matrix = transpose_matrix(input_matrix)
    print("Транспонированный список:")
    for row in result_matrix:
        print(row)
except ValueError as e:
    print(f"Ошибка: {e}")
