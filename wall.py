import pygame
from pygame.math import Vector2

class Wall:
    def __init__(self, x1, y1, x2, y2, screen):
        self.a = Vector2(x1, y1)
        self.b = Vector2(x2, y2)
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, "white", self.a, self.b)
