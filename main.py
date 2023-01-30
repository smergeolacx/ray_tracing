import pygame
from pygame import quit
from sys import exit
from ray import Ray
from wall import Wall
from ray_particle import Particle

pygame.init()
clock = pygame.time.Clock()
height, width = 800, 800
screen = pygame.display.set_mode((width, height))

ray_cast = Ray(200, 400, screen)
obstacle = Wall(600, 200, 600, 600, screen)

while True:
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
            exit()

    screen.fill("black")
    ray_part = Particle(screen, obstacle, pygame.mouse.get_pos())
    obstacle.show()
    ray_cast.cast(obstacle)
    ray_part.show_rays()
    clock.tick(60)
    pygame.display.flip()
