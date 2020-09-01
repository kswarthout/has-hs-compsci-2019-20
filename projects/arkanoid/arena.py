import os
import pygame
from pygame.locals import *
from brick import Brick


class Arena:

    tileside = 31
    # numxtiles, numytiles, and rect refer to the region where the ball is allowed to be in
    numxtiles = 12
    numytiles = 14

    def __init__(self, screenrect, levels):
        '''Draws the background'''
        self.levels = levels
        # print((screenrect.size[0] / 4) * 3)
        # print(screenrect.size)

        # self.background = pygame.Surface(screenrect.size).convert()
        self.topx = (screenrect.width - screenrect.width /
                     self.tileside * self.tileside) / 2
        self.topy = (screenrect.height - screenrect.height /
                     self.tileside * self.tileside) / 2
        self.rect = Rect(self.topx + self.tileside, self.topy + self.tileside,
                         self.tileside * (self.numxtiles), self.tileside * (self.numytiles))

        self.levelnum = 0
        self.score = 0
        # self.score_font = pygame.font.SysFont('bahnschrift', 32)
        # self.show_score()
        self.background = pygame.Surface(
            (self.rect.width + 62, self.rect.height + 62)).convert()
        # print(self.rect.topleft[0])

        # self.makebg(2)  # Pass index for dif tile color

    def drawtile(self, tile, x, y):
        '''Draws a tile to the playing field's background'''
        self.background.blit(tile, (self.topx + self.tileside*x,
                                    self.topy + self.tileside * y))

    # def show_score(self):
    #     # text_surface = pygame.Surface((100, 34)).convert()
    #     # text_surface.fill((0, 0, 0))
    #     # self.background.blit(
    #     #     text_surface, (int(self.rect.right + self.tileside), int(self.topy + 20)))
    #     # pygame.display.update(self.background.get_rect())

    #     # print(self.score)
    #     score = self.score_font.render(str(self.score), True, (255, 255, 255))
    #     self.background.blit(
    #         score, (int(self.rect.right + self.tileside), int(self.topy + 20)))

    def makebg(self, tilenum):
        '''Draws the playing field's background'''

        # numbers refer to border images
        bordertop = [6, 4, 4, 4, 5, 4, 4, 4, 4, 5, 4, 4, 4, 7]
        borderleft = [0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0, 2, 0, 0]
        borderright = [1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1]
        for x in range(len(bordertop)):
            self.drawtile(self.borders[bordertop[x]], x, 0)
        for y in range(len(borderleft)):
            self.drawtile(self.borders[borderleft[y]], 0, 1 + y)
            self.drawtile(self.borders[borderright[y]],
                          self.numxtiles + 1, 1 + y)

        for x in range(self.numxtiles):
            for y in range(self.numytiles):
                self.drawtile(self.tiles[tilenum], x + 1, y + 1)

    def makelevel(self, levelnum):
        self.score = 0
        self.level_cleared = False
        self.levelnum = levelnum
        if levelnum == 0:
            self.makebg(0)
        if levelnum == 1:
            self.makebg(4)
        if levelnum == 2:
            self.makebg(3)
        if levelnum == 3:
            self.makebg(2)
        if levelnum == 4:
            self.makebg(4)
        if levelnum == 5:
            self.makebg(4)
        for y in range(len(self.levels[levelnum])):
            for x in range(len(self.levels[levelnum][y])):
                color = self.levels[levelnum][y][x] - 1
                if color > -1:
                    Brick(self, x, y, color)

    def add_score(self, color):
        # print(color)
        if color == 0:
            self.score += 120
        elif color == 1:
            self.score += 80
        elif color == 2:
            self.score += 90
        elif color == 3:
            self.score += 60
        elif color == 4:
            self.score += 110
        elif color == 5:
            self.score += 50
        elif color == 6:
            self.score += 70
        elif color == 7:
            self.score += 100
        elif color == 8:
            self.score += ((self.levelnum + 1) * 50)
        # print(self.score)
        # self.show_score()
