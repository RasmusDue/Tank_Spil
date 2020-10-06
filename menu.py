import pygame




done = False
pygame.init()
clock = pygame.time.Clock()
display_width = 1280
display_height = 720
display = pygame.display.set_mode((display_width, display_height), pygame.FULLSCREEN)
pygame.display.set_caption('Tanks Game - Brought To You By Oliver & Rasmus')
myfont = pygame.font.SysFont("comicsansms", 68)

def menu():
    baggrund_menu = pygame.image.load('Menu_wallpaper.png')
    baggrund_menu = pygame.transform.scale(baggrund_menu, (1280,720))

    display.blit(baggrund_menu,(0, 0))
    mouse = pygame.mouse.get_pos()

    if 1050+200 > mouse[0] > 200 and 300+75 > mouse[1] > 300:
        pygame.draw.rect(display, (200,200,200), (1050,300,200,75))
    #else:
        #pygame.draw.rect(display, (250,250,250), (1050,300,200,75),0)
    display.blit(myfont.render("PLAY", 100, (255,255,255)), (1050,300+20))







while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    menu()

    pygame.display.update()
    clock.tick(60)
