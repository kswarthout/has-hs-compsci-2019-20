import pygame
from pygame.locals import *


class Cell(pygame.sprite.Sprite):

    BORDER = (218, 218, 218)
    HIGHLIGHT = (0, 195, 216)
    WHITE = (255, 255, 255)
    BLUE = (9, 4, 161)
    BRIGHT_BLUE = (75, 126, 226)
    BLACK = (0, 0, 0)
    BG_RECT = Rect(1, 1, 48, 48)

    def __init__(self, board, cell_side, x, y, border_height, num=0):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.board = board
        self.cell_side = cell_side
        self.border_height = border_height
        self.image = pygame.Surface((self.cell_side, self.cell_side))
        self.image.fill(self.BORDER)
        pygame.draw.rect(self.image, self.WHITE, self.BG_RECT)
        self.rect = self.image.get_rect()
        self.rect.left = board.topx + self.cell_side * x + self.border_height
        self.rect.top = board.topy + self.cell_side * y + self.border_height

        # cell selected
        self.selected = False

        # cell number
        self.x = x
        self.y = y
        self.num = num
        self.font = pygame.font.SysFont("bahnschrift", 30)
        if self.num != 0:
            self.num_set = True
        else:
            self.num_set = False

    def update(self):
        # decide font color
        color = self.BLACK
        if self.num != 0 and self.num_set:
            color = self.BLUE

        # detect mouse actions
        mx, my = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if mx > self.rect.left and mx < self.rect.left + self.cell_side \
                and my > self.rect.top and my < self.rect.top + self.cell_side \
            and not self.num_set:

            if click[0] == True:
                self.selected = True
                if self.board.selected_num != 0:
                    self.num = self.board.selected_num
                    if self.is_num_valid():
                        color = self.BLUE
                    else:
                        color = (255, 0, 0)

            self.image.fill(self.HIGHLIGHT)
            color = self.BRIGHT_BLUE
        else:
            if click[0] == True:
                self.selected = False

            if self.selected:
                self.image.fill(self.HIGHLIGHT)
                color = self.BRIGHT_BLUE
            else:
                self.image.fill(self.BORDER)
        pygame.draw.rect(self.image, self.WHITE, self.BG_RECT)
        self.draw_num(color)

    def draw_num(self, color):

        if self.num != 0:
            text = self.font.render(str(self.num), True, color)
            text_rect = text.get_rect()
            text_rect.center = (self.image.get_width() / 2,
                                self.image.get_height() / 2)
            self.image.blit(text, text_rect)

    def set_num(self, num):
        self.num = num

    def is_num_valid(self):
        return self.num != self.board.sln[self.x][self.y]
