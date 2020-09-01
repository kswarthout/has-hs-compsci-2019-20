import pygame
from settings import *


class Grid:
    def __init__(self):
        self.selected = None
        self.locked_cells = []
        self.incorrect_cells = []

    def update(self, mouse):
        pass

    def draw(self, window):
        # shade selected
        if self.selected:
            self.draw_selection(window, self.selected)

        # shade locked cells
        self.shade_locked_cells(window, self.locked_cells)
        self.shade_incorrect_cells(window, self.incorrect_cells)

        self.draw_grid(window)

####### BOARD CHECKING METHODS #########
    def check_all_cells(self):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != self.grid_finished[yidx][xidx]:
                    self.incorrect_cells.append([xidx, yidx])
        # self.check_rows()
        # self.check_cols()
        # self.check_region()

####### HELPER METHODS #########
    def draw_grid(self, window):
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

    def shade_locked_cells(self, window, locked):
        for cell in locked:
            x = cell[0] * cell_size + grid_pos[0]
            y = cell[1]*cell_size + grid_pos[1]
            pygame.draw.rect(window, LOCKED_CELL_COLOR,
                             (x, y, cell_size, cell_size))

    def shade_incorrect_cells(self, window, incorrect):
        for cell in incorrect:
            if self.grid[cell[1]][cell[0]] != 0:
                x = cell[0] * cell_size + grid_pos[0]
                y = cell[1]*cell_size + grid_pos[1]
                pygame.draw.rect(window, INCORRECT_CELL_COLOR,
                                 (x, y, cell_size, cell_size))

    def mouse_on_grid(self):
        if self.mouse_pos[0] < grid_pos[0] or self.mouse_pos[1] < grid_pos[1]:
            return False
        elif self.mouse_pos[0] > grid_pos[0] + grid_size or self.mouse_pos[1] > grid_pos[1] + grid_size:
            return False
        return ((self.mouse_pos[0] - grid_pos[0]) // cell_size, (self.mouse_pos[1] - grid_pos[1]) // cell_size)
