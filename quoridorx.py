from quoridor import *
from turtle import *


class Quoridorx(Quoridor):
    
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs=murs)
        
    def afficher(self):
        jeu = self.partie
        position = [1, 2]