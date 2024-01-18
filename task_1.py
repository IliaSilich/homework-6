input_numbers = input("Введите два числа через пробел: ")

numbers = input_numbers.split()

if len(numbers) != 2:
    print("Ошибка ввода. Пожалуйста, введите ровно два числа.")
else:
    try:
        num1 = int(numbers[0])
        num2 = int(numbers[1])
        a, b = abs(num1), abs(num2)

        while b:
            a, b = b, a % b
        print(f"НОД чисел {num1} и {num2} равен {a}")

    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите два целых числа.")
