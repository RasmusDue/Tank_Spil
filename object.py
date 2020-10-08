import pygame
import random

#setup variables
pygame.init()
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
        self.t1_mask = []
        self.t2_mask = []
        self.angle1 = 90
        self.angle2 = -90
        self.map = []
        self.t1 = Tank(self.blue, self.p1, self.tank1, self.t1_mask)
        self.t2 = Tank(self.red, self.p2, self.tank2, self.t2_mask)
        self.pball = []
        self.ball_png = []
        self.ball = Ball(self.pball, self.ball_png)
        self.ball_mask = []
    #Sounds
        self.main_sound_volume = 0.0
        self.sound_crowd = []
        self.sound_back1 = []



class Tank():
    def __init__(self, color, position, tank, mask):
        # Call the parent class (Sprite) constructor
        #pygame.sprite.Sprite.__init__(self)

        self.size = 100
        self.color = color
        self.position = position
        self.speed = 8
        self.angle = 0
        self.tank_png = tank
        self.mask = mask

    def update(self):
        pass

    def collision(self, other):
        offset = (int(other.position[0] - self.position[0]), int(other.position[1] - self.position[1]))
        mask = self.mask
        result = mask.overlap(other.mask, offset)
        if result:
            return True
        if not result:
            return False

class Ball():
    def __init__(self, position, png):
        self.speed_x = 0
        self.speed_y = 0
        self.size = 100
        self.position = position
        #self.ball_png = pygame.transform.scale(png, (self.size, self.size))

    def update(self):
        self.position[0] += 1
        self.position[1] += 1
