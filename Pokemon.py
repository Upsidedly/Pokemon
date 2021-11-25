import pygame
import sys
import random

pygame.init()
WIDTH = 800
HEIGHT = 600
dimensions = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(dimensions, pygame.RESIZABLE)
pygame.display.set_caption("Pokemon")
BGImage = pygame.transform.scale(pygame.image.load("BGImage.jpg"), dimensions).convert_alpha()


class pokemon:
    def __init__(self, name):
        self.name = name

    def images(self, tup):
        self.front = tup[0]
        self.back = tup[1]

    def draw(self, screen):
        screen.blit(self.front, (450, 85))
        screen.blit(self.back, (600, 700))


def draw_window(screen, BGImage, bulbasaur):
    screen.blit(BGImage, (0, 0))
    bulbasaur.draw(screen)
    pygame.display.update()


def main():
    clock = pygame.time.Clock()
    run = True
    clock.tick(60)
    # player1_hp = 100
    # player2_hp = 100
    # hp = player1_hp, player2_hp
    bulbasaur = pokemon("Bulbasaur")
    bulbasaur.images(
        (pygame.transform.scale(pygame.image.load("bulbasaur.png"), (500, 500)), pygame.image.load("bulbasaur.png")))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                quit()
                break
        draw_window(screen, BGImage, bulbasaur)


main()