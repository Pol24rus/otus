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

    # def add_area(self, other_figure):
    #     if not isinstance(other_figure, Figure):
    #         raise ValueError("Нужно передать фигуру")
    #     return self.get_area() + other_figure.get_area()


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


class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <=0:
            raise ValueError("Стороны треугольника должны быть больше нуля")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    def get_area(self):
        return (self.side_a * self.side_b) * 0.3

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c

#        p = (side_a + side_b + side_c) / 2


s = Square(6)
r = Rectangle(3, 4)
t = Triangle(3, 4, 5)
# print(r.add_area(other_figure=s))
print("площадь прямоугольника = ", r.get_area())
print("периметр прямоугольника = ", r.get_perimetr())
print("Площадь квадрата=", s.get_area())
print("Периметр квадрата=", s.get_perimetr())
print("Площадь треугольника=", t.get_area())
print("Периметр теруголиника=", t.get_perimetr())
#
