import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, msg, w, h, color, alt_color, text_color):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.color = color
        self.alt_color = alt_color
        self.text_color = text_color
        self.msg = msg

        self.image = pygame.Surface((w, h))
        self.rect = self.image.get_rect()

    def update(self):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        x = self.rect.left
        w = self.rect.width
        y = self.rect.top
        h = self.rect.height
        if x + w > mouse[0] > x and self.rect.top + h > mouse[1] > y:
            pygame.draw.rect(self.image, self.alt_color, (0, 0, w, h))

            if click[0] == 1:
                self.action()
        else:
            pygame.draw.rect(self.image, self.color, (0, 0, w, h))

        smallText = pygame.font.Font(None, 25)
        textSurf, textRect = self.text_objects(
            self.msg, smallText, self.text_color)
        textRect.center = (w/2, h/2)
        self.image.blit(textSurf, textRect)

    def text_objects(self, text, font, color):
        text_surface = font.render(text, True, color)
        return text_surface, text_surface.get_rect()
