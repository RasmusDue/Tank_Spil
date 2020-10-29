#import pygame
import random
import math

#setup variables
display_width = 1280
display_height = 720

class Game():
    def __init__(self):
        self.tilstand = 0
        self.tank_move = False
        self.countdown = True
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
        self.t1 = Tank(self.blue, self.p1, self.tank1)
        self.t2 = Tank(self.red, self.p2, self.tank2)
        self.pball = [display_width/2-60,display_height/2-50]
        self.ball_png = []
        self.ball = Ball(self.pball, 1)
        self.ball_mask = []
        self.pball_red = []
        self.pball_blue = []
        self.red_ball = Ball(self.pball_red, 2)
        self.blue_ball = Ball(self.pball_blue, 3)
    #Sounds
        self.main_sound_volume = 0
        self.sound_crowd = []
        self.sound_back1 = []
        self.sound_countdown1 = []
        self.sound_countdown2 = []

        self.objects = Objects()
        self.objects.container.append(self.blue_ball)
        self.objects.container.append(self.red_ball)
        self.objects.container.append(self.ball)

        self.goal_left_mask = []
        self.goal_right_mask = []

        self.count_image = 0
        self.frame_image = 0

    def reset_ball(self):
        self.ball.speed_x = 0
        self.ball.speed_y = 0
        self.ball.position = [display_width/2-60,display_height/2-50]
        self.p1 = [1135,720/2-50]
        self.p2 = [45,720/2-50]
        self.angle1 = 90
        self.angle2 = -90

    def goal(self, team):
    #team 0 = red and team 1 = blue
        if team == 0:
            self.score[0] += 1
        elif team == 1:
            self.score[1] += 1
        self.reset_ball()

class Tank():
    def __init__(self, color, position, tank):
        self.size = 100
        self.color = color
        self.position = position
        self.speed = 8
        self.angle = 0
        self.tank_png = tank
        self.liv = 200

    def update(self):
        pass


class Ball():
    def __init__(self, position, id):
        self.speed_x = 0
        self.speed_y = 0
        self.size = 100
        self.position = position
        self.id = id

        self.result_xy = [0,0]

    def hasOverlapped(self, xy, radius):
        minDistance = 0.0 + radius + self.size/2
        distance = math.hypot(xy[0]-self.position[0],xy[1]-self.position[1])
        if distance >= minDistance:
            return False
        radians = math.atan2(xy[1]-self.position[1],xy[0]-self.position[0])
        overlap = 1 + (minDistance - distance)
        return (math.cos(radians) * overlap, math.sin(radians) * overlap, overlap)

    def setPosition(self, xy):
        self.position = xy

class Objects:
	def __init__(self):
		self.container = list([])
		self.overlap = list([])
    # def collision(self, x):
    #     self.overlap.append(self.container[x])
    #     while self.overlap:
    #         source = self.overlap[x]
    #         self.overlap.pop(x)
    #
    #         for index in range(1, len(self.container)):
    #             target = self.container[index]
    #             if target.id == source.id: continue
    #                 result = source.hasOverlapped((target.position[0]+50, target.position[1]+50), 50)
    #                 if result:
    #                     target.position[0] += result[0]
    #                     target.position[1] += result[1]
    #                     self.overlap.append(target)

	def collision(self, x, g_ball):
		# self.overlap.append(self.container[x])
		# while self.overlap:
		# 	source = self.overlap[0]
		# 	self.overlap.pop(0)

			#for index in range(1, len(self.container)):
                #target = self.container[index]
			#if target.id == source.id: continue

            #target = self.append(self.container[x])

		result = x.hasOverlapped((g_ball.position[0]+50, g_ball.position[1]+50), 50)
		if result:
			g_ball.speed_x = result[0]
			g_ball.speed_y = result[1]
        #print("x: {} y: {}".format(result[0],result[1]))
			#self.overlap.append(target)
