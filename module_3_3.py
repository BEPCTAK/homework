def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(10)
print_params(10, 'собака')
print_params(b=25)
print_params(c=[1, 2, 3])


values_list = [777, 'яблоко', False]
values_dict = {'a': 42, 'b': 'молоко', 'c': None}


print_params(*values_list)
print_params(**values_dict)


values_list_2 = [4.3, 'Небо']
print_params(*values_list_2, 42)
