#import pygame
import random

#setup variables
display_width = 1280
display_height = 720

class Game():
    def __init__(self):
        self.tilstand = 0
        self.score = [0, 0]
        self.blue = (0, 0, 255)
        self.red = (200, 0 , 0)
        self.p1 = [1135,720/2-50]
        self.p2 = [45,720/2-50]
        self.tank1 = []
        self.tank2 = []
        self.angle1 = 90
        self.angle2 = -90
        self.map = []
        self.c1 = Tank(self.blue, self.p1, self.tank1)
        self.c2 = Tank(self.red, self.p2, self.tank2)
        self.pball = [display_width/2-60,display_height/2-50]
        self.ball_png = []
        self.ball = Ball(self.pball, self.ball_png)



class Tank():
    def __init__(self, color, position, tank):
        self.size = 100
        self.color = color
        self.position = position
        self.speed = 8
        self.angle = 0
        self.tank_png = tank

    def update(self):
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
