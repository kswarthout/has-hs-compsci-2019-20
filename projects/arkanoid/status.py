import pygame


class Status:

    def __init__(self):
        self.background = pygame.Surface((200, 34)).convert()
        self.background.blit(self.score_image, (0, 6))

        # available = pygame.font.get_fonts()
        # print(available)
        self.font = pygame.font.SysFont('bahnschrift', 22)
        self.score_text = self.font.render(
            '0', True, (255, 255, 255), (0, 0, 0))
        self.background.blit(self.score_text, (103, 0))
