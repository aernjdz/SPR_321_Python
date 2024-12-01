from math import pi
import json

class Figure:
    def area(self):
        raise NotImplementedError("This method should be overridden in a subclass.")

    def __int__(self):
        return int(self.area())
    
    def __str__(self):
        return f"Figure: {self.__class__.__name__}, Area: {self.area():.2f}"


# Rectangle
class Rectangle(Figure):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Circle
class Circle(Figure):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return pi * (self.radius ** 2)

class RightTriangle(Figure):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

class Trapezoid(Figure):
    def __init__(self, base1, base2, height):
        self.base1 = base1
        self.base2 = base2
        self.height = height

    def area(self):
        return 0.5 * (self.base1 + self.base2) * self.height

   
shapes = [
    Trapezoid(6, 8, 5),
    Rectangle(4, 5),
    Circle(7),
    RightTriangle(4, 5)
]


print("=" * 8)
for i, shape in enumerate(shapes):
    print(i, f"Figure: {type(shape).__name__} => Area: {int(shape)}")

print("=" * 8)


for i, shape in enumerate(shapes):
    print(i, shape)
print("=" * 8)

import json

class Shape:
    def show(self):
        print(self)

    def save(self, filename):
        with open(filename, 'w') as file:
            json.dump({'class': self.__class__.__name__, **self.__dict__}, file)

    @classmethod
    def load(cls, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            class_name = data.pop('class')
            shape_class = globals()[class_name]
            return shape_class(**data)



class Square(Shape):
    def __init__(self, x, y, side):
        self.x = x
        self.y = y
        self.side = side

    def __str__(self):
        return f"Square: Top-left corner ({self.x}, {self.y}), side {self.side}"


class Rectangle(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Rectangle: Top-left corner ({self.x}, {self.y}), width {self.width}, height {self.height}"


class Circle(Shape):
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius

    def __str__(self):
        return f"Circle: Center ({self.x}, {self.y}), radius {self.radius}"


class Ellipse(Shape):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def __str__(self):
        return f"Ellipse: Top-left corner ({self.x}, {self.y}), width {self.width}, height {self.height}"


shapes = [
    Square(0, 0, 5),
    Rectangle(1, 2, 4, 6),
    Circle(3, 3, 7),
    Ellipse(0, 0, 8, 4)
]


for i, shape in enumerate(shapes):
    filename = f"shape_{i}.json"
    shape.save(filename)

loaded_shapes = []
for i in range(len(shapes)):
    filename = f"shape_{i}.json"
    loaded_shapes.append(Shape.load(filename))

for shape in loaded_shapes:
    shape.show()


