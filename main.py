"""Точка входа"""
import pygame
import pygame.mixer
import sys
from game import Game


def main():
    pygame.mixer.pre_init(44100, -16, 1, 2048)
    pygame.mixer.init()
    pygame.init()
    pygame.font.init()
    game = Game()
    game.main_loop()
    sys.exit()


if __name__ == '__main__':
    main()
