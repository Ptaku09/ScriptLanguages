import pygame as py


class Button:
    def __init__(self, x, y, sx, sy, bg_color, font_bg_color, font_color, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.font_size = 25
        self.bg_color = bg_color
        self.font_bg_color = font_bg_color
        self.font_color = font_color
        self.text = text
        self.current_state = False
        self.button_font = py.font.Font('./fonts/ubuntu.ttf', self.font_size)

    def show_button(self, display):
        if self.current_state:
            py.draw.rect(display, self.font_bg_color, (self.x, self.y, self.sx, self.sy))
        else:
            py.draw.rect(display, self.bg_color, (self.x, self.y, self.sx, self.sy))

        text_surface = self.button_font.render(self.text, False, self.font_color)
        text_x = self.x + (self.sx / 2) - (self.font_size / 2) * (len(self.text) / 2) - 5
        text_y = self.y + (self.sy / 2) - (self.font_size / 2) - 4
        display.blit(text_surface, (text_x, text_y))

    def focus_check(self, mouse_pos, mouseclick):
        if self.x <= mouse_pos[0] <= self.x + self.sx and self.y <= mouse_pos[1] <= self.y + self.sy:
            self.current_state = True
            return mouseclick[0]
        else:
            self.current_state = False
            return False
