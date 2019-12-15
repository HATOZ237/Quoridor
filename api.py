""" C'est le module dans lequel le jeu contacte le serveur"""

import requests
import argparse
from copy import deepcopy
from quoridorx import *
import quoridor


def affichage_graphique(état):
    pass

def débuter_partie(idul):
    """ renvoit les informations d'un début de partie """
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    rep = rep.json()
    print(rep)
    if 'id' in rep and 'état' in rep:
        return (rep['id'], rep['état'])
    print(rep['message'])
    raise RuntimeError


def jouer_coup(id_partie, type_coup, position):
    """ Permet à l'utilisateur d'effectuer des actions"""
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    payload = {'id': id_partie, 'type': type_coup, 'pos': position}
    rep = requests.post(url_base+'jouer/', data=payload)
    rep = rep.json()
    if 'message' in rep:
        raise RuntimeError(rep['message'])
    elif 'gagnant' in rep:
        raise StopIteration(rep["gagnant"])
    else:
        return rep['état']


def analyser_commande():
    """ analyseur de ligne de commande """
    parser = argparse.ArgumentParser(description='Jeu Quoridor - phase 1')
    parser.add_argument('idul', help='Jouer en mode manuel contre le serveur.', type=str)
    parser.add_argument('-a', '--automatique', action='store_true',
                        help='Jouer en mode automatique contre le serveur.')
    parser.add_argument('-x', '--manuel', action='store_true',
                        help='Jouer en mode manuel contre le serveur avec affichage graphique.')
    parser.add_argument('-ax', '--automatiquex', action='store_true',
                        help='Jouer en mode automatique contre le serveur avec affichage graphique.')
    return parser.parse_args()

def mode_manuel_simple(idul):
    (identifiant, état) = débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    fen = Quoridorx(état["joueurs"], état["murs"])
    while start:
        print(  "\t Entre le type de coup que tu veux effectuer -- \n:"
                "\t 'D' pour déplacer le jeton \n"
                "\t 'MH' pour placer un mur horizontal \n"
                "\t ou 'MV' pour placer un mur vertical ")
        type_coup = input('\t')
        position = []
        print('Entre la position (x, y) correspondante')
        position.append(input('Entre la position x correspondante'))
        position.append(input('Entre la position y correspondante'))
        try:
            Q1.partie['état'] = jouer_coup(identifiant, type_coup, position)
            fen.afficher(Q1.partie['état'])
            fen.partie['état'] = Q1.partie["état"]
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False 
        except RuntimeError as err:
            print(err)

def mode_manuel_complex(idul):
    (identifiant, état) = débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    while start:
        print(  "\t Entre le type de coup que tu veux effectuer -- \n:"
                "\t 'D' pour déplacer le jeton \n"
                "\t 'MH' pour placer un mur horizontal \n"
                "\t ou 'MV' pour placer un mur vertical ")
        type_coup = input('\t')
        position = []
        print('Entre la position (x, y) correspondante')
        position.append(input('Entre la position x correspondante'))
        position.append(input('Entre la position y correspondante'))
        try:
            Q1.partie['état'] = jouer_coup(identifiant, type_coup, position)
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False 
        except RuntimeError as err:
            print(err)

def mode_automatique_simple(idul):
    (identifiant, état) = débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    while start:
        print(Q1)
        Q1.jouer_coup(1)
        try:
            Q1.partie['état'] = jouer_coup(identifiant, type_coup, position)
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False 
        except RuntimeError as err:
            print(err)

if __name__ == "__main__":
    args = analyser_commande()
    mode_manuel_simple(args.idul)
mainloop()