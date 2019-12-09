# -*- coding: utf-8 -*-
"""This is the Board class.
@author: Iooss
@license: MIT
"""

from case import *


class Board:
    """
    this method implement the board of the game
    """
    def __init__(self, size=9):
        """
            Constructor
        """
        self.size = size  # nomber of cases
        self.map = []  # 2D tabular with the cases
        self.nodes = []  # the nodes of the bard : each node contain
                        # 0 => nothing
                        # 1 => a horizontal wall
                        # 2 => a vertical wall
        # init of nodes
        for i in range(self.size - 1):
            self.nodes += [(self.size - 1) * [0]]

        # init of map
        for i in range(self.size):
            self.map += [[]]
            for j in range(self.size):
                self.map[i] += [Case()]

        # Place walls around the map
        for i in range(self.size):
            self.map[i][self.size - 1].placeWall(1)  # Top Walls
            self.map[self.size - 1][i].placeWall(2)  # Left Walls
            self.map[i][0].placeWall(3)  # Bottom Walls
            self.map[0][i].placeWall(4)  # Right Walls

    def placeWall(self, x, y, type):
        """
            Place a wall on the node of coordonate (x, y) of type "type"
            return True if the wall has been created, else False
        """
        if self.nodes[x][y] != 0:
            print("Erreur : impossible de placer un mur au niveau de ce noeud")
            return False

        if type == 1:  # horizontal
            # check if no wall are already here
            if x > 0:
                if self.nodes[x - 1][y] == 1:
                    return False
            if x < self.size - 2:
                if self.nodes[x + 1][y] == 1:
                    return False

            # the wall can be put
            self.nodes[x][y] = type
            self.map[x][y].placeWall(1)
            self.map[x + 1][y].placeWall(1)
            self.map[x][y + 1].placeWall(3)
            self.map[x + 1][y + 1].placeWall(3)
            return True

        if type == 2:  # vertical
            # check if no wall are already here
            if y > 0:
                if self.nodes[x][y - 1] == 2:
                    return False
            if y < self.size - 2:
                if self.nodes[x][y + 1] == 2:
                    return False

            # the wall can be put
            self.nodes[x][y] = type
            self.map[x][y].placeWall(2)
            self.map[x + 1][y].placeWall(4)
            self.map[x][y + 1].placeWall(2)
            self.map[x + 1][y + 1].placeWall(4)
            return True

    def resetBoard(self):
        """
            Create a 2D array contenant des objets "case"
        """
        self.__init__()

    def getCase(self, x, y):
        """
            Return la case correspondant a la position
        """
        return self.map[x][y]

    def checkPath(self, positionPlayer, destinations):
        """
            Check if the player can go to his destinations
        """
        alreadyExplore = []
        return self.resursiveCheckPath(positionPlayer, destinations,
            alreadyExplore)

    def resursiveCheckPath(self, pending, destinations, alreadyExplore):
        """
            this method find a path
            pending : [x,y]
        """
        #print(pending)

        if pending in alreadyExplore:
            return False
        if pending in destinations:
            return True

        alreadyExplore += [pending]

        if not self.map[pending[0]][pending[1]].hasWall(1):
            if self.resursiveCheckPath([pending[0], pending[1] + 1],
                    destinations, alreadyExplore):
                return True

        if not self.map[pending[0]][pending[1]].hasWall(2):
            if self.resursiveCheckPath([pending[0] + 1, pending[1]],
                    destinations, alreadyExplore):
                return True

        if not self.map[pending[0]][pending[1]].hasWall(3):
            if self.resursiveCheckPath([pending[0], pending[1] - 1],
                    destinations, alreadyExplore):
                return True

        if not self.map[pending[0]][pending[1]].hasWall(4):
            if self.resursiveCheckPath([pending[0] - 1, pending[1]],
                    destinations, alreadyExplore):
                return True

    def iterativCheckPath(self, positionPlayer, destinations):
        """
            Check if the player can go to his destinations
        """
        alreadyExplore = []
        toExplore = [positionPlayer]

        while toExplore:
            # Take the first element to analyse
            pending = toExplore[0]

            if pending in destinations:
                print("fini")
                return True

            toExplore = toExplore[1:]
            alreadyExplore += [pending]

            newCaseToExplore = []

            if not self.map[pending[0]][pending[1]].hasWall(1):
                newCase = [pending[0], pending[1] + 1]
                if not newCase in toExplore:
                    if not newCase in alreadyExplore:
                        newCaseToExplore += [newCase]

            if not self.map[pending[0]][pending[1]].hasWall(2):
                newCase = [pending[0] + 1, pending[1]]
                if not newCase in toExplore:
                    if not newCase in alreadyExplore:
                        newCaseToExplore += [newCase]

            if not self.map[pending[0]][pending[1]].hasWall(3):
                newCase = [pending[0], pending[1] - 1]
                if not newCase in toExplore:
                    if not newCase in alreadyExplore:
                        newCaseToExplore += [newCase]

            if not self.map[pending[0]][pending[1]].hasWall(4):
                newCase = [pending[0] - 1, pending[1]]
                if not newCase in toExplore:
                    if not newCase in alreadyExplore:
                        newCaseToExplore += [newCase]

            toExplore = newCaseToExplore + toExplore

        print("Rien...")
        return False
