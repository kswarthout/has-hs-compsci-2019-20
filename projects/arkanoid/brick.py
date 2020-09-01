import pygame


class Brick(pygame.sprite.Sprite):
    def __init__(self, arena, x, y, color):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.image = self.images[color]
        self.rect = self.image.get_rect()
        self.rect.left = arena.rect.left + x*self.rect.width
        self.rect.top = arena.rect.top + y * self.rect.height
        self.hit_count = 0
        self.color = color
