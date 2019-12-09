# -*- coding: utf-8 -*-
import pyglet


class Line():
    """
        Line between (x1, y1) and (x2, y2) with an origin.
        Optionaly, a color (rgb) and a thickness.
    """

    def __init__(self, x1, y1, x2, y2, origin, color=[255, 255, 255], width=1):
        """
            Constructor
        """
        self.line = pyglet.graphics.vertex_list(
                    2,
                    ('v2i', (origin[0] + x1, origin[1] + y1,
                            origin[0] + x2, origin[1] + y2)),
                    ('c3B', (color[0], color[1], color[2],
                            color[0], color[1], color[2]))
        )
        self.width = width

    def draw(self):
        """
            Draw the object
        """
        pyglet.graphics.glLineWidth(self.width)
        self.line.draw(pyglet.gl.GL_LINES)
