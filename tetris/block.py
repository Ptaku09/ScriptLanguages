# All possible shapes of blocks come from this 4x4 matrix:
# 0   1    2   3
# 4   5    6   7
# 8   9   10  11
# 12  13  14  15
possible_shapes = [
    [0, 1, 4, 5],  # Square
    [0, 1, 2, 3],  # Line
    [0, 1, 5, 6],  # L
    [0, 1, 2, 6],  # Reverse L
    [0, 1, 2, 5],  # T
    [0, 1, 2, 4],  # S
    [1, 2, 4, 5],  # Z
    [1, 5, 9, 13],  # Vertical Line
    [2, 6, 9, 10, 11],  # big reversed T
]

# Possible colors for blocks
possible_colors = [
    (46, 204, 113),  # Green
    (52, 152, 219),  # Blue
    (155, 89, 182),  # Purple
    (241, 196, 15),  # Yellow
    (243, 156, 18),  # Orange
    (231, 76, 60),  # Red
]
