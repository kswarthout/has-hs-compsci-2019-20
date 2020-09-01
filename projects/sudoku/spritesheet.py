import os
import pygame
from pygame.locals import *


class Spritesheet:

    def __init__(self, filename):
        self.sheet = pygame.image.load(
            os.path.join('data', filename)).convert()

    def imgat(self, rect, colorkey=None):
        '''Allows us to extract subimages from the spritesheet
        - rect: describes the region we want to extract
        - colorkey: allows us to make the background transparent
        '''
        rect = Rect(rect)

        # create a surface so we can place the image where we want
        image = pygame.Surface(rect.size).convert()

        # transfer the subimage from the sprite sheet onto the surface
        image.blit(self.sheet, (0, 0), rect)

        # make the color transparent if no colorkey is passed
        if colorkey is not None:
            if colorkey == -1:
                colorkey = image.get_at((0, 0))

            # use the flag RLEACCEL to make using the resulting image fast
            image.set_colorkey(colorkey, RLEACCEL)

        return image

    def imgsat(self, rects, colorkey=None):
        '''Loads all images from the spritesheet and 
        store them to a list for faster retrieval'''
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs
