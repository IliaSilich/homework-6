for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i * j:2d}", end=" ")
    print()

print('=' * 30)

i = 1
while i <= 10:
    j = 1
    while j <= 10:
        print(f"{i * j:2d}", end=" ")
        j += 1
    print()
    i += 1
