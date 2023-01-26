import pygame
from sys import exit
from ray import Ray
from wall import Wall
from math import sin, cos, pi

pygame.init()
clock = pygame.time.Clock()
height, width = 800, 800
screen = pygame.display.set_mode((width, height))

raycast = Ray(200, 400, screen)
obstacle = Wall(600, 200, 600, 600, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    raycast.show()
    # raycast.point(pygame.mouse.get_pos())
    obstacle.show()
    clock.tick(60)
    pygame.display.flip()