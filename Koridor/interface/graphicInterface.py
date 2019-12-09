# -*- coding: utf-8 -*-

from .windowFactory import *


class GraphicInterface:
    """
        Graphic interface of the game, created with OpenGL
        It used PyGlet to bind OpenGL to Python
    """

    def __init__(self, game, width=300, height=300):
        """
            Constructor
        """
        self.factory = WindowFactory()  # Factory
        self.factory.createLabel('quoridor', 50, 400)  # Title
        self.grid = self.factory.createGrid(game.board, width, height)  # Grid

        self.game = game  # for players & active player
        self.board = game.board  # for walls

        self.refresh()  # Place players & walls

    def refresh(self):
        """
            Method to refresh the interface
        """
        # Refresh players
        self.factory.initPlayerItems()
        for player in self.game.players:
            self.factory.addPlayerItem(player, self.grid)

        # Refresh walls
        self.factory.initWallItems()
        for i in range(self.board.size):
            for j in range(self.board.size):
                if self.board.map[i][j].hasWall(1):
                    self.factory.addWallItem([i, j], 1, self.grid)
                if self.board.map[i][j].hasWall(2):
                    self.factory.addWallItem([i, j], 2, self.grid)
                if self.board.map[i][j].hasWall(3):
                    self.factory.addWallItem([i, j], 3, self.grid)
                if self.board.map[i][j].hasWall(4):
                    self.factory.addWallItem([i, j], 4, self.grid)
