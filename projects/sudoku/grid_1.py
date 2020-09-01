import pygame
from settings import *


class Grid:

    def __init__(self, audio):
        self.audio = audio
        self.mouse_pos = None
        self.selected = None
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.grid_finished = [[0 for i in range(9)] for j in range(9)]

    def update(self, mouse_pos):
        self.mouse_pos = mouse_pos

    def draw(self, window):

        # shade selected cell
        if self.selected:
            self.draw_selection(window, self.selected)

        # draw sudoku grid lines
        self.draw_grid(window)

####### HELPER METHODS #########

    def draw_grid(self, window):
        # self.draw_grid_border(window)
        gx = grid_pos[0]
        gy = grid_pos[1]
        gw = gx + grid_size - cell_size
        gh = gy + grid_size - cell_size
        pygame.draw.rect(window, BLACK, (gx, gy, gw, gh), 2)
        for x in range(9):
            vx = (grid_pos[0] + (x * cell_size), grid_pos[1])
            vy = (grid_pos[0] + (x * cell_size), grid_pos[1] + 450)
            hx = (grid_pos[0], grid_pos[1] + (x * cell_size))
            hy = (grid_pos[0] + 450, grid_pos[1] + (x * cell_size))
            pygame.draw.line(window, BLACK, vx, vy, 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, hx, hy, 2 if x % 3 == 0 else 1)

    def draw_selection(self, window, pos):
        x = pos[0] * cell_size + grid_pos[0]
        y = pos[1] * cell_size + grid_pos[1]
        pygame.draw.rect(
            window, LIGHT_BLUE, (x, y, cell_size, cell_size))

    def get_selected(self):
        selected = self.mouse_on_grid()
        if selected:
            self.audio.select_cell()
            self.selected = selected
        else:
            self.selected = None

    def mouse_on_grid(self):
        if self.mouse_pos[0] < grid_pos[0] or self.mouse_pos[1] < grid_pos[1]:
            return False
        elif self.mouse_pos[0] > grid_pos[0] + grid_size or self.mouse_pos[1] > grid_pos[1] + grid_size:
            return False
        return ((self.mouse_pos[0] - grid_pos[0]) // cell_size, (self.mouse_pos[1] - grid_pos[1]) // cell_size)

    # def update(self, mouse_pos):
    #     self.mouse_pos = mouse_pos
