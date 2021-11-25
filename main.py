import pygame, sys, pickle, os

version = 1.0

pygame.init()

screen = pygame.display.set_mode((1280, 720))
pygame.display.set_caption(f'Pokemon First Form Edition v.{version}')

run = True
while run:
    for event in pygame.event.get():
        if event == pygame.QUIT:
            pygame.quit()
            run = False

    pygame.display.update()
    pygame.time.Clock.tick(120)