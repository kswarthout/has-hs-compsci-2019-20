import pygame
import sys
from settings import *
from button_class import *
import requests
import json
from victory import VictoryAnimation
from spritesheet import Spritesheet


class App:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.running = True

        victory_spritesheet = Spritesheet('sudoku_winner_spritesheet.png')
        border_sprites = Spritesheet('borders.png')
        VictoryAnimation.images = victory_spritesheet.imgsat(
            VictoryAnimation.img_rects, -1)
        self.border_images = border_sprites.imgsat(border_img_locs, -1)

        self.grid = [[0 for i in range(9)] for j in range(9)]
        self.grid_finished = [[0 for i in range(9)] for j in range(9)]
        # self.grid = test_board_2
        # self.grid_finished = test_board_2_finished

        self.selected = None
        self.mouse_pos = None
        self.mouse_click = None
        self.finished = False
        self.cell_changed = False
        self.show_victory = False
        self.status = ''
        self.incorrect_cells = []
        self.locked_cells = []
        self.state = "playing"
        self.playing_buttons = []
        self.menu_buttons = []
        self.end_buttons = []

        self.victory = VictoryAnimation(victory_pos)

        self.font = pygame.font.SysFont('arial', int(cell_size / 2))
        self.load()

    def run(self):
        while self.running:
            if self.state == "playing":
                self.playing_events()
                self.playing_update()
                self.playing_draw()
        pygame.quit()
        sys.exit()

####### PLAYING STATE FUNCTIONS #########

    def playing_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            # USER CLICKS
            if event.type == pygame.MOUSEBUTTONDOWN:
                selected = self.mouse_on_grid()
                # selected = self.grid_display.mouse_on_grid()
                if selected:
                    self.selected = selected
                    # self.grid_display.selected = selected
                else:
                    print('not on board')
                    self.selected = None
                    # self.grid_display.selected = None

            # USER TYPES A KEY
            if event.type == pygame.KEYDOWN:
                if self.selected != None and self.selected not in self.locked_cells:

                    # Cell changed
                    if self.is_int(event.unicode):
                        row = self.selected[1]
                        col = self.selected[0]
                        self.grid[row][col] = int(event.unicode)
                        self.cell_changed = True
                # print(event.unicode)
            # self.grid = test_board_2_finished

    def playing_update(self):
        self.mouse_pos = pygame.mouse.get_pos()
        self.mouse_click = pygame.mouse.get_pressed()

        for button in self.playing_buttons:
            button.update(self.mouse_pos, self.mouse_click)

        if self.show_victory:
            self.victory.update()

        if self.cell_changed:
            self.incorrect_cells = []
            self.check_all_cells()
            if self.all_cells_done():
                # check if board is correct
                self.check_all_cells()

        if len(self.incorrect_cells) == 0 and self.all_cells_done():
            self.show_victory = True

    def playing_draw(self):
        self.window.fill(BG_COLOR)
        # self.draw_grid_border(self.window)
        self.draw_panel(self.window)
        self.draw_status(self.window)
        for button in self.playing_buttons:
            button.draw(self.window)

        if self.show_victory:
            self.victory.draw(self.window)

        # shade selected
        if self.selected:
            self.draw_selection(self.window, self.selected)

        # shade locked cells
        self.shade_locked_cells(self.window, self.locked_cells)
        self.shade_incorrect_cells(self.window, self.incorrect_cells)

        self.draw_numbers(self.window)
        self.draw_grid(self.window)

        # self.draw_grid(self.window)
        pygame.display.update()

        # stops cell changed from always being true
        self.cell_changed = False


####### BOARD CHECKING FUNCTIONS #########

    def check_all_cells(self):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != self.grid_finished[yidx][xidx]:
                    self.incorrect_cells.append([xidx, yidx])
        # self.check_rows()
        # self.check_cols()
        # self.check_region()

    def all_cells_done(self):
        for row in self.grid:
            for num in row:
                if num == 0:
                    return False
        return True

    def check_rows(self):
        for yidx, row in enumerate(self.grid):
            possibles = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            for xidx in range(9):
                if self.grid[yidx][xidx] in possibles:
                    possibles.remove(self.grid[yidx][xidx])
                else:
                    if [xidx, yidx] not in self.locked_cells:
                        self.incorrect_cells.append([xidx, yidx])
            # print(self.incorrect_cells)

    def check_cols(self):
        pass

    def check_region(self):
        pass

    def action(self):
        try:
            self.status = 'Loading...'
            self.playing_draw()
            r = requests.get('http://localhost:8080/puzzle')
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
                start = self.parse_encoding(resp['start'])
                sln = self.parse_encoding(resp['sln'])
                self.set_game(start, sln)

    def set_game(self, start, sln):
        self.status = ''
        self.grid = start
        self.grid_finished = sln
        self.reload_grid()

