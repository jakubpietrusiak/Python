import sys

import pygame
from setting import Settings

def run_game():
    #inicjacja gry i utworzenie objektu ekranu
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width ,
                                     ai_settings.screen_height))

    pygame.display.set_caption('Inwazja obcych')


    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color)
        pygame.display.flip()

run_game()