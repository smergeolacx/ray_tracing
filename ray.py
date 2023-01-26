import pygame
from pygame.math import Vector2

class Ray:
    def __init__(self,x,y,screen):
        self.pos = Vector2(x,y)
        self.dir = Vector2(1,0)
        self.screen = screen

    def show(self):
        pygame.draw.line(self.screen, "white", self.pos, self.pos+self.dir*10)

    def point(self, newp):
        self.dir.x, self.dir.y = newp[0]/self.pos.x, newp[1]/self.pos.y