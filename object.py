import pygame
import random

#setup pygame
pygame.init()

class circle():
    def __init__(self, color, position): # controls):
        self.size = 100
        self.color = color
        self.position = position
        #self.controls = controls
        self.speed = 4

    # def move(self):
    #     keys = pygame.key.get_pressed()
    #     #circle 1
    #     con1 = self.controls[0]
    #     con2 = self.controls[1]
    #     con3 = self.controls[2]
    #     con4 = self.controls[3]
    #
    #     if keys[pygame.con1] and self.position[0]>25:
    #         self.postiton[0] -= self.speed
    #     if keys[pygame.con2] and self.position[0]<775:
    #         self.postiton[1] += self.speed
    #     if keys[pygame.con3] and self.position[1]>25:
    #         self.postiton[2] -= self.speed
    #     if keys[pygame.con4] and self.position[1]<575:
    #         self.postiton[3] += self.speed

    def update(self, frame, tank): # position):
        #self.position = position
        #pygame.draw.circle(frame, self.color, (self.position[0], self.position[1]), self.size)
        frame.blit(pygame.transform.scale(tank, (self.size, self.size)), (self.position[0], self.position[1]))
# controls1 = ["K_LEFT", "K_RIGHT", "K_UP", "K_DOWN"]
# print(controls1[0])
