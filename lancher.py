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
myfont2 = pygame.font.SysFont("arial", 42)
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (200, 0 , 0)
ball=False


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
baggrund_menu = pygame.image.load('Menu_wallpaper.png').convert_alpha()
baggrund_menu = pygame.transform.scale(baggrund_menu, (1280,720))

map1 = pygame.image.load('background1(1).png').convert_alpha()
map1 = pygame.transform.scale(map1, (1280,720))
map2 = pygame.image.load('background 2.png').convert_alpha()
map2 = pygame.transform.scale(map2, (1280,720))

tank1 = pygame.image.load('blaa_tank.png').convert_alpha()
tank_png1 = pygame.transform.scale(tank1, (100, 100))
tank1_mask = pygame.mask.from_surface(tank_png1)
tank1_rect = tank_png1.get_rect()


tank2 = pygame.image.load('rod_tank.png').convert_alpha()
tank_png2 = pygame.transform.scale(tank2, (100, 100))
tank2_mask = pygame.mask.from_surface(tank_png2)
tank2_rect = tank_png2.get_rect()

ball = pygame.image.load('bold.png').convert_alpha()
ball_png = pygame.transform.scale(ball, (100, 100))

bullet_image = pygame.image.load("ball.png")
bullet_image = pygame.transform.scale(bullet_image, (20,20))
ball_mask = pygame.mask.from_surface(ball_png)
ball_rect = ball_png.get_rect()
ballx = display_width/2 - ball_rect.center[0]
bally = display_height/2 - ball_rect.center[1]

#game
game = Game()
game.tank1 = tank_png1
game.tank2 = tank_png2
game.ball_png = ball_png
game.sound_crowd = lyd_crowd
game.pball = [ballx, bally]
game.ball_mask = ball_mask
#game.sound_back1 = lyd_back1

#random map
random_map = random.randint(0,1)
print(random_map)
if random_map == 0:
    game.map = map1
elif random_map == 1:
    game.map = map2

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
    display.blit(myfont.render("PLAY", 100, (255,255,255)), (1050,300+20))

    display.blit(myfont2.render("Sound: {}".format(int(game.main_sound_volume*100)), 100, (255,255,255)), (1000,0))

    #Vol-Up
    if 1000+200> mouse[0] > 1000 and 100+75 > mouse[1] > 100:
        pygame.draw.rect(display, (200,200,200), (1000,100,200,80))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.main_sound_volume <= 0.9:
                game.main_sound_volume += 0.1
                game.main_sound_volume = round(game.main_sound_volume,2)
    display.blit(myfont2.render("Vol-Up", 100, (255,255,255)), (1000,100))
    #Vol-Down
    if 1000+200> mouse[0] > 1000 and 200+75 > mouse[1] > 200:
        pygame.draw.rect(display, (200,200,200), (1000,200,200,80))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if game.main_sound_volume >= 0.1:
                game.main_sound_volume -= 0.1
                game.main_sound_volume = round(game.main_sound_volume,2)
    display.blit(myfont2.render("Vol-Down", 100, (255,255,255)), (1000,200))







    pygame.mixer.music.set_volume(game.main_sound_volume)

    if 1050+200> mouse[0] > 1050 and 500+75 > mouse[1] > 500:
        pygame.draw.rect(display, (200,200,200), (1050,500,200,100))
        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.quit()
    display.blit(myfont.render("QUIT", 100, (255,255,255)), (1050,500+20))


