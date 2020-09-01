#! /usr/bin/env python

# scriptedfun.com Arinoid
# http://www.scriptedfun.com/
# June 1, 2006
# MIT License

# arinoid_master.bmp
# taken from the Spritelib by Ari Feldman
# http://www.flyingyogi.com/fun/spritelib.html
# Common Public License

import math
import os
import pygame
import random
from pygame.locals import *

# game constants
SCREENRECT = Rect(0, 0, 640, 480)


def load_sound(filename):
    filename = os.path.join('data', filename)
    return pygame.mixer.Sound(filename)


def imgcolorkey(image, colorkey):
    if colorkey is not None:
        if colorkey is -1:
            colorkey = image.get_at((0, 0))
        image.set_colorkey(colorkey, RLEACCEL)
    return image


def load_image(filename, colorkey=None):
    filename = os.path.join('data', filename)
    image = pygame.image.load(filename).convert()
    return imgcolorkey(image, colorkey)


class SpriteSheet:
    def __init__(self, filename):
        self.sheet = load_image(filename)

    def imgat(self, rect, colorkey=None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        return imgcolorkey(image, colorkey)

    def imgsat(self, rects, colorkey=None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs


def hborders(spritesheet):
    """will redraw horizontal borders to place them at the bottom of the tiles,
    and will make a plain horizontal border without a background,
    which is not present in the original sprite sheet"""
    # plain border - 4, special border - 5, upper left - 6, upper right - 7
    rects = [(449, 35, 31, 9), (129, 289, 31, 13),
             (129, 193, 31, 13), (193, 193, 31, 13)]
    # the plain border had to be extracted
    # two pixels away from the edge to remove the background
    offsets = [2, 0, 0, 0]
    borders = []
    for x in range(len(rects)):
        borders.append(pygame.Surface((31, 31)).convert())
        # draw border at the bottom part of the tile, and add the offset if necessary
        # to ensure that the borders will remain aligned
        # -1 index refers to the most recently appended element in the list
        borders[-1].blit(spritesheet.imgat(rects[x]), (0, 18 + offsets[x]))
    return borders


def paddleimage(spritesheet):
    paddle = pygame.Surface((55, 11)).convert()
    paddle.blit(spritesheet.imgat((261, 143, 27, 11)), (0, 0))    # left half
    paddle.blit(spritesheet.imgat((289, 143, 28, 11)), (27, 0))   # right half
    return imgcolorkey(paddle, -1)


class Arena:
    tileside = 31
    # when drawing tiles, the origin is at (topx, topy),
    # so that a filled tile map will be centered on the screen
    # (since 640 x 480 is not divisible by 31 x 31, so the remainder
    # was distributed over the edges of the screen, centering the resulting image)
    topx = 10
    topy = 7
    # numxtiles, numytiles, and rect refer to the region where the ball is allowed to be in
    numxtiles = 12
    numytiles = 14
    rect = Rect(topx + tileside, topy + tileside,
                tileside*(numxtiles), tileside*(numytiles))

    def __init__(self, levels):
        self.levels = levels
        self.background = pygame.Surface(SCREENRECT.size).convert()
        self.makebg(4)

    def drawtile(self, tile, x, y):
        self.background.blit(
            tile, (self.topx + self.tileside*x, self.topy + self.tileside*y))

    def makebg(self, tilenum):
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
                # draw tiles within the border
                self.drawtile(self.tiles[tilenum], x + 1, y + 1)

    def makelevel(self, levelnum):
        print(self.levels[levelnum])
        for y in range(len(self.levels[levelnum])):
            print(self.levels[levelnum][y])
            for x in range(len(self.levels[levelnum][y])):
                color = self.levels[levelnum][y][x] - 1
                print(color)
                if color > -1:
                    # print('x: {:d}'.format(x))
                    # print('y: {:d}'.format(y))
                    # print('color: {:d}'.format(color))
                    Brick(self, x, y, color)

# each type of game object gets an init and an
# update function. the update function is called
# once per frame, and it is when each object should
# change its current position and state


class Paddle(pygame.sprite.Sprite):
    def __init__(self, arena):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.arena = arena
        self.rect.bottom = arena.rect.bottom - arena.tileside

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        if not self.arena.rect.contains(self.rect):
            if self.rect.left < self.arena.rect.left:
                self.rect.left = self.arena.rect.left
            elif self.rect.right > self.arena.rect.right:
                self.rect.right = self.arena.rect.right


class Ball(pygame.sprite.Sprite):
    # the speed should be less than
    # the smallest dimension
    # used in the game
    # to prevent teleporting
    speed = 5
    anglel = 45
    angleh = 135

    def __init__(self, arena, paddle, bricks):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.arena = arena
        self.paddle = paddle
        self.update = self.start
        self.bricks = bricks

    def start(self):
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top
        if pygame.mouse.get_pressed()[0] == 1:
            self.fpx = self.rect.centerx
            self.fpy = self.rect.centery
            self.fpdx = 0
            self.fpdy = 1
            self.update = self.move

    def setfp(self):
        """use whenever usual integer rect values are adjusted"""
        self.fpx = self.rect.centerx
        self.fpy = self.rect.centery

    def setint(self):
        """use whenever floating point rect values are adjusted"""
        self.rect.centerx = self.fpx
        self.rect.centery = self.fpy

    def move(self):
        # bounce from paddle
        if self.rect.colliderect(self.paddle.rect) and self.fpdy > 0:
            ballpos = self.rect.width + self.rect.left - self.paddle.rect.left - 1
            ballmax = self.rect.width + self.paddle.rect.width - 2
            factor = float(ballpos)/ballmax
            angle = math.radians(self.angleh - factor *
                                 (self.angleh - self.anglel))
            self.fpdx = self.speed*math.cos(angle)
            self.fpdy = -self.speed*math.sin(angle)

        # usual movement
        self.fpx = self.fpx + self.fpdx
        self.fpy = self.fpy + self.fpdy
        self.setint()

        # keep inside arena
        if self.rect.left < self.arena.rect.left:
            self.rect.left = self.arena.rect.left
            self.setfp()
            self.fpdx = -self.fpdx
        if self.rect.right > self.arena.rect.right:
            self.rect.right = self.arena.rect.right
            self.setfp()
            self.fpdx = -self.fpdx
        if self.rect.top < self.arena.rect.top:
            self.rect.top = self.arena.rect.top
            self.setfp()
            self.fpdy = -self.fpdy
        if self.rect.top > self.arena.rect.bottom:
            self.update = self.start

        # destroy bricks
        brickscollided = pygame.sprite.spritecollide(self, self.bricks, False)
        if brickscollided:
            oldrect = self.rect
            left = right = up = down = 0
            for brick in brickscollided:
                # [] - brick, () - ball

                # ([)]
                if oldrect.left < brick.rect.left < oldrect.right < brick.rect.right:
                    self.rect.right = brick.rect.left
                    self.setint()
                    left = -1

                # [(])
                if brick.rect.left < oldrect.left < brick.rect.right < oldrect.right:
                    self.rect.left = brick.rect.right
                    self.setint()
                    right = 1

                # top ([)] bottom
                if oldrect.top < brick.rect.top < oldrect.bottom < brick.rect.bottom:
                    self.rect.bottom = brick.rect.top
                    self.setint()
                    up = -1

                # top [(]) bottom
                if brick.rect.top < oldrect.top < brick.rect.bottom < oldrect.bottom:
                    self.rect.top = brick.rect.bottom
                    self.setint()
                    down = 1

                brick.kill()

            # if the ball is asked to go both ways, then do not change direction
            if left + right != 0:
                self.fpdx = (left + right)*abs(self.fpdx)
            if up + down != 0:
                self.fpdy = (up + down)*abs(self.fpdy)


class Brick(pygame.sprite.Sprite):
    def __init__(self, arena, x, y, color):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[color]
        self.rect = self.image.get_rect()
        self.rect.left = arena.rect.left + x*self.rect.width
        self.rect.top = arena.rect.top + y*self.rect.height


def main():
    pygame.init()

    # set the display mode
    winstyle = 0  # | FULLSCREEN
    bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
    screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

    # load images, assign to sprite classes
    # (do this before the classes are used, after screen setup)
    spritesheet = SpriteSheet('arinoid_master.bmp')

    Arena.tiles = spritesheet.imgsat([(129, 321, 31, 31),   # purple - 0
                                      (161, 321, 31, 31),   # dark blue - 1
                                      (129, 353, 31, 31),   # red - 2
                                      (161, 353, 31, 31),   # green - 3
                                      (129, 385, 31, 31)])  # blue - 4

    # left border - 0, right border - 1,
    # special left border - 2, special right border - 3
    Arena.borders = spritesheet.imgsat([(129, 257, 31, 31),
                                        (193, 257, 31, 31),
                                        (129, 225, 31, 31),
                                        (193, 225, 31, 31)]) + hborders(spritesheet)

    Paddle.image = paddleimage(spritesheet)
    Ball.image = spritesheet.imgat((428, 300, 11, 11), -1)

    # yellow - 1, green - 2, red - 3, dark orange - 4,
    # purple - 5, orange - 6, light blue - 7, dark blue - 8
    Brick.images = spritesheet.imgsat([(225, 193, 31, 16),
                                       (225, 225, 31, 16),
                                       (225, 257, 31, 16),
                                       (225, 289, 31, 16),
                                       (257, 193, 31, 16),
                                       (257, 225, 31, 16),
                                       (257, 257, 31, 16),
                                       (257, 289, 31, 16)])

    levels = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
               [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0],
               [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
               [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0],
               [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
               [0, 7, 7, 7, 7, 7, 7, 7, 7, 7, 7, 0],
               [0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

    # decorate the game window
    pygame.display.set_caption('scriptedfun.com Arinoid')

    # create the background
    arena = Arena(levels)
    screen.blit(arena.background, (0, 0))
    pygame.display.flip()

    # initialize game groups
    balls = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    # assign default groups to each sprite class
    Paddle.containers = all
    Ball.containers = all, balls
    Brick.containers = all, bricks

    clock = pygame.time.Clock()

    # initialize our starting sprites
    paddle = Paddle(arena)
    Ball(arena, paddle, bricks)
    arena.makelevel(0)

    while 1:

        # get input
        for event in pygame.event.get():
            if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

        # clear/erase the last drawn sprites
        all.clear(screen, arena.background)

        # update all the sprites
        all.update()

        # draw the scene
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # cap the framerate
        clock.tick(60)


if __name__ == '__main__':
    main()
