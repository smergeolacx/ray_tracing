import pygame

class Obstacle():
    def __init__(self,x,y,width,height,surface):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.surface = surface
        self.create()

    def create(self):
        pygame.draw.rect(self.surface,"white",pygame.Rect(self.x,self.y,self.width,self.height),2)