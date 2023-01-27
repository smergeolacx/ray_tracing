import pygame
from pygame.math import Vector2
from math import sqrt

class Ray:
    def __init__(self,x,y,screen):
        self.pos = Vector2(x,y)
        self.dir = Vector2(0,1)
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, "white", self.pos, self.pos+self.dir*10)

    def point(self, newp):
        nx = newp[0]-self.pos.x
        ny = newp[1]-self.pos.y
        normal = sqrt((nx**2)+(ny**2))
        self.dir.x, self.dir.y = (nx)/normal, (ny)/normal