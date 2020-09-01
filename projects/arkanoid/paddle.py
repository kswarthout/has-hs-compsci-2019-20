import pygame


class Paddle(pygame.sprite.Sprite):
    '''Represents an arkanoid paddle'''

    def __init__(self, arena):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.arena = arena
        self.rect = self.image.get_rect()
        self.rect.bottom = self.arena.rect.bottom - self.arena.tileside

    def update(self):
        '''Updates paddle image on screen'''
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(self.arena.rect)
