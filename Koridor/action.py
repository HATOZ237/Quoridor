# -*- coding: utf-8 -*-


class Action:
    """
        This class create an object to encode the player wish of action
    """
    allActions = ["go_forward", "go_right", "go_backward", "go_left",
                "place_wall"]

    def __init__(self):
        """
            constructor
        """
        self.id = 0
        # 1 : forward
        # 2 : right
        # 3 : backward
        # 4 : left
        # 5 : wall

        self.wallCoordinate = [0, 0]
        self.wallType = 0
        # 1 : le mur commence en haut et s'etend a gauche
        # 2 : le mur commence a droite et s'etend en bas
        # 3 : le mur commence en bas et s'etend a gauche
        # 4 : le mur commence a geuche et s'etend en bas

    def stringToAction(self, actionString):
        """
            This method take a string and init the Action object depending of it
        """
        for i in range(4):
            if actionString == Action.allActions[i]:
                self.id = i + 1
                return True
        if actionString[:len(Action.allActions[4])] == Action.allActions[4]:
            # cas du placement de mur
            part = actionString.split()
            self.id = 5
            self.wallCoordinate = [int(part[1]), int(part[2])]
            self.wallType = int(part[3])
            return True

        return False
