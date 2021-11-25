import pygame
import pickle
import os
import sys

pygame.init()

WIDTH = 1280
HEIGHT = 720
dim = [WIDTH, HEIGHT]

screen = pygame.display.set_mode(dim)

version = 1.0
pygame.display.set_caption(f'Pokemon First Form Edition v.{version}')
background = pygame.transform.scale(pygame.image.load('Assets/forest.png').convert(), dim)

def mainLoop():
    running = True
    clock = pygame.time.Clock()

    while running:
        # Event Run
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.quit()
        screen.blit(background, (0,0))

        pygame.display.update()
        clock.tick(120)

mainLoop()


