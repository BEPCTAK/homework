import random


def generate_password(n):
    result = ""

    for i in range(1, n // 2 + 1):
        for j in range(n, n // 2, -1):
            if i < j:  # Проверка на уникальность пары
                pair_sum = i + j
                if n % pair_sum == 0:
                    result += f"{i}{j}"

    return result


n = random.randint(3, 20)
result = generate_password(n)
print(f"Сгенерированное число: {n}")
print(f"Пароль для числа {n}: {result}")
