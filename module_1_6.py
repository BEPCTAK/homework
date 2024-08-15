my_dict = {"john": 2001, "Anna": 1998, "Mike": 2003}
print(my_dict)
print(my_dict["Anna"])
my_dict["Nikolay"]= 1999
print(my_dict["Nikolay"])
my_dict.update({"Peter": 2010, "Olga": 2000})
print(my_dict)
del my_dict["Mike"]
print(my_dict.get("Mike"))
print(my_dict)
my_set = {1, 2, 1, 2, 3, "pen", "pencil", "table", (4, 17, 3, 11)}
print(my_set)
my_set.update({555, "orange"})
my_set.remove("pen")
print(my_set)
