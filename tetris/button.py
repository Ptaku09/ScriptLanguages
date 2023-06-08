import pygame as py


class Button:
    def __init__(self, x, y, sx, sy, button_color, rect_color, font_color, text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.button_color = button_color
        self.rect_color = rect_color
        self.font_size = 25
        self.font_color = font_color
        self.text = text
        self.current_state = False
        self.button_font = py.font.Font('./fonts/ubuntu.ttf', self.font_size)

    def show_button(self, display):
        if self.current_state:
            py.draw.rect(display, self.rect_color,
                         (self.x, self.y,
                          self.sx, self.sy))
        else:
            py.draw.rect(display, self.rect_color,
                         (self.x, self.y,
                          self.sx, self.sy))

        text_obj = self.button_font.render(self.text, False, self.rect_color)

        display.blit(text_obj, (self.x + (self.sx / 2) - (self.font_size / 2) * (len(self.text) / 2) - 5,
                                (self.y + (self.sy / 2) - (self.font_size / 2) - 4)))

    def check_focus(self, mouse_pos, mouse_click):
        if self.x <= mouse_pos[0] <= self.x + self.sx and self.y <= mouse_pos[1] <= self.y + self.sy:
            self.current_state = True
            # on button click navigate to other screen
            return mouse_click[0]
        else:
            self.current_state = False
            return False
