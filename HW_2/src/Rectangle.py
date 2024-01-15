from HW_2.src.Figure import Figure


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


r = Rectangle(3, 4)
print("площадь прямоугольника = ", r.get_area())
print("периметр прямоугольника = ", r.get_perimetr())
