import pygame

# https://www.pygame.org/docs/ref/color.html
# https://github.com/pygame/pygame/blob/master/src_py/colordict.py

RED = pygame.color.Color('red')
YELLOW = pygame.color.Color('yellow')
BLUE = pygame.color.Color('blue')
GREEN = pygame.color.Color('green')
BLACK = pygame.color.Color('black')
WHITE = pygame.color.Color('white')
ORANGE = pygame.color.Color('orange')

# menu font
pygame.font.init()
FONT = 'system/bank_ghothic_medium.ttf'

# files
SETTINGS_PATH = 'settings.json'
SAVE_PATH = 'data.txt'
