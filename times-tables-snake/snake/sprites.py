import pygame

from . import constants


class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y, screen_size):
        super().__init__()

        self.image = pygame.Surface(constants.SNAKE_SEGMENT_DIMENSIONS)
        self.image.fill(constants.WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.momentum = (0, constants.SPEED)
        self.screen_size = screen_size

    def update(self):
        self.rect.x += self.momentum[0]
        self.rect.y += self.momentum[1]
        
        if self.rect.center[1] > self.screen_size[1]:
            self.rect.y -= self.screen_size[1]

        if self.rect.center[1] < 0:
            self.rect.y += self.screen_size[1]

        if self.rect.center[0] > self.screen_size[0]:
            self.rect.x -= self.screen_size[0]

        if self.rect.center[0] < 0:
            self.rect.x += self.screen_size[0]


class NumberFruit(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()

        font = pygame.font.Font(constants.TEXT_FONT, constants.TEXT_SIZE)
        surface = font.render(str(number), True, constants.WHITE)
        self.rect = surface.get_rect()
        self.rect.center = (x, y)

        self.image = surface