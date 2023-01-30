import math
from math import pi, cos, sin
import pygame
from pygame.math import Vector2
from math import sqrt


class Ray:
    def __init__(self, x, y, screen, angle=2 * pi):
        self.pos = Vector2(x, y)
        self.dir = Vector2(1, 0)
        self.angle = angle
        self.screen = screen
        self.pt = Vector2()

    def show(self):
        x, y = cos(self.angle), sin(self.angle)
        self.dir.x = x
        self.dir.y = y
        pygame.draw.line(self.screen, "white", self.pos, self.pos + self.dir * 10)

    def cast(self, obstacle):
        x1 = obstacle.a.x
        y1 = obstacle.a.y
        x2 = obstacle.b.x
        y2 = obstacle.b.y
        x3 = self.pos.x
        y3 = self.pos.y
        x4, y4 = self.pos.x + self.dir.x, self.pos.y + self.dir.y
        # pygame.draw.circle(self.screen,"white",(x4,y4),5)
        den = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
        if (den == 0):
            return None
        else:
            t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / den
            u = -((x1 - 2) * (y1 - y3) - (y1 - y2) * (x1 - x3)) / den
            if 0 < t < 1 and u > 0:
                self.pt.x = x1 + t * (x2 - x1)
                self.pt.y = y1 + t * (y2 - y1)
                return self.pt
            else:
                return None
