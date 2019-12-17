""" cette fonction fonctionne """
import api
import quoridor
import quoridorx
import argparse


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


def mode_manuel_simple(idul):
    (identifiant, état) = api.débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    if état["joueurs"][0]['nom'] != idul:
        print(Q1.état_partie())
    while start:
        print(Q1)
        print("\t Entre le type de coup que tu veux effectuer -- \n:"
              "\t 'D' pour déplacer le jeton \n"
              "\t 'MH' pour placer un mur horizontal \n"
              "\t ou 'MV' pour placer un mur vertical ")
        type_coup = input('\n-')
        position = []
        print('Entre la position (x, y) correspondante')
        position.append(input('Entre la position x correspondante'))
        position.append(input('Entre la position y correspondante'))
        try:
            Q1.partie['état'] = api.jouer_coup(
                identifiant, type_coup, position)
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False
        except RuntimeError as err:
            print(err)


def mode_manuel_graphique(idul):
    """Jouer en mode manuel contre le serveur avec affichage graphique."""
    (identifiant, état) = api.débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    # j'implante le mode graphique
    fen = quoridorx.QuoridorX(état["joueurs"], état["murs"])
    while start:
        print(Q1.état_partie())
        print("Entre le type de coup que tu veux effectuer -- \n:"
              "\t 'D' pour déplacer le jeton \n"
              "\t 'MH' pour placer un mur horizontal \n"
              "\t ou 'MV' pour placer un mur vertical ")
        type_coup = input('\n- ')
        position = []
        print('Entre la position (x, y) correspondante')
        position.append(input('- Entre la position x correspondante: '))
        position.append(input('- Entre la position y correspondante: '))
        try:
            Q1.partie['état'] = api.jouer_coup(
                identifiant, type_coup, position)
            fen.afficher(Q1.partie['état'])  # j'actualise la partie
            # l'ancien etat comparé pour l'actualisation et c'est parti pour la boucle
            fen.partie['état'] = Q1.partie["état"]
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False
        except RuntimeError as err:
            print(err)


def mode_automatique_simple(idul):
    """Jouer en mode automatique contre le serveur."""
    (identifiant, état) = api.débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    if état["joueurs"][0]['nom'] != idul:
        print(Q1)
    while start:
        print(Q1)
        (position, type_coup) = Q1.jouer_coup(1)
        try:
            Q1.partie['état'] = api.jouer_coup(
                identifiant, type_coup, position)
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False
        except RuntimeError as err:
            print(err)


def mode_automatique_graphique(idul):
    """lance automatiquement le jeu graphiquement"""
    (identifiant, état) = api.débuter_partie(idul)
    Q1 = quoridor.Quoridor(état["joueurs"], état["murs"])
    start = True
    # j'implante le mode graphique
    fen = quoridorx.QuoridorX(état["joueurs"], état["murs"])
    while start:
        (position, type_coup) = Q1.jouer_coup(1)
        try:
            Q1.partie['état'] = api.jouer_coup(
                identifiant, type_coup, position)
            fen.afficher(Q1.partie['état'])  # j'actualise la partie
            # l'ancien etat comparé pour l'actualisation et c'est parti pour la boucle
            fen.partie['état'] = Q1.partie["état"]
        except StopIteration as err:
            print(f"le gagnant est: {err} ")
            start = False
        except RuntimeError:
            fen.afficher(Q1.partie['état'])
            fen.partie['état'] = Q1.partie["état"]
            

def jeu():
    """on met aussi pour mettre"""
    args = analyser_commande()
    if args.automatique:
        mode_automatique_simple(args.idul)
    elif args.manuel:
        mode_manuel_graphique(args.idul)
    elif args.automatiquex:
        mode_automatique_graphique(args.idul)
    else:
        mode_manuel_simple(args.idul)


jeu()
quoridorx.turtle.mainloop()
