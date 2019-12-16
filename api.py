""" C'est le module dans lequel le jeu contacte le serveur"""

import requests
import argparse
from copy import deepcopy
import quoridorx
import quoridor


def débuter_partie(idul):
    """ renvoit les informations d'un début de partie """
    url_base = 'https://python.gel.ulaval.ca/quoridor/api/'
    rep = requests.post(url_base+'débuter/', data={'idul': idul})
    rep = rep.json()
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
    parser.add_argument(
        'idul', help='Jouer en mode manuel contre le serveur.', type=str)
    parser.add_argument('-a', '--automatique', action='store_true',
                        help='Jouer en mode automatique contre le serveur.')
    parser.add_argument('-x', '--manuel', action='store_true',
                        help='Jouer en mode manuel contre le serveur avec affichage graphique.')
    parser.add_argument('-ax', '--automatiquex', action='store_true',
                        help='Jouer en mode automatique contre le serveur avec affichage graphique.')
    return parser.parse_args()
