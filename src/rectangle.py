from abc import ABC, abstractmethod


class Figure(ABC):

    def __init__(self, name: str):
        self.name = name


    @abstractmethod
    def get_area(self):
        pass

    @abstractmethod
    def get_perimetr(self):
        pass

    def add_area(self, other_figure):
        if not isinstance(other_figure, Figure):
            raise ValueError("Нужно передать фигуру")
        return self.get_area() + other_figure.get_area()


class Rectangle(Figure):

    def __init__(self, side_a, side_b):
        super().__init__(name="Rectangle")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Стороны прямоугольника должны быть больше нуля")
        self.side_a = side_a
        self.side_b = side_b

    def get_area(self):
        return self.side_a * self.side_b

    def get_perimetr(self):
        return (self.side_a + self.side_b) * 2


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Стороны квадрата должны быть больше нуля")
        super().__init__(side_a, side_a)


#       self.side_a = side_a

s = Square(6)
r = Rectangle(3, 4)
print(r.add_area(other_figure=s))
print("площадь прямоугольника = ", r.get_area())
print("периметр прямоугольника = ", r.get_perimetr())
print("Площадь квадрата=", s.get_area())
print("Периметр квадрата=", s.get_perimetr())

#
