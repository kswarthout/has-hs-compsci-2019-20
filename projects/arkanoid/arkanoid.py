import pygame
from pygame.locals import *
from sprites import Spritesheet
from arena import Arena
from paddle import Paddle
from ball import Ball
from brick import Brick
from status import Status
from score import Score

SCREENRECT = Rect(0, 0, 640, 480)


def score_image(spritesheet, screen, arena):
    score_image = spritesheet.imgat((0, 440, 103, 17), -1)
    background = pygame.Surface((100, 34)).convert()
    background.blit(score_image, (0, 6))
    screen.blit(background, (int(arena.rect.right +
                                 arena.tileside), int(arena.topy + 20)))


def paddle_image(spritesheet):
    '''Loads paddle image'''
    paddle = pygame.Surface((55, 11)).convert()
    # Left Half of Paddle
    paddle.blit(spritesheet.imgat((261, 143, 27, 11)), (0, 0))
    # Right Half of Paddle
    paddle.blit(spritesheet.imgat((289, 143, 28, 11)), (27, 0))
    paddle.set_colorkey(paddle.get_at((0, 0)), RLEACCEL)
    return paddle


def arena_h_borders(spritesheet):
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


def main():
    pygame.init()

    # set the display mode
    pygame.display.set_caption('Arkanoid')
    screen = pygame.display.set_mode(SCREENRECT.size)

    # load images, assign to sprite classes
    spritesheet = Spritesheet('arinoid_master.bmp')

    # Status.score_image = spritesheet.imgat((0, 440, 103, 17), -1)

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
                                        (193, 225, 31, 31)]) + arena_h_borders(spritesheet)

    # yellow - 1, green - 2, red - 3, dark orange - 4,
    # purple - 5, orange - 6, light blue - 7, dark purple - 8
    # silver - 9, dark gray - 10
    Brick.images = spritesheet.imgsat([(225, 193, 31, 16),
                                       (225, 225, 31, 16),
                                       (225, 257, 31, 16),
                                       (225, 289, 31, 16),
                                       (257, 193, 31, 16),
                                       (257, 225, 31, 16),
                                       (257, 257, 31, 16),
                                       (257, 289, 31, 16),
                                       (129, 1, 31, 16),
                                       (97, 1, 31, 16)])

    levels = [[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # level 1
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
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
              [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # level 2
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2],
               [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
              [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # level 3
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 8, 1, 1, 8, 0, 0, 0, 0],
               [0, 0, 0, 8, 1, 1, 1, 1, 8, 0, 0, 0],
               [0, 0, 8, 1, 1, 8, 8, 1, 1, 8, 0, 0],
               [0, 0, 8, 1, 1, 8, 8, 1, 1, 8, 0, 0],
               [0, 0, 0, 8, 1, 1, 1, 1, 8, 0, 0, 0],
               [0, 0, 0, 0, 8, 1, 1, 8, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 8, 8, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 5, 5, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
              [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # level 4
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 3, 3, 9, 3, 3, 9, 3, 3, 9, 3, 0],
               [0, 7, 9, 7, 7, 9, 7, 7, 9, 7, 7, 0],
               [0, 3, 3, 9, 3, 3, 9, 3, 3, 9, 3, 0],
               [0, 7, 9, 7, 7, 9, 7, 7, 9, 7, 7, 0],
               [0, 3, 3, 9, 3, 3, 9, 3, 3, 9, 3, 0],
               [0, 7, 9, 7, 7, 9, 7, 7, 9, 7, 7, 0],
               [0, 3, 3, 9, 3, 3, 9, 3, 3, 9, 3, 0],
               [0, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 0],
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
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
              [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # level 5
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8, 8],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [5, 5, 5, 5, 0, 10, 10, 10, 0, 0, 8, 8],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [2, 2, 2, 2, 2, 2, 10, 2, 2, 2, 2, 2],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [10, 3, 3, 0, 0, 0, 10, 0, 0, 3, 3, 10],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [3, 3, 3, 3, 3, 3, 10, 3, 3, 3, 3, 3],
               [0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0],
               [10, 0, 0, 7, 7, 7, 10, 7, 7, 0, 0, 10],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [7, 7, 7, 7, 7, 7, 10, 7, 7, 7, 7, 7],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [9, 9, 0, 0, 0, 10, 10, 10, 0, 0, 9, 9],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],
              [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],  # level 6 test
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 10, 0, 0, 0, 0, 0],
               [2, 0, 0, 0, 0, 10, 10, 10, 0, 0, 0, 2],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]]

    Paddle.image = paddle_image(spritesheet)
    Ball.image = spritesheet.imgat((428, 300, 11, 11), -1)

    # create the background
    arena = Arena(SCREENRECT, levels)
    # screen.blit(arena.background, (0, 0))  # Attach arena bg to screen
    # pygame.display.update()  # update screen

    score_image(spritesheet, screen, arena)

    # # initialize game groups
    balls = pygame.sprite.Group()
    bricks = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    # # keep track of time
    clock = pygame.time.Clock()

    # assign default groups to each sprite class
    Paddle.containers = all
    Ball.containers = all, balls
    Brick.containers = all, bricks
    Score.containers = all

    # initialize our starting sprites
    paddle = Paddle(arena)
    score = Score(arena)
    arena.makelevel(1)
    screen.blit(arena.background, (0, 0))  # Attach arena bg to screen
    pygame.display.update()  # update screen

    # game loop
    while 1:

        # get input
        for event in pygame.event.get():
            if event.type == QUIT \
                    or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

        # update score
        score.update_score()

        # check for win
        if arena.level_cleared:
            print('won')

        # clear sprites
        all.clear(screen, arena.background)

        # update sprites
        all.update()
        if not balls:
            Ball(arena, paddle, bricks)

        # redraw sprites
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # maintain frame rate
        clock.tick(30)


if __name__ == '__main__':
    main()
