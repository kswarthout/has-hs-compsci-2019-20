import pygame
from pygame.locals import *
from spritesheet import Spritesheet
from victory import Victory
from board import Board
from panel import Panel
from cell import Cell
from button import Button
from new_game import NewGame
from nums_grid import NumsGrid

SCREENRECT = Rect(0, 0, 840, 550)
CELL_SIDE = 50
BOARD_WIDTH = 9
BORDER_HEIGHT = 25


def main():
    pygame.init()

    # set the display mode
    pygame.display.set_caption('Arkanoid')
    screen = pygame.display.set_mode(SCREENRECT.size)
    background = pygame.Surface(SCREENRECT.size).convert()

    # load images, assign to sprite classes
    spritesheet = Spritesheet('sudoku_spritesheet.png')
    border_sprites = Spritesheet('borders.png')
    victory_spritesheet = Spritesheet('sudoku_winner_spritesheet.png')

    # assign images to sprites
    Board.images = spritesheet.imgsat([(32, 0, 32, 32), (0, 32, 32, 32)])
    Board.border_images = border_sprites.imgsat(Board.border_img_locs)
    Victory.images = victory_spritesheet.imgsat(Victory.img_rects)

    # create sprite groups
    cells = pygame.sprite.Group()
    all = pygame.sprite.RenderUpdates()

    # assign sprite groups
    Cell.containers = cells, all
    Victory.containers = all
    Button.containers = all

    # create the background
    board = Board(background, CELL_SIDE, BOARD_WIDTH, BORDER_HEIGHT)
    panel = Panel(board, background)
    new_game = NewGame(panel, 'New Game', 100, 50,
                       (255, 0, 0), (0, 255, 0), (255, 255, 255))
    nums_grid = NumsGrid(panel)

    # create sprites
    # victory = Victory(panel)

    # transfer bg
    screen.blit(background, (0, 0))
    pygame.display.update()

    # keep track of time
    clock = pygame.time.Clock()

    # game loop
    while True:

        # get input
        for event in pygame.event.get():
            if event.type == QUIT \
                    or (event.type == KEYDOWN and event.key == K_ESCAPE):
                return

        # clear sprites
        all.clear(screen, board.background)

        # update sprites
        all.update()

        # redraw sprites
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # maintain frame rate
        clock.tick(30)


if __name__ == '__main__':
    main()
