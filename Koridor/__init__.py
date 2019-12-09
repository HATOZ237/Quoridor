# -*- coding: utf-8 -*-
"""This project consists of recreating the Koridor game in Python.
@author: Iooss
@license: MIT
"""

from game import *
from interface.graphicInterface import *
from action import *
import pyglet
from pyglet.window import key
from pyglet.window import mouse

nbPlayer = 2
size = 9

# Create game and interface instance
game = Game(nbPlayer, size)
interface = GraphicInterface(game)


def play(actionString):
    """
        Function to play an action
    """
    action = Action()
    action.stringToAction(actionString)
    game.play(action)
    interface.refresh()


@interface.factory.window.event
def on_draw():
    """
        Event to clear & draw the window
    """
    interface.factory.draw()


@interface.factory.window.event
def on_key_press(symbol, modifiers):
    """
        Event to bind keys to actions
    """
    if symbol == key.Z or symbol == key.UP:
        play('go_forward')
    elif symbol == key.D or symbol == key.RIGHT:
        play('go_right')
    elif symbol == key.S or symbol == key.DOWN:
        play('go_backward')
    elif symbol == key.Q or symbol == key.LEFT:
        play('go_left')


@interface.factory.window.event
def on_mouse_press(x, y, button, modifiers):
    """
        Event to bind mouse to actions
    """
    x = interface.grid.getCaseColByAbsX(x)
    y = interface.grid.getCaseLineByAbsY(y)

    if x and y:
        if button == mouse.LEFT:
            play('place_wall ' + str(x) + ' ' + str(y) + ' 1')
        elif button == mouse.RIGHT:
            play('place_wall ' + str(x) + ' ' + str(y) + ' 2')

# Run Forest, run !
pyglet.app.run()
