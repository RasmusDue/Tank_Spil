import pygame

pygame.init()

display_width = 800
display_height = 600
black = (0,0,0)

game_layout_display = pygame.display.set_mode((display_width, display_height))
# pygame.display.set_caption('Tanks Game - Brought To You By Itsourcecode.com')

def gameLoop():
    pygame.display.update()
    pygame.quit()
gameLoop()
