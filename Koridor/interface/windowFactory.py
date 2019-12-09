# -*- coding: utf-8 -*-

from .grid import *
from .label import *
from .line import *
from .player import *
from .wall import *


class WindowFactory:
    """
        Factory to simplify drawing object with OpenGL
    """

    def __init__(self):
        """
            Constructor
        """
        self.window = pyglet.window.Window(400, 450, visible=False,
            resizable=True, caption='quoridor')
        self.window.set_minimum_size(400, 450)

        # Create items
        self.items = []  # Static items
        self.initPlayerItems()  # Player items
        self.initWallItems()  # Wall items
        self.setActivePlayerLabel()  # Active player label

        # Show the window
        self.draw()
        self.window.set_visible()

    def draw(self):
        """
            Clear and then draw all objects
        """
        self.window.clear()

        # Static items
        for item in self.items:
            item.draw()

        # Player items
        for item in self.player_items:
            item.draw()

        # Wall items
        for item in self.wall_items:
            item.draw()

        # Active player label item
        self.activePlayerLabel.draw()

    def createLabel(self, text, x, y, size=36, font='Liberation Sans'):
        """
            Create a label contening text, at position (x, y)
        """
        self.items += [Label(text, x, y, size, font)]

    def createLines(self, x1, y1, x2, y2, origin=[0, 0]):
        """
            Create a line from (x1, y1) to (x2, y2)
        """
        self.items += [Line(x1, y1, x2, y2, origin)]

    def createGrid(self, board, width, height):
        """
            Create a grid of size size_x, size_y
        """
        grid = Grid(board, width, height)
        self.items += [grid]
        return grid

    def initPlayerItems(self):
        """
            Remove all players
        """
        self.player_items = []

    def addPlayerItem(self, player, grid):
        """
            Create or move a player
        """
        self.player_items += [Player(player, grid)]

    def initWallItems(self):
        """
            Remove all wall
        """
        self.wall_items = []

    def addWallItem(self, coord, side, grid):
        """
            Create or move a wall
        """
        self.wall_items += [Wall(coord, side, grid)]

    def setActivePlayerLabel(self, activePlayerNb=1, nbWallPlayer=0):
        """
            Change the show number for the active player
        """
        label = 'Player ' + str(activePlayerNb) + " (" + str(nbWallPlayer) + ")"
        self.activePlayerLabel = Label(label, 50, 380, 16)
