import os
import importlib

import pygame
from watchdog import observers, events

from . import init, loop, constants, sprites

HERE = os.path.abspath(os.path.dirname(__file__))


def main():
    pygame.init()
    display = pygame.display.set_mode(constants.SCREEN_DIMENSIONS)

    path = os.path.join(HERE)    
    controller = init.Controller()
    state = init.State()

    def start_game():
        controller.reset()

        for package in [init, loop, constants, sprites]:
            importlib.reload(package)
            
        loop.game_loop(display, controller, state)

    controller.shutdown_callback = start_game

    def reboot_game(_):        
        controller.running = False

    event_handler = events.FileSystemEventHandler()
    event_handler.on_modified = reboot_game

    observer = observers.Observer()
    observer.schedule(event_handler, path)
    observer.start()
    
    start_game()
    

if __name__ == "__main__":
    main()