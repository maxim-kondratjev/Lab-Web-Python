from math import pi

from python_lab_oop.FigureColour import FigureColour
from python_lab_oop.GeometricFigure import GeometricFigure


class Circle(GeometricFigure):
    figure_name = "Круг"

    def __init__(self, radius, colour):
        self.radius = radius
        self.colour = FigureColour(colour)

    def find_square(self):
        return pi*self.radius**2

    def __repr__(self):
        return ("Фигура - {}, Радиус - {}, Цвет - {}, Площадь - {}\n"
              .format(self.figure_name, self.radius, self.colour, self.find_square()))

    def get_name(self):
        return self.figure_name