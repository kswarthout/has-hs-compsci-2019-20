import pygame
import requests
from button_class import Button
from settings import *
import json


class NewGameButton(Button):

    # Stores default game encodings to fall back to
    # if server fails to return a new game
    default_game_start = [[0, 9, 0, 0, 0, 0, 3, 0, 1],
                          [0, 0, 0, 0, 0, 0, 0, 0, 6],
                          [0, 0, 0, 0, 0, 6, 0, 0, 0],
                          [9, 8, 0, 0, 0, 0, 2, 0, 3],
                          [0, 6, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 7, 0, 6, 0, 0],
                          [8, 7, 0, 0, 0, 2, 0, 0, 0],
                          [0, 0, 9, 0, 0, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0, 0, 0, 0, 0]]

    default_game_sln = [[6, 9, 8, 7, 5, 4, 3, 2, 1],
                        [7, 5, 4, 3, 2, 1, 9, 8, 6],
                        [3, 2, 1, 9, 8, 6, 7, 5, 4],
                        [9, 8, 7, 6, 4, 5, 2, 1, 3],
                        [5, 6, 3, 2, 1, 9, 8, 4, 7],
                        [4, 1, 2, 8, 7, 3, 6, 9, 5],
                        [8, 7, 5, 4, 6, 2, 1, 3, 9],
                        [2, 4, 9, 1, 3, 7, 5, 6, 8],
                        [1, 3, 6, 5, 9, 8, 4, 7, 2]]

    # def __init__(self, panel, msg, w, h, color, alt_color, text_color):
    #     Button.__init__(self, msg, w, h, color, alt_color, text_color)
    #     self.panel = panel
    #     self.rect.center = (panel.rect.center[0],
    #                         panel.rect.top + self.rect.height)
    def __init__(self, x, y, w, h, text=None, color=DARK_GRAY, highlight_color=LIGHT_GRAY, function=None, params=None):
        Button.__init__(self, x, y, w, h, text, color,
                        highlight_color, self.action, params)
        self.new_grid_loaded = False
        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.grid_finished = [[0 for i in range(9)] for j in range(9)]

    def action(self):
        try:
            r = requests.get('http://localhost:8080/puzzle')
        except (requests.exceptions.ConnectionError, requests.exceptions.Timeout) as e:
            # Server cannot be reached
            self.set_game(self.default_game_start, self.default_game_sln)
        except requests.exceptions.HTTPError:
            # 4xx, 5xx errors
            self.set_game(self.default_game_start, self.default_game_sln)
        except requests.exceptions.RequestException as e:
            # Bad request
            self.set_game(self.default_game_start, self.default_game_sln)
        else:
            # Successful request (status 200)
            if r:
                resp = json.loads(r.content)
                start = self.parse_encoding(resp['start'])
                sln = self.parse_encoding(resp['sln'])
                self.set_game(start, sln)

    def set_game(self, start, sln):
        # self.panel.set_game(start, sln)
        self.grid = start
        self.grid_finished = sln
        self.new_grid_loaded = True

    def parse_encoding(self, encoding):
        board = [[0 for i in range(9)] for j in range(9)]
        start = [char for char in encoding]
        count = 0
        for i in range(9):
            for j in range(9):
                if start[count] == '.':
                    board[i][j] = 0
                else:
                    board[i][j] = int(start[count])
                count += 1
        return board
