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
img_dir = path.join(path.dirname("__img__"), 'img')
# screen size
screen = pygame.display.set_mode((Width, Height))
# game images
background = pygame.image.load(path.join(img_dir, "night.jpg")).convert()
background = pygame.transform.scale(background, (500, 600))
player_img = pygame.image.load(path.join(img_dir, "ship2.png")).convert_alpha()
# caption
pygame.display.set_caption("Space Invaders")

x_start = 20
x_end = 450
enemy_spawn_positions = []
while x_start <= x_end:
    enemy_spawn_positions.append(x_start)
    x_start += 40
rows_of_enemies = 8
enemies = []


def make_Enemies():
    y = 50
    for i in range(rows_of_enemies):
        for index in enemy_spawn_positions:
            if i <= 2:
                enemy = Aliens(index, y, 1)
            elif 2 <= i < 5:
                enemy = Aliens(index, y, 2)
            else:
                enemy = Aliens(index, y, 3)
            enemies.append(enemy)
        y = y + 30
    for i in enemies:
        all_sprites.add(i)
        aliens.add(i)


class Player(pygame.sprite.Sprite):

    def __init__(self):
        # This is to initialize the player sprite and all elements that come with it
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (25, 25))
        self.rect = self.image.get_rect()
        #		pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = Width / 2
        self.rect.bottom = Height - 30
        self.speedx = 0

    def update(self):
        self.speedx = 0
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            self.speedx = +5
        self.rect.x += self.speedx
        if self.rect.right > Width:
            self.rect.right = Width
        if self.rect.left < 0:
            self.rect.left = 0


class Aliens(pygame.sprite.Sprite):

    def __init__(self, x, y, enemy_type):
        pygame.sprite.Sprite.__init__(self)
        self.enemy_type = enemy_type
        filename = 'enemy{}.png'.format(self.enemy_type)
        img = pygame.image.load(path.join(img_dir, filename)).convert_alpha()
        self.image = img
        self.image = pygame.transform.scale(self.image, (16, 16))
        self.rect = self.image.get_rect()
        #		pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x = x
        self.rect.y = y
        self.speedx = 1

    def update(self):
        self.rect.x += self.speedx
        if self.rect.x > Width - 10:
            self.rect.x = Width - 10
            for self in enemies:
                self.speedx *= -1
                self.rect.y += 10
        if self.rect.x < 0:
            self.rect.x = 0
            for self in enemies:
                self.speedx *= -1
                self.rect.y += 10


def game_loop():
    running = True
    # while running == True:
    while running:
        # draw/ display
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        screen.blit(background, (0, 0))
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()


all_sprites = pygame.sprite.Group()
aliens = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
make_Enemies()

game_loop()

pygame.quit()
