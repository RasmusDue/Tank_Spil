import pygame
import pygame_menu

pygame.init()
surface = pygame.display.set_mode((600, 400))
done = False


def menu():
    menu = pygame_menu.Menu(400, 600, 'Tank Problem', theme=pygame_menu.themes.THEME_DARK)

    menu.add_text_input('Name :', default='John Doe')
    menu.add_selector('Map Selection :', [('Soccer field', 1), ('Space field', 2)], onchange=set_map)
    menu.add_button('Play', start_the_game)
    menu.add_button('Quit', pygame_menu.events.EXIT)
    menu.mainloop(surface)


def set_map(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    pass


while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            done = True

    menu()
