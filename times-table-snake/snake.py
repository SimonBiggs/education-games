import pygame
import time
import random

from rx import subject


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

SCREEN_DIMENSIONS = (800, 600)
SNAKE_SEGMENT_DIMENSIONS = (15, 15)

TEXT_FONT = 'freesansbold.ttf'
TEXT_SIZE = 12

SPEED = 5

TIMES_TABLE_BASE = 2
TIMES_TABLE_RANGE = (0, 15)

NUMBER_OF_OPTIONS = 10

TITLE_START = f"{TIMES_TABLE_BASE} Times Tables   |    Maths Snake    |   "


class Controller:
    def __init__(self):
        self.running = True
        self._shutdown = subject.BehaviorSubject(False)
        self._shutdown.subscribe(self.on_shutdown)

    def reset(self):
        self.running = True
        self.shutdown = False

    @property
    def shutdown(self):
        return self._shutdown.value

    @shutdown.setter
    def shutdown(self, value):
        self._shutdown.on_next(value)

    def shutdown_callback(self):
        pass

    def on_shutdown(self, value):
        if value:
            self.shutdown_callback()


class SnakeSegment(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface(SNAKE_SEGMENT_DIMENSIONS)
        self.image.fill(WHITE)

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.momentum = (0, SPEED)

    def update(self):
        self.rect.x += self.momentum[0]
        self.rect.y += self.momentum[1]
        
        if self.rect.center[1] > SCREEN_DIMENSIONS[1]:
            self.rect.y -= SCREEN_DIMENSIONS[1]

        if self.rect.center[1] < 0:
            self.rect.y += SCREEN_DIMENSIONS[1]

        if self.rect.center[0] > SCREEN_DIMENSIONS[0]:
            self.rect.x -= SCREEN_DIMENSIONS[0]

        if self.rect.center[0] < 0:
            self.rect.x += SCREEN_DIMENSIONS[0]


class NumberFruit(pygame.sprite.Sprite):
    def __init__(self, x, y, number):
        super().__init__()

        font = pygame.font.Font(TEXT_FONT, TEXT_SIZE)
        surface = font.render(str(number), True, WHITE)
        self.rect = surface.get_rect()
        self.rect.center = (x, y)

        self.image = surface


MOMENTUM_MAP = {
    pygame.K_DOWN: (0, SPEED),
    pygame.K_UP: (0, -SPEED),
    pygame.K_LEFT: (-SPEED, 0),
    pygame.K_RIGHT: (SPEED, 0)
}

def main():
    pygame.init()
    display = pygame.display.set_mode(SCREEN_DIMENSIONS)

    controller = Controller()
    try:
        game_loop(display, controller)
    finally:    
        print("Quiting PyGame")
        pygame.quit()


def game_loop(display, controller):
    multiplier = random.randint(*TIMES_TABLE_RANGE)
    answer = multiplier * TIMES_TABLE_BASE
    title = f"{TITLE_START}{multiplier} x {TIMES_TABLE_BASE} = ?"

    pygame.display.set_caption(title)

    clock = pygame.time.Clock()

    snake_sprite_group = pygame.sprite.Group()
    numbers_sprite_group = pygame.sprite.Group()

    segment = SnakeSegment(50, 50)
    snake_sprite_group.add(segment)

    number_fruit = NumberFruit(100, 100, 1)
    numbers_sprite_group.add(number_fruit)

    while controller.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                try:
                    new_momentum = MOMENTUM_MAP[event.key]

                    for sprite in snake_sprite_group:
                        sprite.momentum = new_momentum

                except KeyError:
                    pass
        

        for sprite in snake_sprite_group:
            sprite.update()

        display.fill(BLACK)

        snake_sprite_group.draw(display)
        numbers_sprite_group.draw(display)

        pygame.display.flip()

        clock.tick(60)

    controller.shutdown = True

    


if __name__ == '__main__':
    main()