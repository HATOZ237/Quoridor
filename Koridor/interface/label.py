# -*- coding: utf-8 -*-
import pyglet.text


class Label():
    """
        Label contening text, high customizable
        The label bottom left position is (x, y)
    """

    def __init__(self, text, x, y, size=36, font='Liberation Sans'):
        """
            Constructor
        """
        self.label = pyglet.text.Label(
                text,
                font_name=font, font_size=size,
                x=x,
                y=y
            )

    def draw(self):
        """
            Draw the object
        """
        self.label.draw()