#Main game loop
def game_loop():
    keys = pygame.key.get_pressed()

    display.blit(game.map, (0, 0))
    display.blit(myfont.render("{}:{}".format(game.score[0], game.score[1]), 100, white), (display_width/2-50,20))
    tank1_rotate = pygame.transform.rotate(game.tank1,game.angle1)
    tank2_rotate = pygame.transform.rotate(game.tank2,game.angle2)

    game.t1_mask = pygame.mask.from_surface(tank1_rotate)
    game.t2_mask = pygame.mask.from_surface(tank2_rotate)
    tank_offset = (int(game.p2[0] - game.p1[0]), int(game.p2[1] - game.p1[1]))
    tank_collision = game.t1_mask.overlap(game.t2_mask, tank_offset)

    ball_offset_t1 = (int(game.pball[0] - game.p1[0]), int(game.pball[1] - game.p1[1]))
    ball_offset_t2 = (int(game.pball[0] - game.p2[0]), int(game.pball[1] - game.p2[1]))
    ball_collision_t1 = game.ball_mask.overlap(game.t1_mask, ball_offset_t1)
    ball_collision_t2 = game.ball_mask.overlap(game.t2_mask, ball_offset_t2)
    #game.ball.update()
    game.pball[0] += game.ball.speed_x
    game.pball[1] += game.ball.speed_y

    if ball_collision_t1:
        game.ball.speed_x = -8

    if ball_collision_t2:
        game.ball.speed_x = 8

    if tank_collision:
        print("Collision")
        #display.blit(myfont.render("Tank Collision", 50, red), (display_width/2-180,100))
        game.p1[0] -=  game.t1.speed
        game.p1[1] -=  game.t1.speed
        game.p2[0] +=  game.t2.speed
        game.p2[1] +=  game.t2.speed
        game.t1.liv1 -= 10
        game.t2.liv2 -= 10
    if game.t1.liv1 <=0 or game.t2.liv2 <=0:
        display.blit(myfont.render("TYYYYSKLANNNNNDDDD", 50, red), (display_width/2-180,100))


    #Tank controls
    if not tank_collision:
        #tank 1 controls
        if keys[pygame.K_LEFT] and game.p1[0]>0:
            game.p1[0] -= game.t1.speed
            game.angle1 = 90
        if keys[pygame.K_RIGHT] and game.p1[0]<display_width-100:
            game.p1[0] += game.t1.speed
            game.angle1 = -90
        if keys[pygame.K_UP] and game.p1[1]>0:
            game.p1[1] -= game.t1.speed
            game.angle1 = 0
        if keys[pygame.K_DOWN] and game.p1[1]<display_height-100:
            game.p1[1] += game.t1.speed
            game.angle1 = 180
        if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
            game.angle1 = 45
        if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
            game.angle1 = 135
        if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
            game.angle1 = -135
        if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
            game.angle1 = -45
        #tank 2 controls
        if keys[pygame.K_a] and game.p2[0]>0:
            game.p2[0] -= game.t2.speed
            game.angle2 = 90
        if keys[pygame.K_d] and game.p2[0]<display_width-100:
            game.p2[0] += game.t2.speed
            game.angle2 = -90
        if keys[pygame.K_w] and game.p2[1]>0:
            game.p2[1] -= game.t2.speed
            game.angle2 = 0
        if keys[pygame.K_s] and game.p2[1]<display_height-100:
            game.p2[1] += game.t2.speed
            game.angle2 = 180
        if keys[pygame.K_a] and keys[pygame.K_w]:
            game.angle2 = 45
        if keys[pygame.K_a] and keys[pygame.K_s]:
            game.angle2 = 135
        if keys[pygame.K_d] and keys[pygame.K_s]:
            game.angle2 = -135
        if keys[pygame.K_d] and keys[pygame.K_w]:
            game.angle2 = -45



    #Draw tanks & ball in game
    display.blit(tank1_rotate, (game.p1[0], game.p1[1]))
    display.blit(tank2_rotate, (game.p2[0], game.p2[1]))
    #display.blit(game.ball_png, (game.ball.position[0], game.ball.position[1]))
    display.blit(game.ball_png, (game.pball[0], game.pball[1]))
    RED = (255,0,0)
    GREEN = (0,255,0)
    pygame.draw.rect(display,RED,(1075,5,200,5))
    pygame.draw.rect(display,GREEN,(1075,5,game.t1.liv1,5))

    pygame.draw.rect(display,RED,(25,5,200,5))
    pygame.draw.rect(display,GREEN,(25,5,game.t2.liv2,5))


#    if keys[pygame.K_RETURN]:
    #    display.blit(bullet_image,(game.p1[0], game.p1[1]))

#    if keys[pygame.K_SPACE]:
    #    display.blit(bullet_image,(game.p2[0], game.p2[1]))


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

        #keys = pygame.key.get_pressed()
        # if keys[pygame.K_ESCAPE]:
        #     game.tilstand = 0
    #game_loop()
    if game.tilstand == 0:
        #print("Tilstand 0")
        menu()
    elif game.tilstand == 1:
        #print("Tilstand 1")
        game_loop()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_m):
            game.tilstand = 0
            print("tilstand = 0")
#pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.update()
    clock.tick(60)
