import pygame
from object import tanks

#setup pygame
pygame.init()
display_width = 800
display_height = 600
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Tanks Game - Brought To You By Oliver & Rasmus')


# Initialize game variables
done = False
clock = pygame.time.Clock()
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (200, 0 , 0)
p1 = [400,400]
p2 = [600,200]
controls1 = ["K_LEFT", "K_RIGHT", "K_UP", "K_DOWN"]

#images
tank1 = pygame.image.load('blaa_tank.png')

#pygame.transform.scale(tank1, (45, 45))
tank2 = pygame.image.load('rod_tank.png')

#create tank´s
c1 = tanks(blue, p1, tank1)
c2 = tanks(red, p2, tank2)

#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    keys = pygame.key.get_pressed()
#circle 1
    if keys[pygame.K_LEFT] and c1.position[0]>0:
        c1.position[0] -= c1.speed
        c1.angle = 90
    if keys[pygame.K_RIGHT] and c1.position[0]<700:
        c1.position[0] += c1.speed
        c1.angle = -90
    if keys[pygame.K_UP] and c1.position[1]>0:
        c1.position[1] -= c1.speed
        c1.angle = 0
    if keys[pygame.K_DOWN] and c1.position[1]<500:
        c1.position[1] += c1.speed
        c1.angle = 180
    if keys[pygame.K_LEFT] and keys[pygame.K_UP]:
        c1.angle = 45
    if keys[pygame.K_LEFT] and keys[pygame.K_DOWN]:
        c1.angle = 135
    if keys[pygame.K_RIGHT] and keys[pygame.K_DOWN]:
        c1.angle = -135
    if keys[pygame.K_RIGHT] and keys[pygame.K_UP]:
        c1.angle = -45
#circle 2
    if keys[pygame.K_a] and c2.position[0]>0:
        c2.position[0] -= c2.speed
        c2.angle = 90
    if keys[pygame.K_d] and c2.position[0]<700:
        c2.position[0] += c2.speed
        c2.angle = -90
    if keys[pygame.K_w] and c2.position[1]>0:
        c2.position[1] -= c2.speed
        c2.angle = 0
    if keys[pygame.K_s] and c2.position[1]<500:
        c2.position[1] += c2.speed
        c2.angle = 180
    if keys[pygame.K_a] and keys[pygame.K_w]:
        c2.angle = 45
    if keys[pygame.K_a] and keys[pygame.K_s]:
        c2.angle = 135
    if keys[pygame.K_d] and keys[pygame.K_s]:
        c2.angle = -135
    if keys[pygame.K_d] and keys[pygame.K_w]:
        c2.angle = -45

    display.fill((0,0,0))
    c1.update(display)
    c2.update(display)





#pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    pygame.display.update()
    clock.tick(60)
