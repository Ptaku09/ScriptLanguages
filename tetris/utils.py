from enum import Enum

import pygame


def get_font(size):
    return pygame.font.Font("assets/fonts/tetris.ttf", size)


class FieldSize(Enum):
    SMALL = "5x10"
    MEDIUM = "7x12"
    LARGE = "9x14"
