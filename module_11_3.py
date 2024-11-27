def introspection_info(obj):
    info = {}

    # Определяем тип объекта
    info['type'] = type(obj).__name__

    # Получаем атрибуты объекта
    info['attributes'] = dir(obj)

    # Получаем методы объекта
    methods = [method for method in dir(obj) if callable(getattr(obj, method))]
    info['methods'] = methods

    # Получаем модуль, к которому принадлежит объект
    info['module'] = getattr(obj, '__module__', None)  # Используем getattr для избежания ошибки

    # Cвойства объекта
    info['is_instance'] = isinstance(obj, object)

    # Если объект является классом, добавим информацию о его родительских классах
    if isinstance(obj, type):
        info['base_classes'] = obj.__bases__

    return info


number_info = introspection_info(42)
print(number_info)

string_info = introspection_info("Hello, World!")
print(string_info)

list_info = introspection_info([1, 2, 3])
print(list_info)


class MyClass:
    def my_method(self):
        pass


my_class_info = introspection_info(MyClass)
print(my_class_info)
