import pygame, sys, pickle, os

version = 1.0

pygame.init()

WIDTH = 1280
HEIGHT = 720
dim = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(dim, pygame.RESIZABLE)
pygame.display.set_caption(f'Pokemon First Form Edition v.{version}')

run = True
clock = pygame.time.Clock()

while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            sys.exit()
            run = False

    pygame.display.update()
    clock.tick(120)

