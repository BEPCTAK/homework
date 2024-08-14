number = 7, 6
item = "apples, pen"
taste = True
immutable_var = (7, 6, "apples, pen", True)
print(immutable_var)
print(type(immutable_var)) # кортеж - неизменяемый
mutable_list = [7, 6, "apples, pen", True]
print(mutable_list)
mutable_list.append(False)
print(mutable_list)
mutable_list[2] = 555
print(mutable_list)
print(type(mutable_list)) # список - можно добовлять и изменять

