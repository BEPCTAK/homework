import random

def generate_password(n):
    if n < 3 or n > 20:
        raise ValueError("Число должно быть в диапазоне от 3 до 20")

    numbers = list(range(1, n + 1))
    password = ""


    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            pair_sum = numbers[i] + numbers[j]
            if n % pair_sum == 0:
                password += f"{numbers[i]}{numbers[j]}"

    return password


n = random.randint(3, 20)
result = generate_password(n)
print(f"Сгенерированное число: {n}")
print(f"Пароль для числа {n}: {result}")