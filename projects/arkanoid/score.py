import pygame


class Score(pygame.sprite.Sprite):
    def __init__(self, arena):
        # Call the parent class (Sprite) constructor
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.arena = arena

        self.font = pygame.font.SysFont("bahnschrift", 22)
        self.textSurf = self.font.render(str(arena.score), 1, (255, 255, 255))
        self.image = pygame.Surface((100, 34))
        W = self.textSurf.get_width()
        H = self.textSurf.get_height()
        self.image.blit(self.textSurf, (0, 0))
        self.rect = self.image.get_rect()
        self.rect.left = int(arena.rect.right + arena.tileside + 110)
        self.rect.top = int(arena.topy + 20)

    def update_score(self):
        self.image.fill((0, 0, 0))
        self.textSurf = self.font.render(
            str(self.arena.score), 1, (255, 255, 255))
        self.image.blit(self.textSurf, (0, 0))
