class FigureColour:
    def __init__(self, colour="White"):
        self.colour = colour

    def get_colour(self):
        return self.colour

    def set_colour(self, colour):
        self.colour = colour

    def del_colour(self):
        del self.colour

    def __repr__(self):
        return self.colour
