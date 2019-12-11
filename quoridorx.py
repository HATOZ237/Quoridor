from quoridor import *
from turtle import *


class Quoridorx(Quoridor):
    
    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs=murs)
        afficher()
        
    def afficher(self):
        jeu = self.partie
        position = [1, 2]
        screen = Screen()
        setup(width=500, height=500)
        j1 = Turtle()
        j2 = Turtle()
        pencolor = 
        
def cardre(screen):
    scr = screen
    tortle = Turtle()