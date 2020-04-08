import os
import importlib

import pygame
from watchdog import observers, events

from . import init, loop, constants, sprites

HERE = os.path.abspath(os.path.dirname(__file__))


def main():
    pygame.init()
    display = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    surface = pygame.display.get_surface()
    screen_size = surface.get_width(), surface.get_height()

    path = os.path.join(HERE)    
    controller = init.Controller()
    state = init.State(screen_size)

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