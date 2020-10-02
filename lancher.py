import pygame
from object import circle

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
speed = 4
controls1 = ["K_LEFT", "K_RIGHT", "K_UP", "K_DOWN"]

#images
tank1 = pygame.image.load('blaa_tank.png')

#pygame.transform.scale(tank1, (45, 45))
tank2 = pygame.image.load('rod_tank.png')

c1 = circle(blue, p1) #, controls1)
c2 = circle(red, p2)

#Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    keys = pygame.key.get_pressed()
#circle 1
    if keys[pygame.K_LEFT] and c1.position[0]>25:
        c1.position[0] -= c1.speed
        c1.angle = 90
    if keys[pygame.K_RIGHT] and c1.position[0]<775:
        c1.position[0] += c1.speed
        c1.angle = -90
    if keys[pygame.K_UP] and c1.position[1]>25:
        c1.position[1] -= c1.speed
        c1.angle = 0
    if keys[pygame.K_DOWN] and c1.position[1]<575:
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
    if keys[pygame.K_a] and c2.position[0]>25:
        c2.position[0] -= c2.speed
    if keys[pygame.K_d] and c2.position[0]<775:
        c2.position[0] += c2.speed
    if keys[pygame.K_w] and c2.position[1]>25:
        c2.position[1] -= c2.speed
    if keys[pygame.K_s] and c2.position[1]<575:
        c2.position[1] += c2.speed

    display.fill((0,0,0))
    c1.update(display, tank1)
    #c1.move()
    c2.update(display, tank2)





        #pygame kommandoer til at vise grafikken og opdatere 60 gange i sekundet.
    #pygame.display.flip()

    pygame.display.update()
    clock.tick(60)
