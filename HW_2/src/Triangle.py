from HW_2.src.Figure import Figure

class Triangle(Figure):

    def __init__(self, side_a, side_b, side_c, coefficient):
        super().__init__(name="Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <=0:
            raise ValueError("Стороны треугольника должны быть больше нуля")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.coefficient = coefficient

    def get_area(self):
        return (self.side_a * self.side_b) * self.coefficient

    def get_perimetr(self):
        return self.side_a + self.side_b + self.side_c


t = Triangle(3, 4, 5, 0.3)