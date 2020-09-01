import pygame
from button import Button


class NumButton(Button):

    num = 0

    def __init__(self, panel, nums_grid, msg, w, h, color, alt_color, text_color, row, col):
        Button.__init__(self, msg, w, h, color, alt_color, text_color)
        self.panel = panel
        self.nums_grid = nums_grid
        left_padding = self.panel.rect.left + (self.panel.rect.width - 250) / 2
        # self.rect.left = self.panel.rect.left + col * w
        self.rect.left = left_padding + col * w
        self.rect.top = self.panel.rect.bottom - 150 + row * h

        self.num = int(msg)
        # self.action = action

    def action(self):
        # print(self.num)
        self.nums_grid.select_num(self.num)
