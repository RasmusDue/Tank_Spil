import pygame
import random

#setup pygame
pygame.init()

class tanks():
    def __init__(self, color, position, tank):
        self.size = 100
        self.color = color
        self.position = position
        self.speed = 8
        self.angle = 0
        self.tank_png = pygame.transform.scale(tank, (self.size, self.size))

    def update(self, frame):
        tank_rotate = pygame.transform.rotate(self.tank_png,self.angle)
        frame.blit(tank_rotate, (self.position[0], self.position[1]))

    def collide(self, spriteGroup):
        if pygame.sprite.spritecollide(self, spriteGroup, False):
            self.speed = 0

class ball():
    def __init__(self, position, png):
        self.speed = 8
        self.size = 100
        self.position = position
        self.ball_png = pygame.transform.scale(png, (self.size, self.size))

    def update(self, frame):
        frame.blit(self.ball_png, (self.position[0], self.position[1]))
