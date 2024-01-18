input_numbers = input("Введите список чисел через пробел: ")

try:
    numbers = [int(num) for num in input_numbers.split()]
except ValueError:
    print("Ошибка ввода. Пожалуйста, введите только целые числа, разделенные пробелами.")
    exit()

if not numbers:
    print("Ошибка ввода. Пожалуйста, введите хотя бы одно число.")
    exit()

max_num = float('-inf')
min_num = float('inf')

for num in numbers:
    if num > max_num:
        max_num = num

    if num < min_num:
        min_num = num

print(f"Максимальное число: {max_num}")
print(f"Минимальное число: {min_num}")
