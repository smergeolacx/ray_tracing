import pygame
from sys import exit
from ray import Ray
from wall import Wall
from math import sin, cos, pi

pygame.init()
clock = pygame.time.Clock()
height, width = 800, 800
screen = pygame.display.set_mode((width, height))

ray_cast = Ray(200, 400, screen)
obstacle = Wall(600, 200, 600, 600, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill("black")
    ray_cast.show()
    ray_cast.point(pygame.mouse.get_pos())
    obstacle.show()

    x1, y1 = ray_cast.pos.x, ray_cast.pos.y
    x2, y2 = pygame.mouse.get_pos()
    x3, y3 = obstacle.a.x, obstacle.a.y
    x4, y4 = obstacle.b.x, obstacle.b.y
    denom = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)
    t = ((x1 - x3) * (y3 - y4) - (y1 - y3) * (x3 - x4)) / denom
    u = ((x1 - x3) * (y1 - y2) - (y1 - y3) * (x1 - x2)) / denom

    if denom != 0:
        if 0 <= t <= 1 and 0 <= u <= 1:
            print(True)
    else:
        pass

    clock.tick(60)
    pygame.display.flip()
