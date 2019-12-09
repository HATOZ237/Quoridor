# -*- coding: utf-8 -*-
"""This is the Case class.
@author: Iooss
@license: MIT
"""


class Case:
    """
        This method implement the case of the board
    """
    idClass = 1

    def __init__(self):
        """
            constructor
        """
        self.id = Case.idClass
        Case.idClass += 1

        self.walls = []
        for i in range(4):
            self.walls += [False]

    def placeWall(self, side):
        """
            Method to place a wall in this case
            The attribute side takes values from 1 to 4
            1 => top,
            2 => right,
            3 => bottom,
            4 => left
        """
        self.walls[side - 1] = True

    def hasWall(self, side):
        """
            Method to know if there is a wall on a side
        """
        return self.walls[side - 1]
