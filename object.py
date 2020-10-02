import pygame
import random

#setup pygame
pygame.init()

class tanks():
    def __init__(self, color, position, tank):
        self.size = 100
        self.color = color
        self.position = position
        self.speed = 4
        self.angle = 0
        self.png = pygame.transform.scale(tank, (self.size, self.size))

    def update(self, frame):
        tank_rotate = pygame.transform.rotate(self.png,self.angle)
        frame.blit(tank_rotate, (self.position[0], self.position[1]))