####### HELPER FUNCTIONS #########

    def is_int(self, string):
        try:
            int(string)
        except:
            return False
        return True

    def shade_incorrect_cells(self, window, incorrect):
        for cell in incorrect:
            if self.grid[cell[1]][cell[0]] != 0:
                x = cell[0] * cell_size + grid_pos[0]
                y = cell[1]*cell_size + grid_pos[1]
                pygame.draw.rect(window, INCORRECT_CELL_COLOR,
                                 (x, y, cell_size, cell_size))

    def shade_locked_cells(self, window, locked):
        for cell in locked:
            x = cell[0] * cell_size + grid_pos[0]
            y = cell[1]*cell_size + grid_pos[1]
            pygame.draw.rect(window, LOCKED_CELL_COLOR,
                             (x, y, cell_size, cell_size))

    def load(self):
        self.load_buttons()
        self.reload_grid()

    def reload_grid(self):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    self.locked_cells.append([xidx, yidx])

    def load_buttons(self):
        ngw = 150
        ngx = panel_pos[0] + ((panel_size[0] - ngw) / 2)
        self.playing_buttons.append(Button(
            ngx, panel_pos[1] + 20, ngw, 50, 'New Game', NEW_GAME_BUTTON_COLOR, NEW_GAME_BUTTON_COLOR_ALT, self.action))

    def draw_status(self, window):
        # pygame.draw.rect(window, STATUS_BAR_COLOR,
        #                  (status_pos[0], status_pos[1], status_size[0], status_size[1]))
        pos = [status_pos[0], status_pos[1]]
        font = pygame.font.SysFont('arial', int(status_size[1] / 2))
        self.text_to_screen(window, self.status, pos,
                            DARK_BLUE, font, status_size)

    def draw_selection(self, window, pos):
        x = pos[0] * cell_size + grid_pos[0]
        y = pos[1] * cell_size + grid_pos[1]
        pygame.draw.rect(
            window, LIGHT_BLUE, (x, y, cell_size, cell_size))

    def draw_numbers(self, window):
        for yidx, row in enumerate(self.grid):
            for xidx, num in enumerate(row):
                if num != 0:
                    x = xidx * cell_size + grid_pos[0]
                    y = yidx * cell_size + grid_pos[1]
                    pos = [x, y]
                    self.text_to_screen(window, str(num), pos)

    def draw_grid(self, window):
        # self.draw_grid_border(window)
        gx = grid_pos[0]
        gy = grid_pos[1]
        gw = gx + grid_size - cell_size
        gh = gy + grid_size - cell_size
        pygame.draw.rect(window, BLACK, (gx, gy, gw, gh), 2)
        for x in range(9):
            vx = (grid_pos[0] + (x * cell_size), grid_pos[1])
            vy = (grid_pos[0] + (x * cell_size), grid_pos[1] + 450)
            hx = (grid_pos[0], grid_pos[1] + (x * cell_size))
            hy = (grid_pos[0] + 450, grid_pos[1] + (x * cell_size))
            pygame.draw.line(window, BLACK, vx, vy, 2 if x % 3 == 0 else 1)
            pygame.draw.line(window, BLACK, hx, hy, 2 if x % 3 == 0 else 1)

    def draw_grid_border(self, window):
        topy = grid_pos[1] - border_height
        boty = grid_pos[0] + grid_size
        left = grid_pos[0] - border_height
        for x in range(grid_size + 1):
            if x == 0:
                window.blit(self.border_images[2], (left, topy))
                window.blit(
                    self.border_images[5], (grid_pos[0] - border_height, boty))
                # self.draw_cell(self.border_images[2], self.cell_side * x, 0)
                # self.draw_cell(self.border_images[5],
                #                self.cell_side * x, self.cell_side * self.board_width + self.border_height)
            elif x == 9:
                window.blit(self.border_images[1], (left + grid_size, topy))
                window.blit(
                    self.border_images[4], (left + grid_size, boty))
                # self.draw_cell(self.border_images[4],
                #                self.cell_side * x, self.cell_side * self.board_width + self.border_height)
            else:
                window.blit(self.border_images[0],
                            (left + (cell_size * x), topy))
                # self.draw_cell(self.border_images[3],
                #                self.cell_side * x, self.cell_side * self.board_width + self.border_height)

    def draw_panel(self, window):
        pygame.draw.rect(
            window, PANEL_BG, (panel_pos[0], panel_pos[1], panel_size[0], panel_size[1]))

    def mouse_on_grid(self):
        if self.mouse_pos[0] < grid_pos[0] or self.mouse_pos[1] < grid_pos[1]:
            return False
        elif self.mouse_pos[0] > grid_pos[0] + grid_size or self.mouse_pos[1] > grid_pos[1] + grid_size:
            return False
        return ((self.mouse_pos[0] - grid_pos[0]) // cell_size, (self.mouse_pos[1] - grid_pos[1]) // cell_size)

    def text_to_screen(self, window, text, pos, color=BLACK, font=None, size=(cell_size, cell_size)):
        if font == None:
            font = self.font

        # print(text)
        text = font.render(text, False, color)
        text_width = text.get_width()
        text_height = text.get_height()
        pos[0] += (size[0] - text_width) / 2
        pos[1] += (size[1] - text_height) / 2
        window.blit(text, pos)
