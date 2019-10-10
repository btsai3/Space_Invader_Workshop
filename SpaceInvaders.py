import pygame
import os
import time
import datetime
import random
from os import path

pygame.init()
# Width of the Screen
Width = 460
# Height of the Screen
Height = 600
# FPS of game
FPS = 40
# test

clock = pygame.time.Clock()
img_dir = path.join(path.dirname("__img__"), "img")

screen = pygame.display.set_mode((Width, Height))
background = pygame.image.load(path.join(img_dir, "night.jpg")).convert()
background = pygame.transform.scale(background, (500, 600))
pygame.display.set_caption("Space Invaders")

pygame.image.load(path.join(img_dir, "ship2.png")).convert_alpha()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale("ship2.png", (25, 25))
        self.rect = self.image.get_rect()
        self.radius = 12
        # pygame.draw.circle(self.image, RED, self.rect.center)
        self.rect.centerx = Width / 2
        self.rect.bottom = Height - 30
        self.speedx = 0


def game_loop():
    clock.tick(FPS)
    running = True
    while running:
        # code for while loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            screen.blit(background, (0, 0))
            # blit changes the colors of pixels on screen
            pygame.display.flip()


game_loop()

pygame.quit()
