# -*- coding: utf-8 -*-
from .line import *


class Grid():
    """
        Class to create objects to draw the grid
    """

    def __init__(self, board, width, height):
        """
            Constructor
        """
        self.items = []

        #TODO Maybe to remove
        self.width = width
        self.height = height

        self.size_x = board.size
        self.size_y = board.size
        self.origin = [50, 50]
        self.case_width = int(width // self.size_x)
        self.case_height = int(height // self.size_y)

        # Draw vertical lines
        for i in range(self.size_x - 1):
            x = self.case_width * (i + 1)
            self.items += [Line(x, 0, x, height - 2, self.origin)]

        # Draw horizontal lines
        for i in range(self.size_y - 1):
            y = self.case_height * (i + 1)
            self.items += [Line(0, y, width - 2, y, self.origin)]

    def draw(self):
        """
            Draw the grid
        """
        for item in self.items:
            item.draw()

    def getCaseColByAbsX(self, x):
        """
            Method to get the cooresponding x case colomn to a x coordinate
        """
        x = x - self.origin[0]
        case_x = x // self.case_width

        if not case_x > (self.size_x - 1):
            if not case_x < 0:
                return case_x

    def getCaseLineByAbsY(self, y):
        """
            Method to get the cooresponding y case line to a y coordinate
        """
        y = y - self.origin[1]
        case_y = y // self.case_height

        if not case_y > (self.size_y - 1):
            if not case_y < 0:
                return case_y
