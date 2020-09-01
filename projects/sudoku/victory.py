import pygame


class VictoryAnimation():

    width = 100
    height = 100
    img_rects = [(width * 0, height * 0, width, height),  # row 1
                 (width * 1, height * 0, width, height),
                 (width * 2, height * 0, width, height),
                 (width * 3, height * 0, width, height),
                 (width * 4, height * 0, width, height),
                 (width * 5, height * 0, width, height),
                 (width * 0, height * 1, width, height),  # row 2
                 (width * 1, height * 1, width, height),
                 (width * 2, height * 1, width, height),
                 (width * 3, height * 1, width, height),
                 (width * 4, height * 1, width, height),
                 (width * 5, height * 1, width, height),
                 (width * 0, height * 2, width, height),  # row 3
                 (width * 1, height * 2, width, height),
                 (width * 2, height * 2, width, height),
                 (width * 3, height * 2, width, height),
                 (width * 4, height * 2, width, height),
                 (width * 5, height * 2, width, height),
                 (width * 0, height * 3, width, height),  # row 4
                 (width * 1, height * 3, width, height),
                 (width * 2, height * 3, width, height),
                 (width * 3, height * 3, width, height),
                 (width * 4, height * 3, width, height),
                 (width * 5, height * 3, width, height),
                 (width * 0, height * 4, width, height),  # row 5
                 (width * 1, height * 4, width, height),
                 (width * 2, height * 4, width, height),
                 (width * 3, height * 4, width, height),
                 (width * 4, height * 4, width, height),
                 (width * 5, height * 4, width, height),
                 (width * 0, height * 5, width, height),  # row 6
                 (width * 1, height * 5, width, height),
                 (width * 2, height * 5, width, height),
                 (width * 3, height * 5, width, height),
                 (width * 4, height * 5, width, height),
                 (width * 5, height * 5, width, height)]

    def __init__(self, pos):
        # pygame.sprite.Sprite.__init__(self, self.containers)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.pos = pos
        # self.rect.top = x
        # self.rect.left = y

    def update(self):
        '''Iterates through the elements inside of self.images and
        displays the next one on each tick.'''
        self.index += 1
        if self.index > len(self.images) - 1:
            self.index = 0
        self.image = self.images[self.index]

    def draw(self, window):
        window.blit(self.image, self.pos)


class Victory(pygame.sprite.Sprite):

    width = 100
    height = 100
    img_rects = [(width * 0, height * 0, width, height),  # row 1
                 (width * 1, height * 0, width, height),
                 (width * 2, height * 0, width, height),
                 (width * 3, height * 0, width, height),
                 (width * 4, height * 0, width, height),
                 (width * 5, height * 0, width, height),
                 (width * 0, height * 1, width, height),  # row 2
                 (width * 1, height * 1, width, height),
                 (width * 2, height * 1, width, height),
                 (width * 3, height * 1, width, height),
                 (width * 4, height * 1, width, height),
                 (width * 5, height * 1, width, height),
                 (width * 0, height * 2, width, height),  # row 3
                 (width * 1, height * 2, width, height),
                 (width * 2, height * 2, width, height),
                 (width * 3, height * 2, width, height),
                 (width * 4, height * 2, width, height),
                 (width * 5, height * 2, width, height),
                 (width * 0, height * 3, width, height),  # row 4
                 (width * 1, height * 3, width, height),
                 (width * 2, height * 3, width, height),
                 (width * 3, height * 3, width, height),
                 (width * 4, height * 3, width, height),
                 (width * 5, height * 3, width, height),
                 (width * 0, height * 4, width, height),  # row 5
                 (width * 1, height * 4, width, height),
                 (width * 2, height * 4, width, height),
                 (width * 3, height * 4, width, height),
                 (width * 4, height * 4, width, height),
                 (width * 5, height * 4, width, height),
                 (width * 0, height * 5, width, height),  # row 6
                 (width * 1, height * 5, width, height),
                 (width * 2, height * 5, width, height),
                 (width * 3, height * 5, width, height),
                 (width * 4, height * 5, width, height),
                 (width * 5, height * 5, width, height)]

    def __init__(self, panel):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.index = 0
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.top = panel.rect.top
        self.rect.left = panel.rect.left

    def update(self):
        '''Iterates through the elements inside of self.images and
        displays the next one on each tick.'''
        self.index += 1
        if self.index > len(self.images) - 1:
            self.index = 0
        self.image = self.images[self.index]
