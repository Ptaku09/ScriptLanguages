import pygame

from utils import get_font

pygame.init()


class Checkbox:
    def __init__(self, pos, text="", color="White", check_color="#f0d467", font_size=22):
        self.x = pos[0]
        self.y = pos[1]
        self.color = color
        self.text = text
        self.cc = check_color
        self.fs = font_size
        self.checkbox_obj = pygame.Rect(self.x, self.y, 20, 20)
        self.checked = False

    def draw(self, screen):
        if self.checked:
            pygame.draw.rect(screen, self.cc, self.checkbox_obj)
        else:
            pygame.draw.rect(screen, self.color, self.checkbox_obj)

        font = get_font(self.fs)
        font_surf = font.render(self.text, True, self.color)
        w, h = font.size(self.text)
        font_pos = (self.x + 12 / 2 - w / 2 + 65, self.y + 12 / 2 - h / 2 + 3)
        screen.blit(font_surf, font_pos)

    def check_for_input(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and self.checkbox_obj.collidepoint(event.pos):
            return True

        return False
