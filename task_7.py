def count_students_above_average(heights):
    if not heights or not all(isinstance(height, (int, float)) for height in heights):
        raise ValueError("Некорректный формат входных данных. Ожидается список чисел.")

    average_height = sum(heights) / len(heights)
    above_average_count = sum(1 for height in heights if height > average_height)

    return above_average_count


try:
    heights = [float(input(f"Введите рост ученика {i + 1}: ")) for i in
               range(int(input("Введите количество учеников: ")))]
    result_count = count_students_above_average(heights)
    print("Количество учеников с ростом выше среднего:", result_count)
except ValueError as e:
    print(f"Ошибка: {e}")
