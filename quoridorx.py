from quoridor import *
from turtle import *


class Quoridorx(Quoridor):

    def __init__(self, joueurs, murs=None):
        super().__init__(joueurs, murs=murs)
        j1 = Turtle()
        j2 = Turtle()
        self.screen = Screen()
        cardre(self.screen)
        grille_v(self.screen)
        mainloop()

    def afficher(self):
        jeu = self.partie
        position = [1, 2]
        setup(width=500, height=500)
       # cardre(self.screen)
       # mainloop()


def cardre(screen):
    scr = screen
    tortle = Turtle()
    penup()
    pensize(5)
    goto(-225, -225)
    pendown()
    goto(-225, 225)
    goto(225, 225)
    goto(225, -225)
    goto(-225, -225)
    tortle.color("red")
    hideturtle()

    
def grille_v(screen):
    scr = screen
    a = [Turtle() for i in range(1, 10)]
    for t in a:
        t.penup()
    for i, t in enumerate(a):
        t.goto(-225 +50*(i+1), -225)
    for t in a:
        t.pendown()
    for t in a:
        t.sety(225)
    for t in a:
        t.penup()
    for i, t in enumerate(a):
        t.goto(-225, -225++50*(i+1))
    for t in a:
        t.pendown()
    for t in a:
        t.setx(225)

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