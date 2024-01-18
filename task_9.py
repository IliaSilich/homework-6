def longest_common_prefix(strings):
    if not strings or not all(isinstance(s, str) for s in strings):
        raise ValueError("Некорректный формат входных данных. Ожидается массив строк.")

    if not strings:
        return ""

    prefix = strings[0]

    for string in strings[1:]:
        i = 0
        while i < len(prefix) and i < len(string) and prefix[i] == string[i]:
            i += 1

        prefix = prefix[:i]

    return prefix

try:
    input_strings = [input("Введите строку {}: ".format(i + 1)) for i in range(int(input("Введите количество строк: ")))]
    result_prefix = longest_common_prefix(input_strings)
    print("Самый длинный общий префикс:", result_prefix)
except ValueError as e:
    print(f"Ошибка: {e}")
