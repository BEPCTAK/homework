import math


class Figure:
    def __init__(self, color, *sides):
        self.__sides = []
        self.__color = list(color)
        self.filled = False

        if len(sides) == self.sides_count:
            self.set_sides(*sides)
        else:
            self.__sides = [1] * self.sides_count

    def get_color(self):
        return self.__color

    def __is_valid_color(self, r, g, b):
        return all(isinstance(x, int) and 0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *new_sides):
        return len(new_sides) == self.sides_count and all(isinstance(side, int) and side > 0 for side in new_sides)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)

    def set_sides(self, *new_sides):
        if self.__is_valid_sides(*new_sides):
            self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if len(sides) == 1:
            self.__radius = sides[0]
        else:
            self.__radius = 1  # Если не передан радиус

    def get_square(self):
        return math.pi * (self.__radius ** 2)

    def set_sides(self, *new_sides):
        if len(new_sides) == 1 and isinstance(new_sides[0], (int, float)) and new_sides[0] > 0:
            super().set_sides(*new_sides)
            self.__radius = new_sides[0]


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)

    def get_square(self):
        a, b, c = self.get_sides()
        s = (a + b + c) / 2
        return math.sqrt(s * (s - a) * (s - b) * (s - c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side_length):
        super().__init__(color)
        self.set_sides(*[side_length] * self.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3


# Проверка кода
circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

circle1.set_color(55, 66, 77)
print(circle1.get_color())
cube1.set_color(300, 70, 15)
print(cube1.get_color())

cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())

print(len(circle1))

print(cube1.get_volume())
