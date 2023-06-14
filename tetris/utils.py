from enum import Enum

import pygame


def get_font(size):
    return pygame.font.Font("assets/fonts/tetris.ttf", size)


def extract_field_size(field_size):
    return int(field_size.split("x")[0]), int(field_size.split("x")[1])


class FieldSize(Enum):
    SMALL = "16x8"
    MEDIUM = "18x10"
    LARGE = "20x12"
