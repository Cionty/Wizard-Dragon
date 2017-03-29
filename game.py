import this
import math
import pygame
import time
from pygame.locals import *
import random
import sys, os

def draw_terrain():
    for x in range(0, math.ceil(1366/background_sprite.get_width())):
        for y in range(0, math.ceil(768/background_sprite.get_height())):
            pygame.Surface.blit(game_window, background_sprite, (x*background_sprite.get_width(), y*background_sprite.get_height()))

class Fireball:
    def __init__(self):
        self.fireball_sprite = pygame.transform.scale(pygame.image.load("Sprites/Fireball.png"), (70, 50))
        self.x = mage_x + 30
        self.y = mage_y + 40
        self.speed = 15

    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def get_sprite(self):
        return self.fireball_sprite
    def update(self):
        self.rect.y += 3

    def __str__(self):
        return "Fireball at " + str(self.x) + ", " + str(self.y) + " with speed: " + str(self.speed)

class Wizard:
    def __init__(self):
        self.attack = attack_sprite
        self.base = mage_sprite


def cast_fire():
    pygame.Surface.blit(game_window, attack_sprite, (mage_x, mage_y))
    #print("Current fireballs:", fireballs)
    fireballs.append(Fireball())

pygame.init()


fire = True
count = 0
mage_sprite = pygame.transform.scale(pygame.image.load("Sprites/basemage.png"), (80, 100))
attack_sprite = pygame.transform.scale(pygame.image.load("Sprites/attackskill.png"), (80, 100))
mage_x, mage_y = 10, 400
background_sprite = pygame.image.load("Sprites/Grass_double.jpg")
#fireball_sprite = pygame.image.load("Sprites/Fireball.png")# pygame.transform.scale(, (100, 70))
fireballs = []

game_window = pygame.display.set_mode((1366, 768), HWACCEL|HWSURFACE|FULLSCREEN)

FPS = 120
clock = pygame.time.Clock()
game_end = False

pygame.key.set_repeat(10, 10)
while not game_end:

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            game_end = True
        if event.type == KEYDOWN:
            if event.key == K_F4 or event.key == K_ESCAPE:
                game_end = True
            if event.key == K_SPACE:
                if fire == True:
                    cast_fire()
                    count = 0
                    fire = False
            if event.key == K_w:
                mage_y -= 10
            if event.key == K_s:
                mage_y += 10
            #if event.key == K_a:
            #    mage_x -= 10
            #if event.key == K_d:
            #    mage_x += 10
    # Game logic
    if mage_y < 0:
        mage_y = 0
    if mage_y > 768 - mage_sprite.get_height():
        mage_y = 768 - mage_sprite.get_height()


    if count == 15:
        fire = True
    count += 1

    # Display drawing
    pygame.Surface.fill(game_window, (0, 255, 0))
    draw_terrain()
    for fireball in fireballs:
        #print(fireball)
        #fireball.update
        pygame.Surface.blit(game_window, fireball.get_sprite(), (fireball.get_x(), fireball.get_y()))
        fireball.x += fireball.speed
        if fireball.get_x() > 1366:
            fireballs.remove(fireball)
        #if fireball.get_x() > 1366:
        #    fireball.remove()
        #      print("cancellata")
    pygame.Surface.blit(game_window, mage_sprite, (mage_x, mage_y))



    clock.tick(FPS)
    pygame.display.update()


pygame.quit()
sys.exit()
