

import math
import os
import pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)


def paddleimage(spritesheet):
    paddle = pygame.Surface((55, 11)).convert()
    # left half
    paddle.blit(spritesheet.imgat((261, 143, 27, 11)), (0, 0))
    # right half
    paddle.blit(spritesheet.imgat((289, 143, 28, 11)), (27, 0))
    paddle.set_colorkey(paddle.get_at((0, 0)), RLEACCEL)
    return paddle


class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(
            os.path.join('data', filename)).convert()

    def imgat(self, rect, colorkey=None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0, 0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0, 0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image

    def imgsat(self, rects, colorkey=None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs


class Arena:
    tileside = 31
    numxtiles = 12
    numytiles = 14
    topx = (SCREENRECT.width - SCREENRECT.width/tileside*tileside)/2
    topy = (SCREENRECT.height - SCREENRECT.height/tileside*tileside)/2
    rect = Rect(topx + tileside, topy + tileside,
                tileside*numxtiles, tileside*numytiles)

    def __init__(self):
        self.background = pygame.Surface(SCREENRECT.size).convert()

    def drawtile(self, tile, x, y):
        self.background.blit(tile, (self.topx + self.tileside*x,
                                    self.topy + self.tileside*y))

    def makebg(self, tilenum):
        for x in range(self.numxtiles):
            for y in range(self.numytiles):
                self.drawtile(self.tiles[tilenum], x + 1, y + 1)


class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.arena.rect.bottom - self.arena.tileside

    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(self.arena.rect)


class Ball(pygame.sprite.Sprite):
    '''Represents an Arkanoid ball
    - we want the ball to have two states: 
        - when the game starts, we want the ball to remain on top of the paddle
        - when the user clicks the mouse, the ball will be released from the paddle bouncing around the arena
        - this is why we write two seperate update functions corresponding to the bakk state
    - setfp, setint: in order to make the ball movement smoother, it would be better to use non-integer coordinates, but
      by default this is not allowed. To overcome this we will write to methods to convert between integer and floating-point values
    - angleleft, angleright: determines the angle the ball will leave the paddle when it hits the edge
    '''

    speed = 5
    angleleft = 45
    angleright = 135

    def __init__(self):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.rect = self.image.get_rect()
        self.update = self.start

    def start(self):
        '''When the ball is introduced, places it on top of the paddle'''
        self.rect.centerx = self.paddle.rect.centerx
        self.rect.bottom = self.paddle.rect.top

        # check for mouse clicks from start state to allow update to switch to move state
        if pygame.mouse.get_pressed()[0] == 1:
            self.dx = 0
            self.dy = 1
            self.update = self.move

    def move(self):
        '''Updates the display when ball is not on paddle'''
        if self.rect.colliderect(self.paddle.rect) and self.dy > 0:
            # ballpos represents the ball's x position relative to paddle
            # ballmax is the max pos of ball on the paddle
            # factor is a ratio that represents where the ball is on the paddle
            ballpos = self.rect.width + self.rect.left - self.paddle.rect.left - 1
            ballmax = self.rect.width + self.paddle.rect.width - 2
            factor = float(ballpos) / ballmax
            angle = math.radians(self.angleright - factor *
                                 (self.angleright - self.angleleft))
            self.dx = self.speed*math.cos(angle)
            self.dy = -self.speed*math.sin(angle)

        self.rect.centerx = int(self.rect.centerx + self.dx)
        self.rect.centery = int(self.rect.centery + self.dy)

        # we have to check for the case when the ball hits the arena walls
        if not self.arena.rect.contains(self.rect):
            # check if the ball went out of the bottom part of the arena (player did not catch the ball)
            if self.rect.bottom > self.arena.rect.bottom:
                self.kill()
            else:
                if self.rect.left < self.arena.rect.left:
                    self.rect.left = self.arena.rect.left
                    self.dx = -self.dx
                if self.rect.right > self.arena.rect.right:
                    self.rect.right = self.arena.rect.right
                    self.dx = -self.dx
                if self.rect.top < self.arena.rect.top:
                    self.rect.top = self.arena.rect.top
                    self.dy = -self.dy
                if self.rect.top > self.arena.rect.bottom:
                    self.update = self.start

                # Since the ball went out of bounds, we want to bring it back in the arena
                self.rect.clamp_ip(self.arena.rect)


def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREENRECT.size)

    spritesheet = Spritesheet('arinoid_master.bmp')

    Arena.tiles = spritesheet.imgsat([(129, 321, 31, 31),   # purple - 0
                                      (161, 321, 31, 31),   # dark blue - 1
                                      (129, 353, 31, 31),   # red - 2
                                      (161, 353, 31, 31),   # green - 3
                                      (129, 385, 31, 31)])  # blue - 4

    Paddle.image = paddleimage(spritesheet)
    # load the ball image from the sprite sheet and make the ball transparent
    # this will make the ball circular instead of rectangular
    Ball.image = spritesheet.imgat((428, 300, 11, 11), -1)

    # make background
    arena = Arena()
    arena.makebg(0)  # you may change the background color here
    screen.blit(arena.background, (0, 0))
    pygame.display.update()

    Paddle.arena = arena
    # make the playing field visible to the ball
    Ball.arena = arena

    # keep track of sprites
    # it is useful to assign all the balls to a group so they can easily be accessed at the same time
    balls = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    Paddle.containers = all
    Ball.containers = all, balls

    # keep track of time
    clock = pygame.time.Clock()

    paddle = Paddle()

    # since each ball will have to interact with the paddle, let's make paddle visible to the Ball class
    Ball.paddle = paddle

    # game loop
    while 1:

        # get input
        for event in pygame.event.get():
            if event.type == QUIT   \
               or (event.type == KEYDOWN and
                   event.key == K_ESCAPE):
                return

        # clear sprites
        all.clear(screen, arena.background)

        # update sprites
        all.update()
        # check if there are no more live balls, and add a new one to the arena
        if not balls:
            Ball()

        # redraw sprites
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # maintain frame rate
        clock.tick(60)


if __name__ == '__main__':
    main()
