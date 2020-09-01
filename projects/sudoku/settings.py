# WINDOW DIMENSIONS
WIDTH = 850
HEIGHT = 550

# POSITIONS & SIZES
grid_pos = (50, 50)
panel_pos = (550, 50)
panel_size = (250, 450)
status_size = (panel_size[0], 50)
status_pos = (panel_pos[0], panel_pos[1] + panel_size[1] - status_size[1])
cell_size = 50
grid_size = cell_size * 9
victory_size = 100
victory_pos = (panel_pos[0] + ((panel_size[0] - victory_size) / 2),
               panel_pos[1] + ((panel_size[1] - victory_size) / 2))
border_height = 25

# IMAGE LOCATIONS

# 0 - top normal
# 1 - top right
# 2 - top left
# 3 - bottom normal
# 4 - bottom right
# 5 - bottom left
# 6 - right normal
# 7 - left normal
border_img_locs = [(0, 0, 50, 25),
                   (50, 0, 50, 25),
                   (0, 25, 50, 25),
                   (50, 25, 50, 25),
                   (0, 50, 50, 25),
                   (50, 50, 50, 25),
                   (13, 75, 25, 25),
                   (63, 75, 25, 25)]


# COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (96, 216, 232)
LOCKED_CELL_COLOR = (189, 189, 189)
INCORRECT_CELL_COLOR = (195, 121, 121)
NEW_GAME_BUTTON_COLOR = (162, 201, 107)
NEW_GAME_BUTTON_COLOR_ALT = (162, 214, 107)
DARK_GRAY = (73, 73, 73)
LIGHT_GRAY = (189, 189, 189)
STATUS_BAR_COLOR = (163, 48, 240)
DARK_BLUE = (17, 52, 229)
BG_COLOR = (247, 247, 247)
PANEL_BG = (235, 235, 235)

# FOR TESTING
test_board = [[0 for i in range(9)] for j in range(9)]
test_board_2 = [[0, 9, 0, 0, 0, 0, 3, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0, 6],
                [0, 0, 0, 0, 0, 6, 0, 0, 0],
                [9, 8, 0, 0, 0, 0, 2, 0, 3],
                [0, 6, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 7, 0, 6, 0, 0],
                [8, 7, 0, 0, 0, 2, 0, 0, 0],
                [0, 0, 9, 0, 0, 0, 0, 0, 0],
                [0, 0, 6, 0, 0, 0, 0, 0, 0]]

test_board_2_finished = [[6, 9, 8, 7, 5, 4, 3, 2, 1],
                         [7, 5, 4, 3, 2, 1, 9, 8, 6],
                         [3, 2, 1, 9, 8, 6, 7, 5, 4],
                         [9, 8, 7, 6, 4, 5, 2, 1, 3],
                         [5, 6, 3, 2, 1, 9, 8, 4, 7],
                         [4, 1, 2, 8, 7, 3, 6, 9, 5],
                         [8, 7, 5, 4, 6, 2, 1, 3, 9],
                         [2, 4, 9, 1, 3, 7, 5, 6, 8],
                         [1, 3, 6, 5, 9, 8, 4, 7, 2]]
