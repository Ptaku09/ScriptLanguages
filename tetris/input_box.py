import pygame as pg

from utils import get_font

pg.init()
color_inactive = pg.Color("White")
color_active = pg.Color("#f0d467")
font = get_font(32)


class InputBox:
    def __init__(self, pos, w, h):
        self.rect = pg.Rect(pos[0], pos[1], w, h)
        self.color = color_inactive
        self.text = ""
        self.txt_surface = font.render("", True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = not self.active
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = color_active if self.active else color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                # Normalize and re-render the text.
                self.normalize()
                self.txt_surface = font.render(self.text, True, self.color)

    def normalize(self):
        # Limit the length of the text to 16 characters
        self.text = self.text[:16]

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 10, self.rect.y + 10))
        pg.draw.rect(screen, self.color, self.rect, 2)

    def get_text(self):
        return self.text
