def is_valid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping:
            if not stack or mapping[char] != stack.pop():
                return False
        else:
            stack.append(char)

    return not stack if s else False


my_str1 = "{(})"
my_str2 = "[{}()]"
my_str3 = "[hello]"
my_str4 = "(){}}{"
my_str5 = "(]"
my_str6 = ""

print(is_valid(my_str1))
print(is_valid(my_str2))
print(is_valid(my_str3))
print(is_valid(my_str4))
print(is_valid(my_str5))
print(is_valid(my_str6))
