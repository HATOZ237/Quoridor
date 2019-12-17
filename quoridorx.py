"""ce module me permet de dessiner le graphe de notre partie de quooridor"""
import turtle
from quoridor import Quoridor


class QuoridorX(Quoridor):
    """classe du graphique"""

    def __init__(self, joueurs, murs=None):
        """j'herite de la classe qu0ridor puis j'installe le graphe"""
        super().__init__(joueurs, murs=murs)
        self.j1 = turtle.Turtle()
        self.j2 = turtle.Turtle()
        self.j1.shape("turtle")
        self.j2.shape("turtle")
        self.j1.color("purple")
        self.j2.color("green")
        self.screen = turtle.Screen()
        cardre()
        grille_v()
        deplacer(self.j1, (5, 1))
        deplacer(self.j2, (5, 9))
        self.j1.left(90)
        self.j2.left(-90)
        for x in self.partie["état"]["murs"]["horizontaux"]:
            placer_murh(x)
        for x in self.partie["état"]["murs"]["verticaux"]:
            placer_murv(x)

    def afficher(self, etat_n):
        """je ne sais pas encore ce que cette methode fait """
        etat_a = self.partie["état"]
        if etat_a["joueurs"][0]["pos"] != etat_n["joueurs"][0]["pos"]:
            a = etat_n["joueurs"][0]["pos"]
            deplacer(self.j1, a)
        if etat_a["joueurs"][1]["pos"] != etat_n["joueurs"][1]["pos"]:
            b = etat_n["joueurs"][1]["pos"]
            deplacer(self.j2, b)
        mh_a = etat_a["murs"]["horizontaux"]
        mh_n = etat_n["murs"]["horizontaux"]
        mv_a = etat_a["murs"]["verticaux"]
        mv_n = etat_n["murs"]["verticaux"]
        ch = controle(mh_a, mh_n)
        cv = controle(mv_a, mv_n)
        if ch is not False:
            for x in ch:
                placer_murh(x)
        if cv is not False:
            for x in cv:
                placer_murv(x)


def cardre():
    """cette fonction cree le fameux cardre en bordure noir """
    t = turtle.Turtle()
    t.hideturtle()
    t.speed(5)
    t.penup()
    t.pensize(5)
    t.goto(-250, -250)
    t.pendown()
    t.goto(-250, 250)
    t.goto(250, 250)
    t.goto(250, -250)
    t.goto(-250, -250)


def grille_v():
    """construction de ma grille"""
    a = [turtle.Turtle() for i in range(1, 11)]
    for t in a:
        t.speed(100)
    for t in a:
        t.hideturtle()
    for t in a:
        t.penup()
    for i, t in enumerate(a):
        t.goto(-225 + 50*(i), -225)
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


def placer_murh(pos):
    """placement des murs horizontaux"""
    t = turtle.Turtle()
    t.hideturtle()
    x, y = pos
    t.speed(1)
    t.penup()
    t.pensize(5)
    t.pencolor('blue')
    t.goto(-270+50*x, -275+50*y)
    t.pendown()
    t.setx(-180 + 50*x)


def placer_murv(pos):
    """placement des murs verticaux"""
    t = turtle.Turtle()
    t.hideturtle()
    x, y = pos
    t.speed(1)
    t.penup()
    t.pensize(5)
    t.pencolor('red')
    t.goto(-275+50*x, -270+50*y)
    t.pendown()
    t.sety(-180 + 50*y)


def deplacer(tortle, pos):
    """deplacer les tortues"""
    x, y = pos
    tortle.speed(2)
    tortle.penup()
    tortle.goto(-250 + 50*x, -250 + 50*y)


def controle(mura, murn):
    """controle qualite des murs"""
    if mura == murn:
        return False
    if mura == [] and murn != []:
        return [murn[-1]]
    if mura != []:
        if mura[-1] == murn[-1]:
            return False
        else:
            a = []
            for x in murn:
                if not (x in mura):
                    a.append(x)
            return a
