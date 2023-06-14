import random

# All possible shapes of blocks come from this 4x4 matrix:
# 0   1    2   3
# 4   5    6   7
# 8   9   10  11
# 12  13  14  15
possible_shapes = [
    [[1, 5, 9, 13], [4, 5, 6, 7]],  # I
    [[4, 5, 9, 10], [2, 6, 5, 9]],  # Z
    [[6, 7, 9, 10], [1, 5, 6, 10]],  # S
    [[1, 2, 5, 9], [0, 4, 5, 6], [1, 5, 9, 8], [4, 5, 6, 10]],  # L
    [[1, 2, 6, 10], [5, 6, 7, 9], [2, 6, 10, 11], [3, 5, 6, 7]],  # another L
    [[1, 4, 5, 6], [1, 4, 5, 9], [4, 5, 6, 9], [1, 5, 6, 9]],  # small T
    [[1, 2, 5, 6]],  # square
]

# Possible colors for blocks
possible_colors = [
    (0, 0, 0),  # Black
    (46, 204, 113),  # Green
    (52, 152, 219),  # Blue
    (155, 89, 182),  # Purple
    (241, 196, 15),  # Yellow
    (243, 156, 18),  # Orange
    (231, 76, 60),  # Red
]


class Block:
    def __init__(self, pos):
        self.x = pos[0]
        self.y = pos[1]
        self.shape = random.randint(0, len(possible_shapes) - 1)
        self.color = random.randint(1, len(possible_colors) - 1)
        self.rotation = 0

    def image(self):
        return possible_shapes[self.shape][self.rotation]

    def rotate(self):
        self.rotation = (self.rotation + 1) % len(possible_shapes[self.shape])
