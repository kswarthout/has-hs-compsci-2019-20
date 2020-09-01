import pygame
from num_btn import NumButton


class NumsGrid:

    btn_labels = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    btns = []
    row_size = 2
    col_size = 5
    selected_num = 0

    def __init__(self, panel):
        # super().__init__()
        self.panel = panel

        # self.image = pygame.Surface(
        #     (self.panel.rect.width, 150)).convert()
        for btn_no, label in enumerate(self.btn_labels):
            row = 0
            if btn_no > 4:
                row = 1
            btn = NumButton(self.panel,
                            self,
                            label,
                            50,
                            50,
                            (255, 255, 255),
                            (0, 0, 255),
                            (255, 0, 255),
                            row,
                            btn_no % self.col_size)
            self.btns.append(btn)

    def select_num(self, num):
        self.panel.select_num(num)
