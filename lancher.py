import pygame
import random
from object import Tanks
from object import Ball
from object import Game
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
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (200, 0 , 0)
p1 = [1150,1280/2-50]
p2 = [50,720/2-50]
pball = [display_width/2-100,display_height/2-50]
controls1 = ["K_LEFT", "K_RIGHT", "K_UP", "K_DOWN"]

#images
map1 = pygame.image.load('background1(1).png')
map1 = pygame.transform.scale(map1, (1280,720))
map2 = pygame.image.load('background 2.png')
map2 = pygame.transform.scale(map2, (1280,720))
map = []
tank1 = pygame.image.load('blaa_tank.png')
tank_png1 = pygame.transform.scale(tank1, (100, 100))
tank2 = pygame.image.load('rod_tank.png')
tank_png2 = pygame.transform.scale(tank2, (100, 100))
ball1 = pygame.image.load('bold.png')

#game
game = Game()
game.tank1 = tank_png1
game.tank2 = tank_png2

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


#Main game loop
def game_loop():
    keys = pygame.key.get_pressed()
#circle 1
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
    # if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
    #     c1.angle = 45
    # if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
    #     c1.angle = 135
    # if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
    #     c1.angle = -135
    # if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
    #     c1.angle = -45
#circle 2
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
    # if keys[pygame.K_a] and keys[pygame.K_w]:
    #     c2.angle = 45
    # if keys[pygame.K_a] and keys[pygame.K_s]:
    #     c2.angle = 135
    # if keys[pygame.K_d] and keys[pygame.K_s]:
    #     c2.angle = -135
    # if keys[pygame.K_d] and keys[pygame.K_w]:
    #     c2.angle = -45

    tank1_rotate = pygame.transform.rotate(game.tank1,game.angle1)
    tank2_rotate = pygame.transform.rotate(game.tank2,game.angle2)
    display.blit(game.map, (0, 0))
    display.blit(tank1_rotate, (game.p1[0], game.p1[1]))
    display.blit(tank2_rotate, (game.p2[0], game.p2[1]))
    #display.fill((0,0,0))
    #c1.update(display)
    #c2.update(display)

    #b.update(display)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    #game_loop()
    if game.tilstand == 0:
        print("Tilstand 0")
        #menu()
    elif game.tilstand == 1:
        print("Tilstand 1")
        game_loop()
#pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.update()
    clock.tick(60)
