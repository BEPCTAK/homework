def calculate_structure_sum(*args):
    total_sum = 0
    for item in args:
        if isinstance(item, (list, tuple, set)):
            for element in item:
                total_sum += calculate_structure_sum(element)
        elif isinstance(item, dict):
            for key, value in item.items():
                total_sum += calculate_structure_sum(key)
                total_sum += calculate_structure_sum(value)
        elif isinstance(item, str):
            total_sum += len(item)
        elif isinstance(item, (int, float)):
            total_sum += item
    return total_sum

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(*data_structure)
print(result)