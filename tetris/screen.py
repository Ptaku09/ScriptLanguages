import pygame as py


class Screen:
    def __init__(self, title, width=440, height=445, fill=(0, 0, 255)):
        self.height = height
        self.title = title
        self.width = width
        self.fill = fill
        self.current_state = False
        self.screen = None

    def make_current_screen(self):
        py.display.set_caption(self.title)
        self.current_state = True
        self.screen = py.display.set_mode((self.width, self.height))

    def hide_current_screen(self):
        self.current_state = False

    def check_update(self, fill):
        self.fill = fill
        return self.current_state

    def update(self):
        if self.current_state:
            self.screen.fill(self.fill)

    def get_title(self):
        return self.title
