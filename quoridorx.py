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
        for x in self.partie["état"]["murs"]["horizontaux"]:
            placer_murh(self.screen, x)
        for x in self.partie["état"]["murs"]["verticaux"]:
            placer_murv(self.screen, x)
        mainloop()

    def afficher(self):
        jeu = self.partie
        position = [1, 2]
        setup(width=500, height=500)
       # cardre(self.screen)
       # mainloop()


def cardre(screen):
    speed(5)
    scr = screen
    tortle = Turtle()
    penup()
    pensize(5)
    goto(-250, -250)
    pendown()
    goto(-250, 250)
    goto(250, 250)
    goto(250, -250)
    goto(-250, -250)
    tortle.color("red")
    hideturtle()

    
def grille_v(screen):
    scr = screen
    a = [Turtle() for i in range(1, 11)]
    for t in a:
        t.hideturtle()
    for t in a:
        t.speed(5)
    for t in a:
        t.penup()
    for i, t in enumerate(a):
        t.goto(-225 +50*(i), -225)
    for t in a:
        t.pendown()
    for t in a:
        t.sety(225)
    for t in a:
        t.penup()
    for i, t in enumerate(a):
        t.goto(-225, -225++50*(i))
    for t in a:
        t.pendown()
    for t in a:
        t.setx(225)

def placer_murh(screen, pos):
    scr = screen
    x, y = pos
    penup()
    pensize(5)
    pencolor('blue')
    goto(-275+50*x, -275+50*y)
    pendown()
    setx(-175 + 50*x)

def placer_murv(screen, pos):
    scr = screen
    x, y = pos
    penup()
    pensize(5)
    pencolor('red')
    goto(-225+50*x, -275+50*y)
    pendown()
    sety(-175 + 50*y)
    

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