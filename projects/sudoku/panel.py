import pygame
from pygame.locals import *


class Panel:

    selected_num = 0

    def __init__(self, board, background):
        bg_rect = background.get_rect()
        left = board.rect.width
        top = board.topx
        width = bg_rect.width - left - top
        height = bg_rect.height - top * 2

        self.board = board

        self.rect = Rect(left, top, width, height)
        self.background = pygame.Surface(self.rect.size).convert()
        background.blit(self.background, (left, top))

        self.start_grid = [[0 for i in range(9)] for j in range(9)]
        self.sln_grid = [[0 for i in range(9)] for j in range(9)]

    def set_game(self, start_grid, sln_grid):
        self.start_grid = start_grid
        self.sln_grid = sln_grid
        self.board.set_board(self.start_grid, self.sln_grid)

    def select_num(self, num):
        self.board.set_selected_num(num)
