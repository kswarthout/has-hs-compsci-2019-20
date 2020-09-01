import pygame
from settings import *


class Button:
    def __init__(self, x, y, w, h, text=None, color=DARK_GRAY, highlight_color=LIGHT_GRAY, function=None, params=None):
        self.image = pygame.Surface((w, h))
        self.pos = (x, y)
        self.rect = self.image.get_rect()
        self.rect.topleft = self.pos
        self.text = text
        self.color = color
        self.highlight_color = highlight_color
        self.function = function
        self.params = params
        self.highlighted = False
        self.font = pygame.font.SysFont('arial', int(h / 2))

    def update(self, mouse, click):
        if self.rect.collidepoint(mouse):
            self.highlighted = True

            if click[0] == 1 and self.function != None:
                self.function()
        else:
            self.highlighted = False

    def draw(self, window):
        # fill button color
        self.image.fill(
            self.highlight_color if self.highlighted else self.color)
        window.blit(self.image, self.pos)

        # draw font
        font = self.font.render(self.text, False, WHITE)
        font_width = font.get_width()
        font_height = font.get_height()
        pos = [0, 0]
        pos[0] = self.pos[0] + (self.rect.width - font_width) / 2
        pos[1] = self.pos[1] + (self.rect.height - font_height) / 2
        window.blit(font, pos)
