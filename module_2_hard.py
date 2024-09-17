import random

def generate_password(n):
    # Проверяем, что n находится в диапазоне от 3 до 20
    if n < 3 or n > 20:
        raise ValueError("Число должно быть в диапазоне от 3 до 20")

    # Создаем список чисел от 1 до n
    numbers = list(range(1, n + 1))
    password = ""

    # Генерируем уникальные пары
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            # Сумма пары
            pair_sum = numbers[i] + numbers[j]
            # Проверяем кратность
            if n % pair_sum == 0:
                # Формируем строку из пары и добавляем в пароль
                password += f"{numbers[i]}{numbers[j]}"

    return password


n = random.randint(3, 20)
result = generate_password(n)
print(f"Сгенерированное число: {n}")
print(f"Пароль для числа {n}: {result}")