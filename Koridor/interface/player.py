# -*- coding: utf-8 -*-
from .label import *


class Player():
    """
        Player graphic item takes a player and the grid to draw the player
        at the correct coordinates on the grid.
    """

    def __init__(self, player, grid):
        """
            Constructor
        """
        # Origin of the case
        x = player.position[0] * grid.case_width + grid.origin[0]
        y = player.position[1] * grid.case_height + grid.origin[1]

        # Offset in the case
        x += grid.case_width // 4
        y += grid.case_height // 4

        text_height = grid.case_height // 2

        self.label = Label(str(player.id), x, y, text_height)

    def draw(self):
        """
            Draw the object
        """
        self.label.draw()
