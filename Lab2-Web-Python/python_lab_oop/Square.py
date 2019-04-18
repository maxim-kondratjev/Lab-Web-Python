from python_lab_oop import Rectangle
from python_lab_oop import FigureColour


class Square(Rectangle):
    figure_name = "Квадрат"

    def __init__(self, side, colour):
        self.side = side
        self.colour = FigureColour(colour)

    def find_square(self):
        return self.side**2

    def __repr__(self):
        return ("Фигура - {}, Сторона - {}, Цвет - {}, Площадь - {}\n"
              .format(self.figure_name, self.side, self.colour, self.find_square()))
