import pygame
import time
import random

from rx import subject

from . import constants, sprites


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


class State:
    def __init__(self):
        multiplier = random.randint(*constants.TIMES_TABLE_RANGE)
        answer = multiplier * constants.TIMES_TABLE_BASE
        title = f"{constants.TITLE_START}{multiplier} x {constants.TIMES_TABLE_BASE} = ?"

        pygame.display.set_caption(title)

        self.clock = pygame.time.Clock()

        self.snake_sprite_group = pygame.sprite.Group()
        self.numbers_sprite_group = pygame.sprite.Group()

        segment = sprites.SnakeSegment(50, 50)
        self.snake_sprite_group.add(segment)

        number_fruit = sprites.NumberFruit(100, 100, 1)
        self.numbers_sprite_group.add(number_fruit)
