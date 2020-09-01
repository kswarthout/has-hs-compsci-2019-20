import pygame
import sys
from settings import *
from button_class import Button
from grid_1 import Grid
from audio import Audio
from pygame import mixer
import os
import requests
import json


class App:
    def __init__(self):
        # init window
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

        # init inputs
        self.mouse_pos = None

        self.playing_buttons = []
        self.status = ''

        self.audio = Audio()
        self.grid = Grid(self.audio)

        self.audio.background_music()

        self.font = pygame.font.SysFont('arial', int(cell_size / 2))
        self.load()

    def run(self):
        while self.running:
            self.events()
            self.update()
            self.draw()
        pygame.quit()
        sys.exit()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # USER CLICKS
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.grid.get_selected()

    def update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.grid.update(self.mouse_pos)

    def draw(self):
        # fill window bg
        self.window.fill(BG_COLOR)

        # draw sudoku grid lines
        self.grid.draw(self.window)

        pygame.display.update()

    def load(self):
        self.load_buttons()
        self.reload_grid()

    def load_buttons(self):
        ngw = 150
        ngx = panel_pos[0] + ((panel_size[0] - ngw) / 2)
        self.playing_buttons.append(Button(
            ngx, panel_pos[1] + 20, ngw, 50, 'New Game', NEW_GAME_BUTTON_COLOR, NEW_GAME_BUTTON_COLOR_ALT, self.action))

    def reload_grid(self):
        for yidx, row in enumerate(self.grid.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.grid.locked_cells.append([xidx, yidx])

    def set_game(self, start, sln):
        self.status = ''
        self.grid = start
        self.grid_finished = sln
        self.reload_grid()

    def action(self):
        try:
            self.status = 'Loading...'
            self.draw()
            r = requests.get(
                'https://desolate-shelf-37913.herokuapp.com/puzzle')
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            # Server cannot be reached
            self.set_game(test_board_2, test_board_2_finished)
        except requests.exceptions.HTTPError:
            # 4xx, 5xx errors
            self.set_game(test_board_2, test_board_2_finished)
        except requests.exceptions.RequestException as e:
            # Bad request
            self.set_game(test_board_2, test_board_2_finished)
        else:
            # Successful request (status 200)
            if r:
                resp = json.loads(r.content)
                start = self.grid.parse_encoding(resp['start'])
                sln = self.parse_encoding(resp['sln'])
                self.set_game(start, sln)
