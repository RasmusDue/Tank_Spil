import pygame
import random
from object import Game
game = Game()
from object import Tank
from object import Ball

import pygame_menu

#setup pygame
pygame.init()
display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Tanks Game - Brought To You By Oliver & Rasmus')


# Initialize game variables
done = False
clock = pygame.time.Clock()
myfont = pygame.font.SysFont("arial", 68)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (200, 0 , 0)

#Sounds
lyd_crowd = pygame.mixer.Sound("sounds/Crowd_0001.wav")
#lyd_back1 = pygame.mixer.music.load("sounds/main1.wav")

#pygame.mixer.music.load("sounds/main1.wav")

random_sound = random.randint(0,3)
print(random_sound)
if random_sound == 0:
    pygame.mixer.music.load("sounds/main1.wav")
elif random_sound == 1:
    pygame.mixer.music.load("sounds/main2.wav")
elif random_sound == 2:
    pygame.mixer.music.load("sounds/main3.wav")
elif random_sound == 3:
    pygame.mixer.music.load("sounds/main4.wav")
#pygame.mixer.music.set_volume(game.main_sound_volume)
pygame.mixer.music.play(0)
#print(game.main_sound_volume)

#images
baggrund_menu = pygame.image.load('Menu_wallpaper.png')
baggrund_menu = pygame.transform.scale(baggrund_menu, (1280,720))

map1 = pygame.image.load('background1(1).png')
map1 = pygame.transform.scale(map1, (1280,720))
map2 = pygame.image.load('background 2.png')
map2 = pygame.transform.scale(map2, (1280,720))
tank1 = pygame.image.load('blaa_tank.png')
tank_png1 = pygame.transform.scale(tank1, (100, 100))
tank2 = pygame.image.load('rod_tank.png')
tank_png2 = pygame.transform.scale(tank2, (100, 100))
ball = pygame.image.load('bold.png')
ball_png = pygame.transform.scale(ball, (100, 100))

#game
game = Game()
game.tank1 = tank_png1
game.tank2 = tank_png2
game.ball_png = ball_png
game.sound_crowd = lyd_crowd
#game.sound_back1 = lyd_back1

#random map
random_map = random.randint(0,1)
print(random_map)
if random_map == 0:
    game.map = map1
elif random_map == 1:
    game.map = map2



#create objects
#b = ball(pball, ball1)




#Game Menu
def menu():
    display.blit(baggrund_menu,(0, 0))

    #game.sound_back1.play(0)
    mouse = pygame.mouse.get_pos()
    #print(mouse)
    if 1050+200> mouse[0] > 1050 and 300+75 > mouse[1] > 300:
        pygame.draw.rect(display, (200,200,200), (1050,300,200,100))
        if event.type == pygame.MOUSEBUTTONDOWN:
            game.sound_crowd.play(0)
            game.tilstand = 1
    #else:
        #pygame.draw.rect(display, (250,250,250), (1050,300,200,75),0)
    display.blit(myfont.render("PLAY", 100, (255,255,255)), (1050,300+20))
    display.blit(myfont.render("QUIT", 100, (255,255,255)), (1050,500+20))

    display.blit(myfont.render("Sound: {}".format(game.main_sound_volume), 100, (255,255,255)), (1000,30))
    display.blit(myfont.render("Vol-Up", 100, (255,255,255)), (1000,100))
    if 1000+200> mouse[0] > 1000 and 100+75 > mouse[1] > 100:
        pygame.draw.rect(display, (200,200,200), (1000,100,200,80))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.main_sound_volume <= 0.9:
                game.main_sound_volume += 0.1
    display.blit(myfont.render("Vol-Down", 100, (255,255,255)), (1000,200))
    if 1000+200> mouse[0] > 1000 and 200+75 > mouse[1] > 200:
        pygame.draw.rect(display, (200,200,200), (1000,200,200,80))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.main_sound_volume >= 0.0:
                game.main_sound_volume -= 0.1
    pygame.mixer.music.set_volume(game.main_sound_volume)

    if 1050+200> mouse[0] > 1050 and 500+75 > mouse[1] > 500:
        pygame.draw.rect(display, (200,200,200), (1050,500,200,100))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()


#Main game loop
def game_loop():
    keys = pygame.key.get_pressed()
    #tank 1
    if keys[pygame.K_LEFT] and game.p1[0]>0:
        game.p1[0] -= 8
        game.angle1 = 90
    if keys[pygame.K_RIGHT] and game.p1[0]<display_width-100:
        game.p1[0] += 8
        game.angle1 = -90
    if keys[pygame.K_UP] and game.p1[1]>0:
        game.p1[1] -= 8
        game.angle1 = 0
    if keys[pygame.K_DOWN] and game.p1[1]<display_height-100:
        game.p1[1] += 8
        game.angle1 = 180
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        game.angle1 = 45
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        game.angle1 = 135
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        game.angle1 = -135
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        game.angle1 = -45
    #tank 2
    if keys[pygame.K_a] and game.p2[0]>0:
        game.p2[0] -= 8
        game.angle2 = 90
    if keys[pygame.K_d] and game.p2[0]<display_width-100:
        game.p2[0] += 8
        game.angle2 = -90
    if keys[pygame.K_w] and game.p2[1]>0:
        game.p2[1] -= 8
        game.angle2 = 0
    if keys[pygame.K_s] and game.p2[1]<display_height-100:
        game.p2[1] += 8
        game.angle2 = 180
    if keys[pygame.K_a] and keys[pygame.K_w]:
        game.angle2 = 45
    if keys[pygame.K_a] and keys[pygame.K_s]:
        game.angle2 = 135
    if keys[pygame.K_d] and keys[pygame.K_s]:
        game.angle2 = -135
    if keys[pygame.K_d] and keys[pygame.K_w]:
        game.angle2 = -45

    tank1_rotate = pygame.transform.rotate(game.tank1,game.angle1)
    tank2_rotate = pygame.transform.rotate(game.tank2,game.angle2)
    display.blit(game.map, (0, 0))
    display.blit(myfont.render("{}:{}".format(game.score[0], game.score[1]), 100, white), (display_width/2-50,20))
    display.blit(tank1_rotate, (game.p1[0], game.p1[1]))
    display.blit(tank2_rotate, (game.p2[0], game.p2[1]))
    display.blit(game.ball_png, (game.pball[0], game.pball[1]))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True
        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_ESCAPE] and game.tilstand == 1:
        #     game.tilstand = 0
    #game_loop()
    if game.tilstand == 0:
        #print("Tilstand 0")
        menu()
    elif game.tilstand == 1:
        #print("Tilstand 1")
        game_loop()
#pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.update()
    clock.tick(60)
