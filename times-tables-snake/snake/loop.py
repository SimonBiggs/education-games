import pygame
import time
import random

from rx import subject

from . import constants, init


def game_loop(display, controller: init.Controller, state: init.State):
    while controller.running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

            if event.type == pygame.KEYDOWN:
                try:
                    new_momentum = constants.MOMENTUM_MAP[event.key]

                    for sprite in state.snake_sprite_group:
                        sprite.momentum = new_momentum

                except KeyError:
                    pass
        

        for sprite in state.snake_sprite_group:
            sprite.update()

        display.fill(constants.BLACK)

        state.snake_sprite_group.draw(display)
        state.numbers_sprite_group.draw(display)

        pygame.display.flip()

        state.clock.tick(60)

    controller.shutdown = True