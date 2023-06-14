from enum import Enum

from block import Block


class GameStates(Enum):
    START = "start"
    END = "end"


class Tetris:
    def __init__(self, pos, height, width):
        self.x = pos[0]
        self.y = pos[1]
        self.height = height
        self.width = width
        self.point_multiplier = height
        self.level = 2
        self.score = 0
        self.state = GameStates.START
        self.field = []
        self.zoom = 30
        self.block = None

        for _ in range(self.height):
            new_line = []
            for _ in range(self.width):
                new_line.append(0)
            self.field.append(new_line)

    def new_block(self):
        self.block = Block((3, 0))

    def intersects(self):
        intersection = False

        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    if i + self.block.y > self.height - 1 or j + self.block.x > self.width - 1 or \
                            j + self.block.x < 0 or self.field[i + self.block.y][j + self.block.x] > 0:
                        intersection = True

        return intersection

    def break_lines(self):
        lines = 0

        for i in range(1, self.height):
            zeros = 0
            for j in range(self.width):
                if self.field[i][j] == 0:
                    zeros += 1
            if zeros == 0:
                lines += 1
                for i2 in range(i, 1, -1):
                    for j in range(self.width):
                        self.field[i2][j] = self.field[i2 - 1][j]

        self._calculate_score(lines)
        self.level += lines

    def _calculate_score(self, lines):
        self.score += (1000 // self.point_multiplier) * self.level * lines ** 2

    def go_space(self):
        while not self.intersects():
            self.block.y += 1
        self.block.y -= 1
        self.freeze()

    def go_down(self):
        self.block.y += 1
        if self.intersects():
            self.block.y -= 1
            self.freeze()

    def freeze(self):
        for i in range(4):
            for j in range(4):
                if i * 4 + j in self.block.image():
                    self.field[i + self.block.y][j + self.block.x] = self.block.color
        self.break_lines()
        self.new_block()
        if self.intersects():
            self.state = GameStates.END

    def go_side(self, dx):
        old_x = self.block.x
        self.block.x += dx
        if self.intersects():
            self.block.x = old_x

    def rotate(self):
        old_rotation = self.block.rotation
        self.block.rotate()
        if self.intersects():
            self.block.rotation = old_rotation

    def get_speed(self):
        return max(14 - self.level, 6)
