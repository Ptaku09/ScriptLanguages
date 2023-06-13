import pygame as pg

from utils import get_font

pg.init()


class InputBox:
    def __init__(self, pos, w, h, color_inactive="White", color_active="#f0d467", font_size=32):
        self.rect = pg.Rect(pos[0], pos[1], w, h)
        self.color = color_inactive
        self.color_inactive = color_inactive
        self.color_active = color_active
        self.font = get_font(font_size)
        self.text = ""
        self.txt_surface = self.font.render("", True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False

            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Normalize and re-render the text.
                self._trim()
                self.txt_surface = self.font.render(self.text, True, self.color)

    # Trim the text to 16 characters
    def _trim(self):
        self.text = self.text[:16]

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 10))
        pg.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text
