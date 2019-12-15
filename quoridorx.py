from quoridor import *
from turtle import *
import time


class Quoridorx(Quoridor):

    def __init__(self, joueurs, murs=None):
        """j'herite de la classe qu0ridor puis j'installe le graphe"""
        super().__init__(joueurs, murs=murs)
        self.j1 = Turtle()
        self.j2 = Turtle()
        self.j1.shape("turtle")
        self.j2.shape("turtle")
        self.screen = Screen()
        cardre(self.screen)
        grille_v(self.screen)
        deplacer(self.j1, (5, 1))
        deplacer(self.j2, (5, 9))
        self.j1.left(90)
        self.j2.left(-90)
        for x in self.partie["état"]["murs"]["horizontaux"]:
            placer_murh(self.screen, x)
        for x in self.partie["état"]["murs"]["verticaux"]:
            placer_murv(self.screen, x)

    def afficher(self, etat_n):
        """je ne sais pas encore ce que cette methode fait """
        etat_a = self.partie["état"]
        if etat_a["joueurs"][0]["pos"] != etat_n["joueurs"][0]["pos"]:
            a = etat_n["joueurs"][0]["pos"]
            deplacer(self.j1, a)
        if etat_a["joueurs"][1]["pos"] != etat_n["joueurs"][1]["pos"]:
            deplacer(self.j2, etat_n["joueurs"][0]["pos"])
        if etat_a["murs"]["horizontaux"][-1] != etat_n["murs"]["horizontaux"][-1]:
            placer_murh(self.screen, etat_n["murs"]["horizontaux"][-1])
        if etat_a["murs"]["verticaux"][-1] != etat_n["murs"]["verticaux"][-1]:
            placer_murv(self.screen, etat_n["murs"]["verticaux"][-1])


def cardre(screen):
    """cette fonction cree le fameux cardre en bordure noir """
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
    hideturtle()

    
def grille_v(screen):
    """construction de ma grille"""
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
        t.goto(-225, -225+50*(i))
    for t in a:
        t.pendown()
    for t in a:
        t.setx(225)

def placer_murh(screen, pos):
    scr = screen
    x, y = pos
    speed(5)
    penup()
    pensize(5)
    pencolor('blue')
    goto(-270+50*x, -275+50*y)
    pendown()
    setx(-180 + 50*x)

def placer_murv(screen, pos):
    scr = screen
    x, y = pos
    speed(5)
    penup()
    pensize(5)
    pencolor('red')
    goto(-275+50*x, -270+50*y)
    pendown()
    sety(-180 + 50*y)
    
def deplacer(tortle, pos):
    x, y = pos
    tortle.penup()
    tortle.goto(-250 + 50*x, -250+ 50*y)
    
    
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
éta = {
    "joueurs": [
        {"nom": "idul", "murs": 7, "pos": (5, 2)},
        {"nom": "automate", "murs": 3, "pos": (5, 7)}
    ],
    "murs": {
        "horizontaux": [(4, 4), (2, 6), (3, 8), (5, 8), (7, 8)],
        "verticaux": [(6, 2), (4, 4), (2, 5), (7, 5), (7, 7)]
    }
}
jeu = Quoridorx(état['joueurs'], murs = état['murs'])
jeu.afficher(éta)
print(1 for i in range(10))
mainloop()