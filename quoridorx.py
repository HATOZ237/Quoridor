from quoridor import *
from turtle import *


class Quoridorx(Quoridor):

    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs=murs)
        j1 = Turtle()
        j2 = Turtle()
        self.screen = Screen()
        self.afficher()
        mainloop()

    def afficher(self):
        jeu = self.partie
        position = [1, 2]
        setup(width=500, height=500)
        cardre(self.screen)


def cardre(screen):
    scr = screen
    tortle = Turtle()
    penup()
    pensize(5)
    pendown()
    goto(0, 450)
    goto(450, 450)
    goto(450, 0)
    goto(0, 0)
    hideturtle()

état = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": (5, 6)},
        {"nom": "automate", "murs": 3, "pos": (5, 7)}
    ],
    "murs": {
        "horizontaux": [(4, 4), (2, 6), (3, 8), (5, 8), (7, 8)],
        "verticaux": [(6, 2), (4, 4), (2, 5), (7, 5), (7, 7)]
    }
}
jeu = Quoridorx(état['joueurs'], murs = état['murs'])