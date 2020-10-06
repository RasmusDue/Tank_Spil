#import pygame
import random

#setup pygame


class Game():
    def __init__(self):
        self.tilstand = 1
        self.blue = (0, 0, 255)
        self.red = (200, 0 , 0)
        self.p1 = [1150,720/2-50]
        self.p2 = [50,720/2-50]
        self.tank1 = []
        self.tank2 = []
        self.map = []
        self.c1 = Tanks(self.blue, self.p1, self.tank1)
        self.c2 = Tanks(self.red, self.p2, self.tank2)



class Tanks():
    def __init__(self, color, position, tank):
        self.size = 100
        self.color = color
        self.position = position
        self.speed = 8
        self.angle = 0
        self.tank_png = tank

    def update(self, frame):
        #tank_rotate = pygame.transform.rotate(self.tank_png,self.angle)
        #frame.blit(tank_rotate, (self.position[0], self.position[1]))
        pass


class Ball():
    def __init__(self, position, png):
        self.speed = 8
        self.size = 100
        self.position = position
        #self.ball_png = pygame.transform.scale(png, (self.size, self.size))

    def update(self, frame):
        #frame.blit(self.ball_png, (self.position[0], self.position[1]))
        pass
