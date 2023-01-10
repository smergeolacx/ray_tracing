import pygame
from pygame import quit
from sys import exit
from obstacle import Obstacle
from settings import *

screen = pygame.display.set_mode((screenX,screenY))

pygame.init()
clock = pygame.time.Clock()

rect = Obstacle(30,30,100,100,screen)

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            quit()



    pygame.display.flip()
