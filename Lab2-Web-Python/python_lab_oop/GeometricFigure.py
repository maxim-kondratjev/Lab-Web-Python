from abc import *


class GeometricFigure (metaclass=ABCMeta):
    @abstractmethod
    def find_square(self):
        pass
