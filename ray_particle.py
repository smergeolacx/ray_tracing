import pygame
from math import radians
from ray import Ray


class Particle:
    def __init__(self, screen, ob, xy=(200, 400)):
        self.rays = []
        self.ob = ob
        self.x = xy[0]
        self.y = xy[1]
        self.screen = screen
        self.create_rays()

    def create_rays(self):
        for i in range(0, 360, 5):
            ray = Ray(self.x, self.y, self.screen, radians(i))
            self.rays.append(ray)

    def show_rays(self):
        for ray in self.rays:
            ray.show()
            ry = ray.cast(self.ob)
            if ry:
                pygame.draw.line(self.screen, "white", (self.x, self.y), (ry.x, ry.y))

    def collision(self):
        pass
