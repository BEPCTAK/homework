def is_prime_number(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if is_prime_number(result):
            print("Простое")
        else:
            print("Составное")
        print(result)

    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


sum_three(2, 3, 6)
