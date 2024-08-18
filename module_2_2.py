first = str(input('Введите первое число: '))
second = str(input('Введите второе число: '))
third = str(input('Введите третье число: '))
if first == second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)


