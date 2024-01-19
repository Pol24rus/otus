from src.Figure import Figure
import math


class Circle(Figure):

    def __init__(self, side_a):
        super().__init__(name="Circle")
        if side_a <= 0:
            raise ValueError("Диаметр круга должен быть больше нуля")
        self.side_a = side_a

    def get_area(self):
        return math.pi * ((self.side_a / 2) ** 2)

    def get_perimetr(self):
        return self.side_a * math.pi


scl = Circle(3.5)
print("Площадь круга = ", scl.get_area())
print("Длина круга = ", scl.get_perimetr())
