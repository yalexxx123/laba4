#лабораторка 4. вариант 9

n = int(input("Введите количество элементов массива n: "))

A = []
print("Введите элементы массива:")
for i in range(n):
    x = float(input(f"A[{i}] = "))
    A.append(x)

print("Исходный массив A:")
for i in range(n):
    print(f"A[{i}] = {A[i]:.3f}")

# 1 максимальный по модулю элемент
max_abs = abs(A[0])
max_index = 0

for i in range(1, n):
    if abs(A[i]) > max_abs:
        max_abs = abs(A[i])
        max_index = i

print(f"Максимальный по модулю элемент: A[{max_index}] = {A[max_index]:.3f}")
print(f"Его модуль: {max_abs:.3f}")

# 2 сумма между первым и вторым положительными элементами
first_pos = -1
second_pos = -1

for i in range(n):
    if A[i] > 0:
        if first_pos == -1:
            first_pos = i
        else:
            second_pos = i
            break

if first_pos == -1 or second_pos == -1:
    print("Не найдены два положительных элемента — сумму между ними вычислить нельзя.")
else:
    s = 0.0
    for i in range(first_pos + 1, second_pos):
        s += A[i]
    print(f"Первый положительный: A[{first_pos}] = {A[first_pos]:.3f}")
    print(f"Второй положительный: A[{second_pos}] = {A[second_pos]:.3f}")
    print(f"Сумма между ними: {s:.3f}")

# 3 нули — в конец
B = []
zeros = []

for i in range(n):
    if A[i] == 0:
        zeros.append(A[i])
    else:
        B.append(A[i])

A = B + zeros

print("Преобразованный массив A:")
for i in range(n):
    print(f"A[{i}] = {A[i]:.3f}")