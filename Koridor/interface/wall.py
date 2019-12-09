# -*- coding: utf-8 -*-

from .line import *


class Wall:

    def __init__(self, coord, side, grid):
        """
            Constructor
        """
        color = [255, 0, 0]
        width = 3

        # Origin coords of the case
        x = coord[0] * grid.case_width
        y = coord[1] * grid.case_height

        if side == 1:
            x2 = x + grid.case_width
            y1 = y + grid.case_height
            self.line = Line(x, y1, x2, y1, grid.origin, color, width)
        elif side == 2:
            x1 = x + grid.case_width
            y2 = y + grid.case_height
            self.line = Line(x1, y, x1, y2, grid.origin, color, width)
        elif side == 3:
            x2 = x + grid.case_width
            self.line = Line(x, y, x2, y, grid.origin, color, width)
        else:
            y2 = y + grid.case_height
            self.line = Line(x, y, x, y2, grid.origin, color, width)

    def draw(self):
        """
            Draw the object
        """
        self.line.draw()
