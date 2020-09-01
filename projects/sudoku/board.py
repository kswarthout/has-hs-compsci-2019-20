import pygame
from pygame.locals import *
from cell import Cell


class Board:

    selected_num = 0
    # stores grid state for board
    # default value 9x9 grid of 0s
    board = [[0 for i in range(9)] for j in range(9)]
    sln = [[0 for i in range(9)] for j in range(9)]

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

    def __init__(self, background, cell_side, board_width, border_height):
        self.cell_side = cell_side
        self.board_width = board_width
        self.border_height = border_height
        bg_rect = background.get_rect()
        self.topx = ((self.cell_side * self.board_width + 1) +
                     self.cell_side) / self.board_width / 2
        self.topy = ((self.cell_side * self.board_width + 1) +
                     self.cell_side) / self.board_width / 2
        self.rect = Rect(self.topx + self.cell_side, self.topy + self.cell_side,
                         self.cell_side * self.board_width + self.cell_side * 2, self.cell_side * self.board_width + self.cell_side * 2)
        self.background = pygame.Surface(self.rect.size).convert()

        self.make_board()

        background.blit(self.background, (self.topx, self.topy))

    def set_selected_num(self, num):
        self.selected_num = num
        print(self.selected_num)

    def set_board(self, board, sln):
        self.board = board
        self.sln = sln
        self.make_board()

    def draw_cell(self, cell, x, y):
        self.background.blit(cell, (x, y))

    def make_board(self):

        # draw top and bottom borders
        for x in range(self.board_width + 1):
            if x == 0:
                self.draw_cell(self.border_images[2], self.cell_side * x, 0)
                self.draw_cell(self.border_images[5],
                               self.cell_side * x, self.cell_side * self.board_width + self.border_height)
            elif x == self.board_width:
                self.draw_cell(self.border_images[1], self.cell_side * x, 0)
                self.draw_cell(self.border_images[4],
                               self.cell_side * x, self.cell_side * self.board_width + self.border_height)
            else:
                self.draw_cell(self.border_images[0], self.cell_side * x, 0)
                self.draw_cell(self.border_images[3],
                               self.cell_side * x, self.cell_side * self.board_width + self.border_height)

        # draw left / right borders
        for y in range(self.board_width):
            # left borders (horizontal borders are only 25 px, so we need to draw twice)
            self.draw_cell(
                self.border_images[7], 0, self.border_height + self.cell_side * y)
            self.draw_cell(
                self.border_images[7], 0, (self.border_height + self.cell_side * y) + self.border_height)

            # right borders
            self.draw_cell(self.border_images[7],
                           self.cell_side * self.board_width + self.border_height,
                           self.border_height + self.cell_side * y)
            self.draw_cell(self.border_images[7],
                           self.cell_side * self.board_width + self.border_height,
                           (self.border_height + self.cell_side * y) + self.border_height)

        for x in range(len(self.board)):
            for y in range(len(self.board[x])):
                Cell(self, self.cell_side, x, y,
                     self.border_height, self.board[x][y])
