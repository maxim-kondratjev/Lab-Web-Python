from python_lab_oop.FigureColour import FigureColour
from python_lab_oop.GeometricFigure import GeometricFigure


class Rectangle(GeometricFigure):
    figure_name = "Прямоугольник"

    def __init__(self, width, height, colour):
        self.width = width
        self.height = height
        self.colour = FigureColour(colour)

    def find_square(self):
        return self.width*self.height

    def __repr__(self):
        return ("Фигура - {}, Ширина - {}, Высота - {}, Цвет - {}, Площадь - {}\n"
              .format(self.figure_name, self.width, self.height, self.colour, self.find_square()))

    def get_name(self):
        return self.figure_name
