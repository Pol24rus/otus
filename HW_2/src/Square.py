from HW_2.src.Rectangle import Rectangle


class Square(Rectangle):

    def __init__(self, side_a):
        if side_a <= 0:
            raise ValueError("Стороны квадрата должны быть больше нуля")
        super().__init__(side_a, side_a)


s = Square(6)
